import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from .tools.masks import get_masks_in_rois, get_masks_rois, scale_image
from .tools.conversions import to_objects_msg

import rclpy
import cv2
import numpy as np
import message_filters
import torch

from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

from ultralytics import YOLO

from segm_msgs.msg import Objects

REMAP_COCO = {
    0: 2,#'person',
    1: 2,#'bicycle',
    2: 2,#'car',
    3: 2,#'motorcycle',
    4: 0,#'airplane',
    5: 2,#'bus',
    6: 0,#'train',
    7: 2,#'truck',
    8: 2,#'boat',
    9: 0,#'traffic light',
    10: 2,# 'fire hydrant',
    11: 0,# 'stop sign',
    12: 0,# 'parking meter',
    13: 2,# 'bench',
    14: 0,# 'bird',
    15: 2,# 'cat',
    16: 2,# 'dog',
    17: 2,# 'horse',
    18: 2,# 'sheep',
    19: 2,# 'cow',
    20: 2,# 'elephant',
    21: 2,# 'bear',
    22: 2,# 'zebra',
    23: 2,# 'giraffe',
    24: 2,# 'backpack',
    25: 2,# 'umbrella',
    26: 2,# 'handbag',
    27: 0,# 'tie',
    28: 2,# 'suitcase',
    29: 0,# 'frisbee',
    30: 2,# 'skis',
    31: 2,# 'snowboard',
    32: 2,# 'sports ball',
    33: 0,# 'kite',
    34: 2,# 'baseball bat',
    35: 0,# 'baseball glove',
    36: 2,# 'skateboard',
    37: 2,# 'surfboard',
    38: 2,# 'tennis racket',
    39: 2,# 'bottle',
    40: 0,# 'wine glass',
    41: 0,# 'cup',
    42: 0,# 'fork',
    43: 0,# 'knife',
    44: 0,# 'spoon',
    45: 0,# 'bowl',
    46: 0,# 'banana',
    47: 0,# 'apple',
    48: 0,# 'sandwich',
    49: 0,# 'orange',
    50: 0,# 'broccoli',
    51: 0,# 'carrot',
    52: 0,# 'hot dog',
    53: 0,# 'pizza',
    54: 0,# 'donut',
    55: 0,# 'cake',
    56: 2,# 'chair',
    57: 2,# 'couch',
    58: 2,# 'potted plant',
    59: 2,# 'bed',
    60: 2,# 'dining table',
    61: 0,# 'toilet',
    62: 0,# 'tv',
    63: 0,# 'laptop',
    64: 0,# 'mouse',
    65: 0,# 'remote',
    66: 0,# 'keyboard',
    67: 0,# 'cell phone',
    68: 0,# 'microwave',
    69: 0,# 'oven',
    70: 0,# 'toaster',
    71: 0,# 'sink',
    72: 0,# 'refrigerator',
    73: 0,# 'book',
    74: 0,# 'clock',
    75: 0,# 'vase',
    76: 0,# 'scissors',
    77: 0,# 'teddy bear',
    78: 0,# 'hair drier',
    79: 0,# 'toothbrush',
}


