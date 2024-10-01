import rclpy
import cv2
import numpy as np
import message_filters
from rosidl_runtime_py.utilities import get_message

from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage
from semseg_ros2 import  image_tools
from semseg_ros2.depth import resize_depth
from std_msgs.msg import Int32MultiArray, Float64MultiArray
# from segm_msgs.segm_msgsfin import InstanceSegmentationList
from semseg_ros2.obstacle_detection import ObstacleDetection
from segm_msgs.msg import Obstacles

import time

class ObstacleNode(Node):
    def get_topic_type(self, topic_name):
        # Получаем тип сообщения
        msg_type = self.get_topic_names_and_types()
        # print('TYPES', msg_type)
        # Извлекаем тип для нужного топика
        for name, types in msg_type:
            if name == topic_name:
                return types[0]  # Возвращаем первый тип
        return 'sensor_msgs/msg/CompressedImage'
    def __init__(self):
        super().__init__('obstacle_node')
        #print ('GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD')
        image_sub = message_filters.Subscriber(self, CompressedImage, 'image')
        segmentation_sub = message_filters.Subscriber(self, Image, 'segmentation')
        
        # Получаем тип сообщения
        self.depth_msg_type = self.get_topic_type('/depth_camera')

        print('TYPE', self.depth_msg_type)
        
        # depth_sub = message_filters.Subscriber(self, CompressedImage, 'depth')
        depth_sub = message_filters.Subscriber(self, get_message(self.depth_msg_type), '/depth_camera')

        self.ts = message_filters.TimeSynchronizer([image_sub, segmentation_sub, depth_sub], 10)
        self.ts.registerCallback(self.obstacle_detection)

        self.obstacles_vis_pub = self.create_publisher(Image, 'obstacles_visualisation', 10)
        self.obstacles_pub = self.create_publisher(Obstacles, 'obstacles', 10)

        self.br = CvBridge()

    # def obstacle_detection(self, image_msg: CompressedImage, segm_msg: Image, depth_msg: CompressedImage):
    def obstacle_detection(self, image_msg: CompressedImage, segm_msg: Image, depth_msg):
        image = self.br.compressed_imgmsg_to_cv2(image_msg, desired_encoding='bgr8')
        # cv2.imwrite('/home/docker_mask2former_ros2/colcon_ws/src/semseg_ros2/semseg_ros2/0.png', image)
        mask = self.br.imgmsg_to_cv2(segm_msg, desired_encoding='mono8')
        mask = np.where(np.isin(mask, [1,2]),mask,0)
        mask[-90:] = 0
        if self.depth_msg_type == 'sensor_msgs/msg/CompressedImage':
            depth = image_tools.it.convert_compressedDepth_to_cv2(depth_msg)
        else:
            depth = self.br.imgmsg_to_cv2(depth_msg)
        # depth = resize_depth(depth, image)
        # cv2.imwrite('/home/docker_mask2former_ros2/colcon_ws/src/semseg_ros2/semseg_ros2/3.png', depth)
        # print('MAX_DEPTH', np.max(depth, axis=0))
        depth[depth == 0] = 45
        depth = np.nan_to_num(depth, nan=200, posinf=200, neginf=200)
        obstacle_detection = ObstacleDetection(image, mask, depth)

        # obstacle_msg = Float64MultiArray()

        start_time = time.time()
        obstacles_msg = obstacle_detection.get_obstacles()
        end_time = time.time()
        processing_time = (end_time - start_time) * 1000  # в миллисекундах
        # self.get_logger().info(f'Processing time: {processing_time:.2f} ms')
        obstacles_msg.header = image_msg.header
        self.obstacles_pub.publish(obstacles_msg)

        obstacles_vis = obstacle_detection.get_mask()
        # cv2.imwrite('/home/docker_mask2former_ros2/colcon_ws/src/semseg_ros2/semseg_ros2/4.png', obstacles_vis)
        obstacles_vis_msg = self.br.cv2_to_imgmsg(obstacles_vis, 'bgr8')
        obstacles_vis_msg.header = image_msg.header
        
        self.obstacles_vis_pub.publish(obstacles_vis_msg)
def main(args=None):
    rclpy.init(args=args)

    node = ObstacleNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
        
        

