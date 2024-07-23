import os
from glob import glob
from setuptools import setup

package_name = 'semseg_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*_launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='docker_semseg',
    maintainer_email='docker_semseg@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mask2former_node = semseg_ros2.mask2former_node:main',
            'visualizer_node = semseg_ros2.visualizer_node:main',
            'obstacle_node = semseg_ros2.obstacle_node:main',
            # 'inference_meter_node = semseg_ros2.inference_meter_node:main',
            'distance_node = semseg_ros2.distance_node:main',
        ],
    },
)
