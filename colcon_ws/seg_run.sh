source /opt/ros/foxy/setup.bash
colcon build --packages-select segm_msgs semseg_ros2 --symlink-install
source install/setup.bash
ros2 launch semseg_ros2 mask2former_launch.py