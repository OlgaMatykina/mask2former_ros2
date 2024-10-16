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
from semseg_ros2.obstacle_detection import ObstacleDetection
from segm_msgs.msg import Obstacles, Objects

from .tools.conversions import from_objects_msg

import time

class MergeObstaclesNode(Node):
    def __init__(self):
        super().__init__('merge_obstacles_node')
        #print ('GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD')
        yolo_sub = message_filters.Subscriber(self, Objects, 'obstacles')
        mask2former_sub = message_filters.Subscriber(self, Objects, '/yolo_segm')

        self.ts = message_filters.TimeSynchronizer([yolo_sub, mask2former_sub], 10)
        self.ts.registerCallback(self.merge_obstacles)

        self.obstacles_pub = self.create_publisher(Objects, '/merged_obstacles', 10)

    def merge_obstacles(self, yolo_msg: Objects, m2f_msg: Objects):

        obstacles_msg = Objects()

        obstacles_msg.header = yolo_msg.header
        obstacles_msg.classes_ids = yolo_msg.classes_ids
        obstacles_msg.classes_ids.extend(m2f_msg.classes_ids)
        obstacles_msg.masks = yolo_msg.masks
        obstacles_msg.masks.extend(m2f_msg.masks)
        obstacles_msg.distances = yolo_msg.distances
        obstacles_msg.distances.extend(m2f_msg.distances)

        obstacles_msg.num = len(obstacles_msg.classes_ids)
        
        self.obstacles_pub.publish(obstacles_msg)

def main(args=None):
    rclpy.init(args=args)

    node = MergeObstaclesNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()