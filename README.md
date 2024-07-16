# mask2former_ros2

Репозиторий содержит ROS2 (Foxy) интерфейс для работы с Mask2Former.

Представленные инструкции позволяют собрать 2 узла:

- __mask2former_node__, который слушает топик с изображениями и отправляет результаты сегментации в топик segmentation_topic;
- __visualizer_node__, который слушает топики image и segmentation и визуализирует результаты сегментации, отправляя изображения в segmentation_color_topic.

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

## Работа с готовым пакетом

В настоящем репозитории представлен готовый к использованию ROS2 пакет семантической сегментации Mask2Former.

К данному моменту предполагается, что собран образ, запущен контейнер и выполнен вход в него.

Сначала необходимо собрать пакет:

```
cd ~/colcon_ws
source /opt/ros/foxy/setup.bash
colcon build --packages-select semseg_ros2 --symlink-install
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
Для запуска проигрывания нужно сначала активировать окружение ROS1, затем ROS2:
```
cd ~/colcon_ws
source /opt/ros/noetic/setup.bash
source /opt/ros/foxy/setup.bash
ros2 bag play -r 0.15 -s rosbag_v2 2024-05-16-19-24-21_0.bag
```
<!-- ros2 bag play -r 0.07 -s rosbag_v2 camera_2023-06-30-08-58-37_2.bag -->

Визуализировать результаты работы можно с помощью rviz
```
source /opt/ros/foxy/setup.bash
rviz2
```
