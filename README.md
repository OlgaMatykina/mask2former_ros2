# mask2former_ros2

Репозиторий содержит ROS2 (Foxy) интерфейс для работы с Mask2Former.

Представленные инструкции позволяют собрать 4 узла:

- __mask2former_node__, который слушает топик с изображениями и отправляет результаты сегментации в топик segmentation;
- __visualizer_node__, который слушает топики image и segmentation и визуализирует результаты сегментации, отправляя изображения в segmentation_color.
- __obstacle_node__, который слушает топики image, segmentation и depth,  вычисляет расстояния до всех препятствий, отправляет маски, категории препятствий и расстояния до них в топик obstacles. Также этот узел визуализирует маску ближайшего препятствия, отправляя изображения в топик obstacles_visualisation.
- __distance_node__, который слушает топики image, segmentation и depth, вычисляет расстояния до левого и правого края дороги, отправляет расстояния в топик distances, координаты левого и правого края дороги на изображении в топик coords_edge_2d, 3D координаты точек левого и правого края дороги относительно камеры в топик coords_edge_3d. Также этот узел визуализирует края дороги и расстояния до них, отправляя изображения в топик road_edge_vis
Создание образа из докер файла:
```
./build.sh
```

Запуск контейнера (предварительно заменить volumes):
```
./start.sh
```

Подключение к контейнеру:
```
./into.sh
```
Для того, чтобы настроить CUDA Kernel для MSDeformAttn выполнить следующие команды в контейнере:
```
cd ~/colcon_ws
./make_ops.sh
pip install torchinfo
```

## Проигрывание ros2 bag

Так как для публикации сообщений о препятствиях используется пользовательский тип сообщений __segm_msgs__, проигрывание бэга, содержащего все топики, требует предварительной установки пакета __segm_msgs__.

### Без CUDA

Возможно проигрывание бэга на компьютере без видео-карты NVIDIA, для этого нужно собрать и запустить образ командами
```
./build_no_cuda.sh
./start_no_cuda.sh
./into.sh
``` 
В Dockerfile_bridge_no_cuda устанавливается ros2 и torch без cuda, что позволит установить пакет пользовательского типа сообщений __segm_msgs__ и проиграть все топики бэга.

К данному моменту предполагается, что собран образ, запущен контейнер и выполнен вход в него.

Сначала необходимо собрать пакет пользовательского формата сообщений о препятствиях segm_msgs:

```
cd ~/colcon_ws
source /opt/ros/foxy/setup.bash
colcon build --packages-select segm_msgs  --symlink-install
source install/setup.bash 
```

Затем запустить launch, который автоматически запустит необходимые компоненты, передав значения аргументов:
1. camera_ns
2. image_topic
3. cfg

Можно использовать аргументы по умолчанию
```
ros2 launch semseg_ros2 mask2former_launch.py
```
Для тестирования работы узла нужно поместить [ROS-bag](https://drive.google.com/file/d/1xGdnAe4PTC17YMT0-ffMQ3HjWRG7DKks/view?usp=sharing) в папку ~/mask2former_ros2/colcon_ws.
Для запуска проигрывания в отдельном терминале:
```
cd ~/colcon_ws
source /opt/ros/foxy/setup.bash
source install/setup.bash 
ros2 bag play rosbag2_2024_07_23-04_25_52_0.db3
```
<!-- ros2 bag play -r 0.07 -s rosbag_v2 camera_2023-06-30-08-58-37_2.bag -->
Описание топиков:
```
/camera_left - данные с камеры
/depth_camera - данные с камеры глубины
/distances - расстояния до левого и правого края дороги
/obstacles - количество препятствий, их класс и маски
/obstacles_visualisation - визуализация препятсвий
/road_edge_vis - визуализация краев дороги и расстояний до них
/segmentation_color - визуализация маски дороги
/coords_edge_2d - координаты точек левого и правого края дороги на изображении 
/coords_edge_3d - 3D координаты точек левого и правого края дороги относительно камеры
```
Визуализировать результаты работы можно с помощью rviz
```
source /opt/ros/foxy/setup.bash
source install/setup.bash 
rviz2
```

## Работа с готовым пакетом

В настоящем репозитории представлен готовый к использованию ROS2 пакет семантической сегментации Mask2Former.

К данному моменту предполагается, что собран образ, запущен контейнер и выполнен вход в него.

Сначала необходимо собрать пакет (и пакет пользовательского формата сообщений о препятствиях segm_msgs):

```
cd ~/colcon_ws
source /opt/ros/foxy/setup.bash
colcon build --packages-select segm_msgs semseg_ros2 --symlink-install
source install/setup.bash 
```
После этого необходимо скачать веса по [ссылке](https://dl.fbaipublicfiles.com/maskformer/mask2former/mapillary_vistas/semantic/maskformer_R50_bs16_300k/model_final_6c66d0.pkl), переименовать в "maskformer_R50_bs16_300k.pkl" и поместить файл в папку 
```
~/maskformer_ros2/colcon_ws/src/semseg/weights
```
<!-- Затем нужно открыть конфигурационный файл, который расположен
```
~/oneformer_ros2/colcon_ws/src/semseg/weights/valid/swin/oneformer_swin_large_sem_seg_bs4_640k.yaml
```
и изменить название файла с весами (раскомментировать одну из строк):
```
  # WEIGHTS: /home/docker_oneformer_ros2/colcon_ws/src/semseg/weights/train1723_steps260k.pth
  # WEIGHTS: /home/docker_oneformer_ros2/colcon_ws/src/semseg/weights/train1723_steps210k.pth
```
-->
Затем запустить launch, который автоматически запустит необходимые компоненты, передав значения аргументов:
1. camera_ns
2. image_topic
3. cfg
```
ros2 launch semseg_ros2 mask2former_launch.py
```
Для тестирования работы узла нужно поместить ROS-bag в папку ~/mask2former_ros2/colcon_ws.
<!-- Для запуска проигрывания нужно сначала активировать окружение ROS1, затем ROS2: -->
Затем выполнить следующие команды, не забыть переименовать топики от текущей модели камеры в /camera_left и /depth_camera:


если бэг записан в ROS1 (расширение .bag):
```
cd ~/colcon_ws
source /opt/ros/noetic/setup.bash
source /opt/ros/foxy/setup.bash
ros2 bag play -r 0.15 -s rosbag_v2 2024-05-16-19-24-21_0.bag -l --remap /realsense_back/color/image_raw/compressed:=/camera_left /realsense_back/depth/image_rect_raw/compressedDepth:=/depth_camera
```

если бэг записан в ROS2 (расширение .db3):
```
cd ~/colcon_ws
source /opt/ros/foxy/setup.bash
ros2 bag play -r 0.15 rosbag2_2024_09_18-13_15_18_0.db3 -l --remap /cam1/zed_node_0/left/image_rect_color/compressed:=/camera_left /cam1/zed_node_0/depth/depth_registered:=/depth_camera
```
<!-- ros2 bag play -r 0.07 -s rosbag_v2 camera_2023-06-30-08-58-37_2.bag -->

Визуализировать результаты работы можно с помощью rviz
```
source /opt/ros/foxy/setup.bash
rviz2
```
