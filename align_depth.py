import rosbag
import cv2
import numpy as np
import pyrealsense2 as rs
from cv_bridge import CvBridge
from colcon_ws.src.semseg_ros2.semseg_ros2 import image_tools

# Функция для извлечения изображений и карт глубины из rosbag
def extract_images_from_rosbag(bag_file, rgb_topic, depth_topic):
    bridge = CvBridge()
    bag = rosbag.Bag(bag_file, 'r')
    rgb_images = []
    depth_images = []

    for topic, msg, t in bag.read_messages(topics=[rgb_topic, depth_topic]):
        if topic == rgb_topic:
            rgb_image = bridge.compressed_imgmsg_to_cv2(msg)
            rgb_images.append(rgb_image)
        elif topic == depth_topic:
            # depth_image = bridge.compressed_depth_imgmsg_to_cv2(msg)
            depth_image = image_tools.it.convert_compressedDepth_to_cv2(msg)
            depth_images.append(depth_image)

    bag.close()
    return rgb_images, depth_images

# Функция для выравнивания глубины к RGB с использованием pyrealsense2
def align_depth_to_color():
    # Настройка конвейера Realsense
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_device_from_file(bag_file)
    
    # Создание виртуальных устройств
    # color_virtual_sensor = rs.sensor()
    # depth_virtual_sensor = rs.sensor()
    
    # Начало конвейера с виртуальными устройствами
    pipeline.start(config)

    # Выравнивание глубины к RGB
    align = rs.align(rs.stream.color)
    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)
    
    aligned_depth_frame = aligned_frames.get_depth_frame()
    
    # Преобразование кадра глубины в numpy array
    aligned_depth_image = np.asanyarray(aligned_depth_frame.get_data())
    
    pipeline.stop()
    return aligned_depth_image

# Основной код
bag_file = '/home/matykina_ov/mask2former_ros2/colcon_ws/2024-05-16-19-24-21_0.bag'
rgb_topic = '/realsense_back/color/image_raw/compressed'
depth_topic = '/realsense_back/depth/image_rect_raw/compressedDepth'

# rgb_images, depth_images = extract_images_from_rosbag(bag_file, rgb_topic, depth_topic)

# Пример выравнивания для одного кадра
aligned_depth_image = align_depth_to_color()

# Проверка результатов
cv2.imwrite('/home/matykina_ov/mask2former_ros2/depth.png', aligned_depth_image)
# cv2.imshow('/home/matykina_ov/mask2former_ros2/rgb.png', rgb_images[0])