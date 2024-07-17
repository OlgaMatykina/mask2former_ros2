import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        # Параметры модели
        launch.actions.DeclareLaunchArgument(
            'cfg',
            # default_value='/home/docker_mask2former_ros2/colcon_ws/src/semseg/configs/mapillary-vistas/semantic-segmentation/swin/maskformer2_swin_large_IN21k_384_bs16_300k.yaml'
            default_value='/home/docker_mask2former_ros2/colcon_ws/src/semseg/configs/mapillary-vistas/semantic-segmentation/maskformer2_R50_bs16_300k.yaml'
        ),
        # launch.actions.DeclareLaunchArgument(
        #     'treshold',
        #     default_value='0.5'
        # ),

        # Настройка топиков
        launch.actions.DeclareLaunchArgument(
            'camera_ns',
            # default_value='/kitti/camera_color_left/'
            default_value='/realsense_back/'
        ),
        launch.actions.DeclareLaunchArgument(
            'image_topic',
            default_value='color/image_raw/compressed'
            # default_value='image_rect_color'
        ),
        launch.actions.DeclareLaunchArgument(
            'segmentation_topic',
            default_value='segmentation'
        ),
        launch.actions.DeclareLaunchArgument(
            'segmentation_color_topic',
            default_value='segmentation_color'
        ),
        launch.actions.DeclareLaunchArgument(
            'depth_topic',
            default_value='depth/image_rect_raw/compressedDepth'
        ),
        launch.actions.DeclareLaunchArgument(
            'obstacles_visualisation_topic',
            default_value='obstacles_visualisation'
        ),
        launch.actions.DeclareLaunchArgument(
            'obstacles_topic',
            default_value='obstacles'
        ),

        # Nodes
        launch_ros.actions.Node(
            package='semseg_ros2',
            namespace=launch.substitutions.LaunchConfiguration('camera_ns'),
            executable='mask2former_node',
            name='mask2former_node',
            remappings=[
                ('image', launch.substitutions.LaunchConfiguration('image_topic')),
                ('segmentation', launch.substitutions.LaunchConfiguration('segmentation_topic')),
            ],
            parameters=[
                {
                    'cfg': launch.substitutions.LaunchConfiguration('cfg'),
                    # 'treshold': launch.substitutions.LaunchConfiguration('treshold')
                }
            ],
            output="screen"
        ),

        launch_ros.actions.Node(
            package='semseg_ros2',
            namespace=launch.substitutions.LaunchConfiguration('camera_ns'),
            executable='visualizer_node',
            name='visualizer_node',
            remappings=[
                ('image', launch.substitutions.LaunchConfiguration('image_topic')),
                ('segmentation', launch.substitutions.LaunchConfiguration('segmentation_topic')),
                ('segmentation_color', launch.substitutions.LaunchConfiguration('segmentation_color_topic'))
            ],
            # parameters=[
            #     {
                    
            #     }
            # ],
            output="screen"
        ),
        launch_ros.actions.Node(
            package='semseg_ros2',
            namespace=launch.substitutions.LaunchConfiguration('camera_ns'),
            executable='obstacle_node',
            name='obstacle_node',
            remappings=[
                ('image', launch.substitutions.LaunchConfiguration('image_topic')),
                ('segmentation', launch.substitutions.LaunchConfiguration('segmentation_topic')),
                ('depth', launch.substitutions.LaunchConfiguration('depth_topic')),
                ('obstacles_visualisation', launch.substitutions.LaunchConfiguration('obstacles_visualisation_topic')),
                ('obstacles', launch.substitutions.LaunchConfiguration('obstacles_topic')),

            ],
            output="screen"
        )  
    ])
