import os
import cv2
import numpy as np

##Image:
##current_width 
##current_height
##
##Converts to new_height = 113
##
##new_width = current_width * (new_height / current_height)
##
##size = (new_width, 113)

path = "numbers/"

list_of_files = os.listdir(path)

for i, file in enumerate(list_of_files):
    image_file_name = os.path.join(path, file)
    if ".png" in image_file_name:
        img = cv2.imread(image_file_name, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("original", img)
        
        # Aspect Ratio
        current_height = img.shape[0]
        current_width = img.shape[1]
        
        new_height = 14
        new_width = int(current_width * (new_height / current_height))

        dimension = (new_width, new_height)
        
        img = cv2.resize(img, dimension, 0, 0, interpolation=cv2.INTER_AREA)
        cv2.imshow("resize", img)
        
        (thresh, img) = cv2.threshold(img,
                                      128,
                                      255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img = 255-img
        file = "resized2/number" + str(i) + ".png"
        blank_image = np.zeros(shape=[28, 28], dtype=np.uint8)
        blank_image[7:21, 7:7+dimension[0]] = img
        blank_image = blank_image.reshape(28, 28)
        cv2.imwrite(file, blank_image)
