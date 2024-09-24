import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage
from cv_bridge import CvBridge
import cv2
import numpy as np

class DepthImageCompressor(Node):
    def __init__(self):
        super().__init__('depth_image_compressor')

        # Создаем подписчика на топик с глубинным изображением
        self.image_subscriber = self.create_subscription(
            Image,
            '/depth_camera_raw',  # Измените на ваш топик
            self.image_callback,
            10
        )

        # Публикуем сжатое изображение
        self.compressed_image_publisher = self.create_publisher(
            CompressedImage,
            '/depth_camera',
            10
        )

        # Используем CvBridge для конвертации между ROS и OpenCV
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            # Преобразуем сообщение ROS в изображение OpenCV
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')

            # Нормализуем изображение для корректного сжатия (так как глубинные карты могут быть в формате float32)
            # normalized_image = cv2.normalize(cv_image, None, 0, 255, cv2.NORM_MINMAX)
            normalized_image = np.uint16(cv_image)

            # Сжимаем изображение в формат JPEG
            success, compressed_image = cv2.imencode('.png', normalized_image)

            if success:
                # Создаем сообщение CompressedImage
                compressed_msg = CompressedImage()
                compressed_msg.header = msg.header
                compressed_msg.format = "png"
                compressed_msg.data = np.array(compressed_image).tobytes()

                # Публикуем сжатое изображение
                self.compressed_image_publisher.publish(compressed_msg)

        except Exception as e:
            self.get_logger().error(f"Ошибка при обработке изображения: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = DepthImageCompressor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()