from rosbag import Bag

with Bag('/home/matykina_ov/mask2former_ros2/colcon_ws/renamed2024-05-16-19-24-21_0.bag', 'w') as Y:
    for topic, msg, t in Bag('/home/matykina_ov/mask2former_ros2/colcon_ws/2024-05-16-19-24-21_0.bag'):
        if topic == '/realsense_back/color/camera_info':
            Y.write('/camera_left_info', msg, t)
        elif topic == '/realsense_back/color/image_raw/compressed':
            Y.write('/camera_left', msg, t)
        elif topic == '/realsense_back/depth/camera_info':
            Y.write('/depth_camera_info', msg, t)
        elif topic == '/realsense_back/depth/image_rect_raw/compressedDepth':
            Y.write('/depth_camera', msg, t)
        else:
            Y.write(topic, msg, t)