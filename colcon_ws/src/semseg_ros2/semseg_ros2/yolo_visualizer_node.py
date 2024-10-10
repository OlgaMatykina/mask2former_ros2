import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from yolo_visualization import draw_objects
from .tools.masks import reconstruct_masks

import rclpy
import cv2
import numpy as np
import message_filters

from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

from segm_msgs.msg import Objects


class YOLOVisualizerNode(Node):
    def __init__(self):
        super().__init__("yolo_visualizer_node")

        self.palette = coco_palette = (
            (220, 20, 60),   # person
            (119, 11, 32),   # bicycle
            (0, 0, 142),     # car
            (0, 0, 230),     # motorcycle
            (0, 80, 100),    # airplane
            (0, 0, 70),      # bus
            (0, 0, 192),     # train
            (0, 128, 0),     # truck
            (128, 64, 128),  # boat
            (250, 170, 30),  # traffic light
            (220, 220, 0),   # fire hydrant
            (0, 128, 128),   # stop sign
            (255, 255, 255), # parking meter
            (0, 255, 0),     # bench
            (165, 42, 42),   # bird
            (255, 0, 0),     # cat
            (0, 0, 255),     # dog
            (0, 255, 255),   # horse
            (255, 192, 203), # sheep
            (255, 255, 0),   # cow
            (192, 192, 192), # elephant
            (128, 128, 128), # bear
            (128, 0, 128),   # zebra
            (128, 128, 0),   # giraffe
            (255, 105, 180), # backpack
            (0, 255, 255),   # umbrella
            (255, 0, 255),   # handbag
            (255, 20, 147),  # tie
            (0, 0, 128),     # suitcase
            (0, 255, 0),     # frisbee
            (0, 128, 255),   # skis
            (0, 0, 0),       # snowboard
            (0, 255, 0),     # sports ball
            (128, 128, 128), # kite
            (255, 0, 0),     # baseball bat
            (0, 0, 255),     # baseball glove
            (255, 255, 0),   # skateboard
            (0, 128, 0),     # surfboard
            (128, 0, 255),   # tennis racket
            (128, 128, 128), # bottle
            (0, 255, 255),   # wine glass
            (255, 192, 203), # cup
            (220, 20, 60),   # fork
            (119, 11, 32),   # knife
            (0, 0, 142),     # spoon
            (0, 0, 230),     # bowl
            (0, 80, 100),    # banana
            (0, 0, 70),      # apple
            (0, 0, 192),     # sandwich
            (0, 128, 0),     # orange
            (128, 64, 128),  # broccoli
            (250, 170, 30),  # carrot
            (220, 220, 0),   # hot dog
            (0, 128, 128),   # pizza
            (255, 255, 255), # donut
            (0, 255, 0),     # cake
            (165, 42, 42),   # chair
            (255, 0, 0),     # couch
            (0, 0, 255),     # potted plant
            (0, 255, 255),   # bed
            (255, 192, 203), # dining table
            (0, 0, 128),     # toilet
            (0, 255, 0),     # TV
            (0, 128, 255),   # laptop
            (0, 0, 0),       # mouse
            (0, 255, 255),   # remote
            (255, 0, 255),   # keyboard
            (255, 20, 147),  # cell phone
            (0, 0, 128),     # microwave
            (0, 255, 0),     # oven
            (128, 128, 128), # toaster
            (0, 255, 255),   # sink
            (255, 192, 203), # refrigerator
            (220, 20, 60),   # book
            (119, 11, 32),   # clock
            (0, 0, 142),     # vase
            (0, 0, 230),     # scissors
            (0, 80, 100),    # teddy bear
            (0, 0, 70)       # hair drier
        )

        self.colors_palette = {
            0: {"bounds": (7, 7, 132), "inner": (36, 77, 201)},  # firehose
            1: {"bounds": (158, 18, 6), "inner": (196, 48, 35)},  # hose
            # 3: {"bounds": (96, 12, 107), "inner": (214, 80, 229)},  # waste
            # 4: {"bounds": (112, 82, 0), "inner": (255, 208, 79)},  # puddle
            # 5: {"bounds": (163, 0, 68), "inner": (244, 88, 153)},  # breakroad
        }

        self.declare_parameter("queue_size", 10)
        self.queue_size = (
            self.get_parameter("queue_size").get_parameter_value().integer_value
        )

        image_sub = message_filters.Subscriber(self, CompressedImage, "/cam2/zed_node_1/left/image_rect_color/compressed")
        segmentation_sub = message_filters.Subscriber(
            self, Objects, "/yolo_segm"
        )

        self.ts = message_filters.TimeSynchronizer(
            [image_sub, segmentation_sub], self.queue_size
        )
        self.ts.registerCallback(self.on_image_segmentation)

        self.pub_segmentation_color = self.create_publisher(
            Image, "/yolo_segm_color", self.queue_size
        )

        self.br = CvBridge()

    def on_image_segmentation(self, image_msg: CompressedImage, segm_msg: Objects):
        image = self.br.compressed_imgmsg_to_cv2(image_msg, desired_encoding="bgr8")

        # segmentation_color = self.draw_masks(
        #     image, segm_msg.masks, segm_msg.classes_ids
        # )

        types = {
            0: 'person',
            1: 'bicycle',
            2: 'car',
            3: 'motorcycle',
            4: 'airplane',
            5: 'bus',
            6: 'train',
            7: 'truck',
            8: 'boat',
            9: 'traffic light',
            10: 'fire hydrant',
            11: 'stop sign',
            12: 'parking meter',
            13: 'bench',
            14: 'bird',
            15: 'cat',
            16: 'dog',
            17: 'horse',
            18: 'sheep',
            19: 'cow',
            20: 'elephant',
            21: 'bear',
            22: 'zebra',
            23: 'giraffe',
            24: 'backpack',
            25: 'umbrella',
            26: 'handbag',
            27: 'tie',
            28: 'suitcase',
            29: 'frisbee',
            30: 'skis',
            31: 'snowboard',
            32: 'sports ball',
            33: 'kite',
            34: 'baseball bat',
            35: 'baseball glove',
            36: 'skateboard',
            37: 'surfboard',
            38: 'tennis racket',
            39: 'bottle',
            40: 'wine glass',
            41: 'cup',
            42: 'fork',
            43: 'knife',
            44: 'spoon',
            45: 'bowl',
            46: 'banana',
            47: 'apple',
            48: 'sandwich',
            49: 'orange',
            50: 'broccoli',
            51: 'carrot',
            52: 'hot dog',
            53: 'pizza',
            54: 'donut',
            55: 'cake',
            56: 'chair',
            57: 'couch',
            58: 'potted plant',
            59: 'bed',
            60: 'dining table',
            61: 'toilet',
            62: 'tv',
            63: 'laptop',
            64: 'mouse',
            65: 'remote',
            66: 'keyboard',
            67: 'cell phone',
            68: 'microwave',
            69: 'oven',
            70: 'toaster',
            71: 'sink',
            72: 'refrigerator',
            73: 'book',
            74: 'clock',
            75: 'vase',
            76: 'scissors',
            77: 'teddy bear',
            78: 'hair drier',
            79: 'toothbrush',

        }

        classes_names = [types[i] for i in segm_msg.classes_ids]

        segmentation_color = image.copy()
        masks = reconstruct_masks(segm_msg.masks)
        draw_objects(segmentation_color, None, segm_msg.classes_ids, masks=masks, draw_scores=False, draw_masks=True, draw_ids=True, palette=self.palette, customs=segm_msg.classes_ids)
        
        segm_color_msg = self.br.cv2_to_imgmsg(segmentation_color, "bgr8")
        segm_color_msg.header = segm_msg.header

        # print("Publishing visualization.")
        # print("Publishing.")
        self.pub_segmentation_color.publish(segm_color_msg)

    # def draw_masks(self, image, masks, classes):
    #     shape = image.shape
    #     line_thickness = max(1, int((shape[0] + shape[1]) / 2) // 400)

    #     for cls, mask in zip(classes, masks):
    #         mask = mask.mask_poly
    #         if not mask:
    #             continue
    #         mask = np.array(mask).reshape(len(mask) // 2, 2).tolist()

    #         mask_pattern = np.zeros(image.shape)
    #         cv2.fillPoly(
    #             mask_pattern, np.array([mask]), color=self.colors_palette[cls]["inner"]
    #         )
    #         image[mask_pattern > 0] = (
    #             0.5 * image[mask_pattern > 0] + 0.5 * mask_pattern[mask_pattern > 0]
    #         )

    #         cv2.polylines(
    #             image,
    #             np.array([mask]),
    #             isClosed=True,
    #             color=self.colors_palette[cls]["bounds"],
    #             thickness=line_thickness,
    #         )

    #     return image


def main(args=None):
    rclpy.init(args=args)

    node = YOLOVisualizerNode()
    node.get_logger().info("Visualizer node is ready")

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
