import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from .tools.masks import get_masks_in_rois, get_masks_rois, scale_image
from .tools.conversions import to_objects_msg

import rclpy
import cv2
import numpy as np
import torch

from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

from ultralytics import YOLO

from segm_msgs.msg import Objects


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

        self.sub_image = self.create_subscription(
            # Image, "image", self.on_image, self.queue_size
            CompressedImage, "/cam2/zed_node_1/left/image_rect_color/compressed", self.on_image, self.queue_size

        )
        self.pub_segmentation = self.create_publisher(
            # Objects, "segmentation", self.queue_size
            Objects, "/yolo_segm", self.queue_size

        )

    def on_image(self, image_msg: CompressedImage):
        # image = self.br.imgmsg_to_cv2(image_msg, desired_encoding="passthrough")
        image = self.br.compressed_imgmsg_to_cv2(image_msg, desired_encoding="bgr8")

        segmentation_msg = self.process_img(image)
        segmentation_msg.header = image_msg.header

        self.pub_segmentation.publish(segmentation_msg)

    def process_img(self, image: np.ndarray) -> Objects:
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

        # print("SCALED", scaled_masks.shape, np.unique(scaled_masks, return_counts=True))
        rois = get_masks_rois(scaled_masks)
        masks_in_rois = get_masks_in_rois(scaled_masks, rois)

        distances = np.zeros(len(classes))

        segmentation_objects_msg = to_objects_msg(classes, masks_in_rois, rois, width, height, distances)

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