import numpy as np
import cv2

mask_class_obs = np.array([
    [0,0,0,0,2],
    [0,0,0,0,2],
    [0,2,0,0,2],
    [2,2,0,0,2],
], dtype=np.uint8)

pos_min = (2,1)

print(mask_class_obs[pos_min])

# individual_masks = []

contours, _ = cv2.findContours(mask_class_obs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result_mask = np.zeros_like(mask_class_obs)
for contour in contours:
    # print(contour)
    ind = np.zeros_like(mask_class_obs)
    # print(ind)
    cv2.drawContours(ind, [contour], -1, 1, thickness = cv2.FILLED)
    # individual_masks.append(ind)
    if ind[pos_min]==1:
        print('FIND')
        cv2.drawContours(result_mask, [contour], -1, 1, thickness = cv2.FILLED)
        break
print(result_mask)
# for ind in individual_masks:
#     print(ind)