class YOLOv11SegNode(Node):
    def __init__(self) -> None:
        super().__init__("yolov11_seg_node")

        self.declare_parameter(
            "weights",
            "/home/docker_mask2former_ros2/colcon_ws/src/semseg/weights/yolo11m-seg.pt",
            )
        self.weights = self.get_parameter("weights").get_parameter_value().string_value

        self.declare_parameter("device", "cuda:0")
        self.device = self.get_parameter("device").get_parameter_value().string_value

        if self.device != "cpu":
            if not torch.cuda.is_available():
                self.device = "cpu"

        self.declare_parameter("confidence", 0.5)
        self.confidence = (
            self.get_parameter("confidence").get_parameter_value().double_value
        )

        self.declare_parameter("treshold", 0.5)
        self.treshold = (
            self.get_parameter("treshold").get_parameter_value().double_value
        )

        self.declare_parameter("queue_size", 10)
        self.queue_size = (
            self.get_parameter("queue_size").get_parameter_value().integer_value
        )

        self.get_logger().info("Init segmentator")
        self.segmentator = YOLO(self.weights)
        warmup_img = np.ones((720, 1280, 3))
        self.segmentator(warmup_img)

        self.br = CvBridge()

        image_sub = message_filters.Subscriber(self, CompressedImage, "image")

        # self.sub_image = self.create_subscription(
        #     # Image, "image", self.on_image, self.queue_size
        #     CompressedImage, "/cam2/zed_node_1/left/image_rect_color/compressed", self.on_image, self.queue_size

        # )

        depth_sub = message_filters.Subscriber(self, Image, "depth")


        self.ts = message_filters.TimeSynchronizer([image_sub, depth_sub], self.queue_size)
        self.ts.registerCallback(self.on_image)


        self.pub_segmentation = self.create_publisher(
            # Objects, "segmentation", self.queue_size
            Objects, "/yolo_segm", self.queue_size

        )

    def on_image(self, image_msg: CompressedImage, depth_msg: Image):
        # image = self.br.imgmsg_to_cv2(image_msg, desired_encoding="passthrough")
        image = self.br.compressed_imgmsg_to_cv2(image_msg, desired_encoding="bgr8")

        depth = self.br.imgmsg_to_cv2(depth_msg)
        depth[depth == 0] = 45
        depth = np.nan_to_num(depth, nan=200, posinf=200, neginf=200)

        segmentation_msg = self.process_img(image, depth)
        segmentation_msg.header = image_msg.header

        self.pub_segmentation.publish(segmentation_msg)

    def process_img(self, image: np.ndarray, depth: np.ndarray) -> Objects:
        predictions = self.segmentator(
            image, device=self.device, conf=self.confidence, iou=self.treshold
        )[0]

        conf = predictions.boxes.conf.cpu().numpy().astype(np.float32).tolist()

        classes = predictions.boxes.cls.cpu().numpy().astype(np.uint8).tolist()

        # boxes = predictions.boxes.xyxy.cpu().numpy()
        # boxes = boxes.astype(np.uint32).tolist()
        masks = predictions.masks
        height, width = predictions.orig_shape
        if masks is None:
            masks = np.array([])
            scaled_masks = np.empty((0, *(height, width)), dtype=np.uint8)
        else:
            # masks = masks.xy
            masks = masks.data.cpu().numpy().astype(np.uint8)
            # print("MASKS", masks.shape, np.unique(masks, return_counts=True))
            mask_height, mask_width = masks.shape[1:]
            masks = masks.transpose(1, 2, 0)
            scaled_masks = scale_image((mask_height, mask_width), masks, (height, width))
            scaled_masks = scaled_masks.transpose(2, 0, 1)

        idx = np.where(np.all(scaled_masks==0, axis=(1,2)))[0]
        scaled_masks = np.delete(scaled_masks, idx, axis=0)
        classes = np.delete(classes, idx, axis=0)

        remapped_classes = np.array([REMAP_COCO[cat] for cat in classes])
        idx = np.where(remapped_classes==0)[0]
        remapped_classes = np.delete(remapped_classes, idx, axis=0)
        scaled_masks = np.delete(scaled_masks, idx, axis=0)

        # print("SCALED", scaled_masks.shape, np.unique(scaled_masks, return_counts=True))
        rois = get_masks_rois(scaled_masks)
        # self.get_logger().info(f"SCALES MASKS SHAPE {scaled_masks.shape}")
        masks_in_rois = get_masks_in_rois(scaled_masks, rois)

        # distances = np.zeros(len(remapped_classes))
        distances = []

        
        # masks_in_rois = np.delete(masks_in_rois, idx, axis=0)
        # rois = np.delete(rois, idx, axis=0)
        # distances = np.delete(distances, idx, axis=0)
        depth = np.expand_dims(depth, axis=0)

        depths = np.tile(depth, (len(remapped_classes), 1, 1))
        # self.get_logger().info(f"DEPTHs SHAPE {depths.shape}")

        depth_in_rois = get_masks_in_rois(depths, rois)
        # self.get_logger().info(f"DEPTH IN ROIS SHAPE {depth_in_rois.shape}")
        # self.get_logger().info(f"MASKS IN ROIS SHAPE {masks_in_rois.shape}")

        for mask, depth in zip(masks_in_rois, depth_in_rois):
            obs_depth = np.where(mask, depth, 50)
            min_dist = np.min(obs_depth)
            if min_dist==50:
                min_dist=-1
            distances.append(min_dist)

        segmentation_objects_msg = to_objects_msg(remapped_classes, masks_in_rois, rois, width, height, distances)

        return segmentation_objects_msg


def main(args=None):
    rclpy.init(args=args)

    node = YOLOv11SegNode()
    node.get_logger().info("Segmentation node is ready")

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()