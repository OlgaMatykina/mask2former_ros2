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
            default_value='/home/docker_mask2former_ros2/colcon_ws/src/semseg/configs/vega_semantic/maskformer2_R50_bs16_300k.yaml'
        ),
        # launch.actions.DeclareLaunchArgument(
        #     'treshold',
        #     default_value='0.5'
        # ),

        # 
                # Настройка топиков
        launch.actions.DeclareLaunchArgument(
            'camera_ns',
            # default_value='/kitti/camera_color_left/'
            default_value=''
        ),
        launch.actions.DeclareLaunchArgument(
            'image_topic',
            # default_value= '/camera_left'
            default_value= '/cam2/zed_node_1/left/image_rect_color/compressed'
            # default_value='image_rect_color'
            # '/cam1/zed_node_0/left/image_rect_color/compressed' #'
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
            # default_value='/depth_camera'
            default_value='/cam2/zed_node_1/depth/depth_registered'
            # /cam1/zed_node_0/depth/depth_registered' #
        ),
        launch.actions.DeclareLaunchArgument(
            'obstacles_visualisation_topic',
            default_value='obstacles_visualisation'
        ),
        launch.actions.DeclareLaunchArgument(
            'obstacles_topic',
            default_value='obstacles'
        ),
        launch.actions.DeclareLaunchArgument(
            'distances_topic',
            default_value='distances'
        ),
        launch.actions.DeclareLaunchArgument(
            'road_edge_vis_topic',
            default_value='road_edge_vis'
        ),
        launch.actions.DeclareLaunchArgument(
            'coords_edge_2d_topic',
            default_value='coords_edge_2d'
        ),
        launch.actions.DeclareLaunchArgument(
            'coords_edge_3d_topic',
            default_value='coords_edge_3d'
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
        ),
        launch_ros.actions.Node(
            package='semseg_ros2',
            namespace=launch.substitutions.LaunchConfiguration('camera_ns'),
            executable='distance_node',
            name='distance_node',
            remappings=[
                ('image', launch.substitutions.LaunchConfiguration('image_topic')),
                ('segmentation', launch.substitutions.LaunchConfiguration('segmentation_topic')),
                ('depth', launch.substitutions.LaunchConfiguration('depth_topic')),
                ('distances', launch.substitutions.LaunchConfiguration('distances_topic')),
                ('road_edge_vis', launch.substitutions.LaunchConfiguration('road_edge_vis_topic')),
                ('coords_edge_2d', launch.substitutions.LaunchConfiguration('coords_edge_2d_topic')),
                ('coords_edge_3d', launch.substitutions.LaunchConfiguration('coords_edge_3d_topic'))

            ],
            output="screen"
        ),
        # launch.actions.ExecuteProcess(
        #     cmd=['ros2', 'bag', 'record', '-a'],
        #     output='screen'
        # )  
    ])
