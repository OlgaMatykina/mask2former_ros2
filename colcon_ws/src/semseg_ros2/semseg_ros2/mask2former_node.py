import rclpy
import cv2

from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

from semseg.mask2form import SemanticSegmentator
from semseg_ros2.inference_speed_meter import InferenceSpeedMeter
from semseg.visualize import visualize
import time
import numpy as np

class SemSegNode(Node):

    def __init__(self) -> None:
        super().__init__('mask2former_node')

        self.declare_parameter('cfg')
        self.cfg = self.get_parameter('cfg').get_parameter_value().string_value

        # self.declare_parameter('treshold', 0.5)
        # self.treshold = self.get_parameter('treshold').get_parameter_value().double_value


        # print(self.cat_num)
        # print(type(self.cat_num))

        self.segmentator = SemanticSegmentator(self.cfg)

        self.br = CvBridge()

        self.sub_image = self.create_subscription(CompressedImage, 'image', self.on_image, 10)
        self.pub_segmentation = self.create_publisher(Image, 'segmentation', 10)

        # self.speed_meter = InferenceSpeedMeter()


    def on_image(self, image_msg : CompressedImage):
        image = self.br.compressed_imgmsg_to_cv2(image_msg, desired_encoding='bgr8')

        # self.speed_meter.start()
        start_time = time.time()
        segmentation = self.segmentator.inference(image)
        # print('SEGMENTATION')
        # print(np.unique(segmentation, return_counts=True))
        # print(segmentation.shape)
        # cv2.imwrite('/home/docker_mask2former_ros2/colcon_ws/src/semseg_ros2/semseg_ros2/1.png', segmentation)
        # cv2.imwrite('/home/docker_mask2former_ros2/colcon_ws/src/semseg_ros2/semseg_ros2/2.png', self.segmentator.colorize(segmentation))
        # cv2.imwrite('/home/docker_mask2former_ros2/colcon_ws/src/semseg_ros2/semseg_ros2/2.png', visualize(segmentation, image))
        # self.speed_meter.stop()
        segmentation[-90:] = np.where(segmentation[-90:],3,0)
        end_time = time.time()
        processing_time = (end_time - start_time) * 1000  # в миллисекундах
        # self.get_logger().info(f'Processing time: {processing_time:.2f} ms')

        segmentation_msg = self.br.cv2_to_imgmsg(segmentation, 'mono8')
        segmentation_msg.header = image_msg.header

        self.pub_segmentation.publish(segmentation_msg)


def main(args=None):
    rclpy.init(args=args)

    node = SemSegNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
