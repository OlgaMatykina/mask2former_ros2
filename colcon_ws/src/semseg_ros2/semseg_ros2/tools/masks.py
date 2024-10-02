import numpy as np
from numbers import Number
import cv2


def get_masks_rois(masks):
    if len(masks) == 0:
        return np.empty((0,), dtype=object)

    if isinstance(masks, np.ndarray) and masks.ndim == 2:
        masks = np.expand_dims(masks, axis=0)
        extended = True
    else:
        extended = False

    rows = np.any(masks, axis=2)
    cols = np.any(masks, axis=1)

    rois = list()
    for rs, cs in zip(rows, cols):
        y_min, y_max = np.where(rs)[0][[0, -1]]
        x_min, x_max = np.where(cs)[0][[0, -1]]
        roi = (slice(y_min, y_max + 1), slice(x_min, x_max + 1))
        rois.append(roi)

    if extended:
        rois = rois[0]
    else:
        rois = np.array(rois + [None], dtype=object)[:-1]
    return rois


def get_masks_in_rois(masks, rois, copy=True):
    if len(masks) == 0 and len(rois) == 0:
        return np.empty((0,), dtype=object)

    if isinstance(masks, np.ndarray) and masks.ndim == 2:
        masks = np.expand_dims(masks, axis=0)
        rois = [rois]
        extended = True
    else:
        extended = False

    if len(masks) != len(rois):
        raise RuntimeError("Number of masks and rois is not equal.")

    masks_in_rois = list()
    for mask, roi in zip(masks, rois):
        mask_in_roi = mask[roi]
        if copy:
            masks_in_rois.append(mask_in_roi.copy())
        else:
            masks_in_rois.append(mask_in_roi)

    if extended:
        masks_in_rois = masks_in_rois[0]
    else:
        masks_in_rois = np.array(masks_in_rois + [None], dtype=object)[:-1]
    return masks_in_rois

def scale_image(im1_shape, masks, im0_shape, ratio_pad=None):
    """
    Takes a mask, and resizes it to the original image size

    Args:
      im1_shape (tuple): model input shape, [h, w]
      masks (torch.Tensor): [h, w, num]
      im0_shape (tuple): the original image shape
      ratio_pad (tuple): the ratio of the padding to the original image.

    Returns:
      masks (torch.Tensor): The masks that are being returned.
    """
    # Rescale coordinates (xyxy) from im1_shape to im0_shape
    if ratio_pad is None:  # calculate from im0_shape
        gain = min(im1_shape[0] / im0_shape[0], im1_shape[1] / im0_shape[1])  # gain  = old / new
        pad = (im1_shape[1] - im0_shape[1] * gain) / 2, (im1_shape[0] - im0_shape[0] * gain) / 2  # wh padding
    else:
        pad = ratio_pad[1]
    top, left = int(pad[1]), int(pad[0])  # y, x
    bottom, right = int(im1_shape[0] - pad[1]), int(im1_shape[1] - pad[0])

    if len(masks.shape) < 2:
        raise ValueError(f'"len of masks shape" should be 2 or 3, but got {len(masks.shape)}')
    masks = masks[top:bottom, left:right]
    # masks = masks.permute(2, 0, 1).contiguous()
    # masks = F.interpolate(masks[None], im0_shape[:2], mode='bilinear', align_corners=False)[0]
    # masks = masks.permute(1, 2, 0).contiguous()
    masks = cv2.resize(masks, (im0_shape[1], im0_shape[0]))

    if len(masks.shape) == 2:
        masks = masks[:, :, None]
    return masks

def reconstruct_masks(mask_messages):
    # Проходим по каждому объекту Mask и восстанавливаем маски
    reconstructed_masks = []

    for mask_msg in mask_messages:
        # Создаем пустую маску с размерами оригинального изображения
        full_mask = np.zeros((mask_msg.height, mask_msg.width), dtype=np.uint8)

        # Извлекаем данные ROI
        roi_x = mask_msg.roi.x
        roi_y = mask_msg.roi.y
        roi_width = mask_msg.roi.width
        roi_height = mask_msg.roi.height

        # Преобразуем одномерный массив mask_in_roi в двумерный по размерам ROI
        mask_in_roi_2d = np.array(mask_msg.mask_in_roi, dtype=np.uint8).reshape(roi_height, roi_width)

        # Вставляем маску обратно в исходную область изображения
        full_mask[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width] = mask_in_roi_2d

        # Добавляем восстановленную маску в список
        reconstructed_masks.append(full_mask)

    # Возвращаем список восстановленных масок
    return reconstructed_masks