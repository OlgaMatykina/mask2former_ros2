import cv2
import numpy as np

def resize_depth(depth_map, left_image):
    # # Параметры камеры (предоставленные вами)
    # K = np.array([[423.958,   0.000, 427.216],
    #             [  0.000, 423.958, 240.158],
    #             [  0.000,   0.000,   1.000]])

    # # Предполагаемая базовая линза (может потребоваться калибровка для более точных данных)
    # baseline = 0.05  # Пример: базовая линза в 10 см

    # # Загрузка изображения с левой камеры
    # # left_image = cv2.imread('left_image.jpg')  # Подставьте свой путь к изображению
    # height, width = left_image.shape[:2]

    # # Загрузка карты глубины
    # # depth_map = cv2.imread('depth_map.png', cv2.IMREAD_UNCHANGED)  # Подставьте свой путь к карте глубины
    # depth_height, depth_width = depth_map.shape[:2]

    # # Размеры изображения и карты глубины
    # # print(f"Размер изображения с левой камеры: {width}x{height}")
    # # print(f"Размер карты глубины: {depth_width}x{depth_height}")

    # # Предположим среднее значение глубины в метрах (для вычисления сдвига)
    # average_depth = 2.0  # В метрах, это нужно скорректировать в зависимости от сцены

    # # Вычисление сдвига в пикселях
    # focal_length = K[0, 0]
    # shift_pixels = int((baseline * focal_length) / average_depth)
    # # print(f"Величина сдвига в пикселях: {shift_pixels}")

    # # Обрезка карты глубины справа на величину сдвига
    # cropped_depth_map = depth_map[:, :-shift_pixels]

    # # Ресэмплинг обрезанной карты глубины до разрешения изображения с камеры
    # depth_map_resized = cv2.resize(cropped_depth_map, (width, height), interpolation=cv2.INTER_NEAREST)

    height, width = left_image.shape[:2]
    cropped_depth_map = depth_map[66:-66, 115:-115]
    depth_map_resized = cv2.resize(cropped_depth_map, (width, height), interpolation=cv2.INTER_NEAREST)

    return depth_map_resized