import os
import cv2
import numpy as np
from natsort import natsorted

##Image:
##current_width 
##current_height
##
##Converts to new_height = 113
##
##new_width = current_width * (new_height / current_height)
##
##size = (new_width, 113)

path = 'G:\\Kuliah\\skripsi\\Project\\RLSA\\segmented_number\\'

list_of_files = os.listdir(path)
list_of_files = natsorted(list_of_files)

mnist_x = 28
mnist_y = 28
center_x, center_y = int(mnist_x/2), int(mnist_y/2)

for i, file in enumerate(list_of_files):
    image_file_name = path + file
    if ".png" in image_file_name:
        img = cv2.imread(image_file_name, cv2.IMREAD_GRAYSCALE)
        
        # Aspect Ratio
        current_height = img.shape[0]
        current_width = img.shape[1]
        
        new_height = 20
        new_width = int(current_width * (new_height / current_height))

        dimension = (new_width, new_height)
        
        img = cv2.resize(img, dimension, 0, 0, interpolation=cv2.INTER_AREA)
        
        (thresh, img) = cv2.threshold(img,
                                      128,
                                      255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img = 255-img
        file = "resize_with_aspect_ratio/number" + str(i) + ".png"
        blank_image = np.zeros(shape=[28, 28], dtype=np.uint8)

        # Calculate offset
        start_x = center_x - int(0.5 * new_width)
        start_y = center_y - int(0.5 * new_height)

        # Place center
        blank_image[start_y:start_y+new_height, start_x:start_x+new_width] = img
        blank_image = blank_image.reshape(28, 28)
        cv2.imwrite(file, blank_image)
