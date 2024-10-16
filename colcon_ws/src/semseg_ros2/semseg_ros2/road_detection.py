#import rosbag
#from cv_bridge import CvBridge
import cv2
#import image_tools
import numpy as np
import struct
import os
import time
from segm_msgs.msg import Edges2d, Edges3d, Coords2d, Coords3d

class RoadEdgeDetection():
    def __init__(self, image, mask, positive, depth, header):
        self.image = image
        self.mask = mask
        self.depth = depth
        self.positive = positive
        self.header = header
    #def get_xyz(self, x_p,y_p,Z,c_x = 427.2,c_y=240.15,f_x=423.96,f_y=423.96):
    def get_xyz(self, x_p,y_p,Z,c_x = 628.25,c_y=354.76 ,f_x=954.4,f_y=954.4):
        X = (x_p - c_x) * Z / f_x
        Y = (y_p - c_y) * Z / f_y
        dist = np.sqrt(X**2 + Y**2 + Z**2)
        return X, abs(Y), Z, dist

    def grouped(self, iterable, n):
        return zip(*[iter(iterable)]*n)

    def get_max_contour(self, contours):
        areas = [cv2.contourArea(cont) for cont in contours]
        MaxVal = max(areas)
        index_max = areas.index(MaxVal)
        return contours[index_max]

    def delete_edges(self,cnt,mask):
        idx1 = np.where(cnt[:,0] >= mask.shape[1] - 5)
        idx2 = np.where(cnt[:,0] <= 5)
        idx3 = np.where(cnt[:,1] >= mask.shape[0] - 5)
        idx = np.hstack(( idx1,idx2,idx3 )).ravel()
        cnt = np.delete(cnt, idx, 0)
        return cnt
    def get_mean_point(self,cnt, radius = 200):
        #min_y = np.max(cnt[:,1])
        #idx = np.where((cnt[:,1] >= min_y - radius) & (min_y >= cnt[:,1]) )
        #point1 = np.min(cnt[idx][:,0])
        #point2 = np.max(cnt[idx][:,0])
        #return int((point1 + point2)/2)
        left_point = np.min(cnt[:,0])
        right_point  = np.max(cnt[:,0])
    
        return int ((left_point + right_point)/2)

    def get_left_side(self,cnt, mean_point):
        idx_left = cnt[:,0] <= mean_point - 30
        return cnt[idx_left]

    def get_right_side(self,cnt, mean_point):
        idx_right = cnt[:,0] >= mean_point + 30
        return cnt[idx_right]
    
    def find_distances(self):
        #k1 = 479 / 720
        #k2 = 847 / 1280
    
        ret, mask = cv2.threshold(self.mask , 0, 255, cv2.THRESH_BINARY)
        contours, hier = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        if len(contours) == 0:
            return [-1.0, -1.0], self.image, None, None
        if len(contours) > 1:
            max_contour = self.get_max_contour(contours)
        else:
            max_contour = contours[0]
        if len(max_contour) == 0:
            return [-1.0, -1.0], self.image, None, None
        max_contour = max_contour.reshape(-1, 2)
        max_contour = self.delete_edges(max_contour, mask)
        #M = cv2.moments(max_contour)
        #mean_point = round(M['m10'] / M['m00'])
        mean_point = self.get_mean_point(max_contour)

        left_side = self.get_left_side(max_contour, mean_point)
        right_side = self.get_right_side(max_contour, mean_point)
        
        kernel = np.ones((40,40), np.uint8)
        dilate = cv2.dilate(self.positive, kernel, iterations = 1)
        
        left_side_new = []
        right_side_new = []
        for item in left_side:
            if dilate[item[1], item[0]] == 0:
                left_side_new.append(item)
        
        for item in right_side:
            if dilate[item[1], item[0]] == 0:
                right_side_new.append(item)
        
        '''
        u_left = list(map(int, left_side[:,0] * k1))
        v_left = list(map(int,left_side[:,1] * k2))
        u_right = list(map(int,right_side[:,0] * k1))
        v_right = list(map(int,right_side[:,1] * k2))
        '''
        #left_side = np.array(left_side_new).reshape(-1,2)
        #right_side = np.array(right_side_new).reshape(-1,2)
        
        u_left = left_side[:,0]
        v_left = left_side[:,1]
        
        u_right = right_side[:,0]
        v_right = right_side[:,1]
        #print (v_left)
        #print ("V_LEFT",v_left)
        Z_left = self.depth[v_left,u_left] 
        Z_right = self.depth[v_right,u_right]

        X_left,Y_left,_,dist_left = self.get_xyz(np.array(u_left),np.array(v_left),Z_left)
        
        #print ("DIST_LEFT",dist_left)

        X_right,Y_right,_,dist_right = self.get_xyz(np.array(u_right),np.array(v_right),Z_right)

        dist_left = Z_left
        dist_right = Z_right
       
        if len(dist_left) == 0:
            dist_left = -1.0

        else:
            idx_left, dist_left = np.argmin(dist_left), np.min(dist_left)
            u_left, v_left = left_side[idx_left][0],left_side[idx_left][1]
                
        if len(dist_right) == 0:
            dist_right = -1.0

        else:
            idx_right, dist_right = np.argmin(dist_right), np.min(dist_right)
            u_right, v_right = right_side[idx_right][0],right_side[idx_right][1]
                

        #print ("DIST_right",dist_right)

        #u_left, v_left = left_side[idx_left][0],left_side[idx_left][1]
        #u_right, v_right = right_side[idx_right][0],right_side[idx_right][1]
        image = self.image.copy()

        max_contour = max_contour.reshape(-1, 1, 2)

        #image = cv2.drawContours(image, max_contour, -1, (0,255,255), 3)
        for item in left_side:
            image = cv2.circle(image, (item[0],item[1]), 2, (255,0,0), 2)
        
        for item in right_side:
            image = cv2.circle(image, (item[0],item[1]), 2, (0,255,0), 2)
        image = cv2.circle(image, (mean_point,mask.shape[0] - 1),radius=20, color=(0, 0, 255), thickness=-1)

        
        image = cv2.putText(image, f'Left distance:{round(dist_left,3)} m', (50,50), cv2.FONT_HERSHEY_SIMPLEX,  
                    1, (0, 0, 255), 2, cv2.LINE_AA)
        if dist_left != -1.0:
            image = cv2.circle(image, (u_left, v_left), radius=10, color=(255, 0, 255), thickness=-1)
            # image = cv2.putText(image, f'X:{round(X_left[idx_left],3)} m', (50,100), cv2.FONT_HERSHEY_SIMPLEX,  
            #             1, (0, 0, 255), 2, cv2.LINE_AA)
            # image = cv2.putText(image, f'Y:{round(Y_left[idx_left],3)} m', (50,150), cv2.FONT_HERSHEY_SIMPLEX,  
            #                 1, (0, 0, 255), 2, cv2.LINE_AA)
            image = cv2.putText(image, f'Z:{round(Z_left[idx_left],3)} m', (50,200), cv2.FONT_HERSHEY_SIMPLEX,  
                            1, (0, 0, 255), 2, cv2.LINE_AA)
        


        image = cv2.putText(image, f'Right distance:{round(dist_right,3)} m', (900,50), cv2.FONT_HERSHEY_SIMPLEX,  
                        1, (0, 0, 255), 2, cv2.LINE_AA)
        if dist_right != -1.0:
            image = cv2.circle(image, (u_right, v_right), radius=10, color=(255, 0, 255), thickness=-1)
            # image = cv2.putText(image, f'X:{round(X_right[idx_right],3)} m', (900,100), cv2.FONT_HERSHEY_SIMPLEX,  
            #                 1, (0, 0, 255), 2, cv2.LINE_AA)
            # image = cv2.putText(image, f'Y:{round(Y_right[idx_right],3)} m', (900,150), cv2.FONT_HERSHEY_SIMPLEX,  
            #                 1, (0, 0, 255), 2, cv2.LINE_AA)
            image = cv2.putText(image, f'Z:{round(Z_right[idx_right],3)} m', (900,200), cv2.FONT_HERSHEY_SIMPLEX,  
                            1, (0, 0, 255), 2, cv2.LINE_AA)
        edges2d_msg = Edges2d()
        edges2d_msg.header = self.header
        edges2d_msg.left_side = self.get_coords2d_msg(left_side[:,0], left_side[:,1])
        edges2d_msg.right_side = self.get_coords2d_msg(right_side[:,0], right_side[:,1])

        edges3d_msg = Edges3d()
        edges3d_msg.left_side = self.get_coords3d_msg(X_left, Y_left, Z_left)
        edges3d_msg.right_side = self.get_coords3d_msg(X_right, Y_right, Z_right)
        
        return [np.asarray(dist_left).item(), np.asarray(dist_right).item()], image, edges2d_msg, edges3d_msg

    def get_coords2d_msg(self, x, y):
        msg = Coords2d()
        msg.header = self.header
        msg.x = [int(a) for a in x]
        msg.y = [int(a) for a in y]
        return msg

    def get_coords3d_msg(self, x, y, z):
        msg = Coords3d()

        msg.x = [float(a) for a in x]
        msg.y = [float(a) for a in y]
        msg.z = [float(a) for a in z]
        return msg
    
    def get_empty_coords2d_msg(self):
        msg = Coords2d()
        msg.x = [-1]
        msg.y = [-1]
        return msg
    
    def get_empty_coords3d_msg(self):
        msg = Coords3d()
        msg.x = [-1]
        msg.y = [-1]
        msg.z = [-1]
        return msg