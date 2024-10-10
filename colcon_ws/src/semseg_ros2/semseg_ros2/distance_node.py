import rclpy
import cv2
import numpy as np
import message_filters
from rosidl_runtime_py.utilities import get_message

from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage
from semseg_ros2.road_detection import RoadEdgeDetection
from semseg_ros2 import  image_tools
from std_msgs.msg import Int32MultiArray, Float64MultiArray
from segm_msgs.msg import Obstacles, Edges2d, Coords2d, Edges3d, Coords3d
class DistanceNode(Node):
    def get_topic_type(self, topic_name):
        # Получаем тип сообщения
        msg_type = self.get_topic_names_and_types()
        # Извлекаем тип для нужного топика
        for name, types in msg_type:
            if name == topic_name:
                return types[0]  # Возвращаем первый тип
        return 'sensor_msgs/msg/Image'
    def __init__(self):
        super().__init__('distance_node')
        #print ('GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD GOOD')
        image_sub = message_filters.Subscriber(self, CompressedImage, 'image')
        segmentation_sub = message_filters.Subscriber(self, Image, 'segmentation')
         # Получаем тип сообщения
        self.depth_msg_type = self.get_topic_type('/depth_camera')
        
        # depth_sub = message_filters.Subscriber(self, CompressedImage, 'depth')
        depth_sub = message_filters.Subscriber(self, get_message(self.depth_msg_type), 'depth')
        # depth_sub = message_filters.Subscriber(self, CompressedImage,'/realsense_back/depth/image_rect_raw/compressedDepth')
        self.ts = message_filters.TimeSynchronizer([image_sub, segmentation_sub,depth_sub], 10)
        self.ts.registerCallback(self.road_edge_detection)

        self.distances = self.create_publisher(Float64MultiArray, 'distances', 10)
        self.road_edge_vis = self.create_publisher(Image, 'road_edge_vis', 10) 
        self.coords2d = self.create_publisher(Edges2d, 'coords_edge_2d', 10)
        self.coords3d = self.create_publisher(Edges3d, 'coords_edge_3d', 10)
        self.br = CvBridge()
        
    def road_edge_detection(self, image_msg: CompressedImage, segm_msg: Image, depth_msg):
        image = self.br.compressed_imgmsg_to_cv2(image_msg, desired_encoding='bgr8')
        height, width = image.shape[:2]
        mask = self.br.imgmsg_to_cv2(segm_msg, desired_encoding='mono8')
        
        road_mask = np.where(mask == 3, mask, 0)
        #negative = np.where(mask==1, mask, 0).astype(np.uint8)
        positive = np.where(mask==2, mask, 0).astype(np.uint8)

        if self.depth_msg_type == 'sensor_msgs/msg/CompressedImage':
            depth = image_tools.it.convert_compressedDepth_to_cv2(depth_msg)
        else:
            depth = self.br.imgmsg_to_cv2(depth_msg)

        # # depth = image_tools.it.convert_compressedDepth_to_cv2(depth_msg)
        # cropped_depth_map = depth[66:-66, 115:-115]
        # depth_map_resized = cv2.resize(cropped_depth_map, (width, height), interpolation=cv2.INTER_NEAREST)
        # depth_map_resized[depth_map_resized == 0] = 15000
        depth[depth == 0] = 45
        depth = np.nan_to_num(depth, nan=200, posinf=200, neginf=200)
        if np.sum(mask) > 300:
            road_detection = RoadEdgeDetection(image, road_mask, positive, depth)

            distances, road_edge_vis, edges2d_msg, edges3d_msg = road_detection.find_distances()
            cv2.imwrite('test.png', road_edge_vis)
        else:
            distances = [-1.0,-1.0]
            road_edge_vis = image
            edges2d_msg = Edges2d()
            edges2d_msg.left_side = self.get_empty_coords2d_msg()
            edges2d_msg.right_side = self.get_empty_coords2d_msg()

            edges3d_msg = Edges3d()

            edges3d_msg.left_side = self.get_empty_coords3d_msg()
            edges3d_msg.right_side = self.get_empty_coords3d_msg()

        distances_msg = Float64MultiArray()
        distances_msg.data = distances
        self.distances.publish(distances_msg)

        road_edge_vis_msg = self.br.cv2_to_imgmsg(road_edge_vis, 'bgr8')
        road_edge_vis_msg.header = segm_msg.header
        self.road_edge_vis.publish(road_edge_vis_msg)

        self.coords2d.publish(edges2d_msg)
        self.coords3d.publish(edges3d_msg)

    def get_empty_coords2d_msg(self):
        msg = Coords2d()
        msg.x = [-1]
        msg.y = [-1]
        return msg
    
    def get_empty_coords3d_msg(self):
        msg = Coords3d()
        msg.x = [-1]
        msg.y = [-1]
        msg.z = [-1]
        return msg

def main(args=None):
    rclpy.init(args=args)

    node = DistanceNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
        
        

