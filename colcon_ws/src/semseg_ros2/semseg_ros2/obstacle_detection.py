#import rosbag
#from cv_bridge import CvBridge
import cv2
#import image_tools
import numpy as np
import struct
import os
import time
from semseg.visualize import visualize
from segm_msgs.msg import Mask, Obstacles

class ObstacleDetection():
    def __init__(self, image, mask, depth):
        self.image = image
        self.mask = mask
        self.depth = depth

    def get_obstacles(self):
        negative = np.where(self.mask==1, self.mask, 0).astype(np.uint8)
        positive = np.where(self.mask==2, self.mask, 0).astype(np.uint8)
        msg = Obstacles()
        msg.classes_ids = []
        msg.masks = []
        msg.distances = []

        # instances_list = []
        # instance_id = 1
        for category_id, mask in enumerate([negative, positive]):
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                mask_msg = Mask()
                instance = np.zeros_like(mask)
                cv2.drawContours(instance, [contour], -1, 1, thickness = cv2.FILLED) #instance of obstacles
                instance = instance.astype('uint8')
                mask_msg.height, mask_msg.width = instance.shape[:2]
                mask_msg.mask = instance.flatten().tolist()

                obs_depth = np.where(instance, self.depth, 30000)
                min_dist = np.min(obs_depth)

                msg.classes_ids.append(category_id+1)
                msg.masks.append(mask_msg)
                msg.distances.append(min_dist)
                # instances_list.append(category_id+1)
                # instances_list.append(min_dist)
                # instances_list.append(instance)
                # # msg.id = instance_id
                # instance_id+=1
                # msg.category_id = category_id+1
                # msg.mask = instance
                # msg.distance = min_dist
        msg.num = len(msg.classes_ids)
        return msg
    
    def get_mask(self):
        obs_depth = np.where(self.mask, self.depth, 30000)
        min_dist = np.min(obs_depth)/1000
        if min_dist==30:
            min_dist=-1
        idx_min = np.argmin(obs_depth)
        pos_min = np.unravel_index(idx_min, obs_depth.shape)
        class_obs = self.mask[pos_min]
        # result_mask = np.full_like(self.mask, class_obs)
        mask_class_obs = np.where(self.mask==class_obs, class_obs, 0)
        mask_class_obs = np.array(mask_class_obs, dtype=np.uint8)
        # result_mask = mask_class_obs
        contours, _ = cv2.findContours(mask_class_obs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        result_mask = np.zeros_like(obs_depth)
        for contour in contours:
            ind = np.zeros_like(mask_class_obs)
            cv2.drawContours(ind, [contour], -1, 1, thickness = cv2.FILLED)
            if ind[pos_min]==1:
                cv2.drawContours(result_mask, [contour], -1, 1, thickness = cv2.FILLED)
                break
        result_mask = result_mask * class_obs
        # if np.all(result_mask==0):
        #     result_mask = np.full_like(self.mask,3)
        image = visualize(result_mask, self.image)
        image = cv2.putText(image, f'Min distance to obstacle:{round(min_dist,3)} m', (50,50), cv2.FONT_HERSHEY_SIMPLEX,  
                    1, (0, 0, 255), 2, cv2.LINE_AA)
        
        return image
            
        # min_dist = np.min(obs_depth)
        # idx_min = np.argmin(obs_depth)
        # pos_min = np.unravel_index(idx_min, obs_depth.shape)
        # class_obs = self.mask[idx_min]
        # mask_class_obs = np.where(self.mask==class_obs, self.mask, 0)
        # contours, _ = cv2.findContours(mask_class_obs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # result_mask = np.zeros_like(obs_depth)
        # for contour in contours:
        #     ind = np.zeros_like(mask_class_obs)
        #     cv2.drawContours(ind, [contour], -1, 1, thickness = cv2.FILLED)
        #     if ind[pos_min]==1:
        #         cv2.drawContours(result_mask, [contour], -1, 1, thickness = cv2.FILLED)
        #         break
        # return min_dist, class_obs, result_mask

