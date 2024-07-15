import cv2
import os
import numpy as np

num_classes = 3

categories = {
    1: {'name': 'negative', "color" : np.array([0, 0, 128])},
    2 : {'name': 'positive', "color" : np.array([0, 128, 0])},
    3 : {'name': 'road', "color" : np.array([128, 0, 0])},
}

def draw_masks(img, masks):
    # img = cv2.imread(imfile)
    # h, w, _ = img.shape
    # print(masks["cats"])

    for m, c in zip(masks["masks"], masks["cats"]):
        if c!=0:
            color = categories[c]["color"]
            # print(img.shape)
            # print(m.shape)
            img[m == 1] = 0.5 * img[m == 1] + 0.5 * color
        #     if c in [1,2,3,4,5]:
                # contours, _ = cv2.findContours((m * 255).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # img = cv2.drawContours(img.copy(), contours, -1, color.tolist(), int(max(1, (min(h, w) / 200))))
        
    return img

def create_binary_masks(semantic_mask):
    unique_categories = np.unique(semantic_mask)
    binary_masks = []
    cats = []

#     semantic_mask[semantic_mask == 10] = 255
#     semantic_mask[semantic_mask == 11] = 255
#     semantic_mask[semantic_mask == 12] = 255

    # cv2.imwrite('test.png', semantic_mask)

    for category in unique_categories:
        binary_mask = (semantic_mask == category).astype(np.uint8)
        binary_masks.append(binary_mask)
        cats.append(category)

    return {'masks': binary_masks, 'cats':cats}

def change_mask(mask, num_classes):
    if num_classes==10:
        mask = np.where((mask==5) | (mask==6) | (mask==7) | (mask==8), 0, mask)
        mask = np.where((mask < 5) & (mask>0), 2, mask) #positive
        mask = np.where((mask==9), 3, mask) #road
    elif num_classes==2:
        mask = np.where((mask==255), 3, mask) #road
    return mask

def visualize(mask, image):
    # mask = change_mask(mask, num_classes)
    #     print(mask)
    #     break
    # cv2.imwrite(os.path.join(mask_dir, name), mask)

    # output_file = os.path.join(visual_dir,name+'.png')
    # print(mask_file)
    # img_path = os.path.join(image_dir, name+'.jpg')
    binary_masks = create_binary_masks(mask)
    visual = draw_masks(image, binary_masks)
    # cv2.imwrite(output_file, visual)
    # check = cv2.imread(output_file)
    return visual
