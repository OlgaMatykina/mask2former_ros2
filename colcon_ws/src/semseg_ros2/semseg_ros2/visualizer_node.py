import rclpy
import cv2
import numpy as np
import message_filters

from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

# from semseg.oneform import SemanticSegmentator
# from semseg.visualizer import ColorMode, Visualizer
from semseg.visualize import visualize


class VisualizerNode(Node):

    def __init__(self):
        super().__init__('visualizer_node')

        print('INIT')

        image_sub = message_filters.Subscriber(self, CompressedImage, 'image')
        segmentation_sub = message_filters.Subscriber(self, Image, 'segmentation')

        self.ts = message_filters.TimeSynchronizer([image_sub, segmentation_sub], 10)
        self.ts.registerCallback(self.on_image_segmentation)

        self.pub_segmentation_color = self.create_publisher(Image, 'segmentation_color', 10)

        self.br = CvBridge()


    def on_image_segmentation(self, image_msg : CompressedImage, segm_msg : Image):
        image = self.br.compressed_imgmsg_to_cv2(image_msg, desired_encoding='bgr8')
        segmentation = self.br.imgmsg_to_cv2(segm_msg, desired_encoding='mono8')
        segmentation_color = visualize(segmentation, image)
        # print('COLOR')
        # print(segmentation_color)
        cv2.imwrite('/home/docker_mask2former_ros2/colcon_ws/src/semseg_ros2/semseg_ros2/2.png', segmentation_color)
        segm_color_msg = self.br.cv2_to_imgmsg(segmentation_color, 'bgr8')
        segm_color_msg.header = segm_msg.header

        self.pub_segmentation_color.publish(segm_color_msg)


def main(args=None):
    rclpy.init(args=args)

    node = VisualizerNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
