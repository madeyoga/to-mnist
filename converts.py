import os
import cv2
import numpy as np
from natsort import natsorted

path = 'G:\\Kuliah\\skripsi\\Project\\RLSA\\segmented_number\\' # "numbers/"

list_of_files = os.listdir(path)
list_of_files = natsorted(list_of_files)

for i, file in enumerate(list_of_files):
    image_file_name = path+file
    print(image_file_name)
    if ".png" in image_file_name:
        img = cv2.imread(image_file_name, cv2.IMREAD_GRAYSCALE)
        dimension = (16, 16)
        img = cv2.resize(img, dimension, 0, 0, interpolation=cv2.INTER_AREA)
##        img = img[0:13]
##        img = cv2.resize(img, dimension, 0, 0, interpolation=cv2.INTER_AREA)
        (thresh, img) = cv2.threshold(img,
                                      128,
                                      255,
                                      cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img = 255-img
        file = "resized/mnist" + str(i) + ".png"
        blank_image = np.zeros(shape=[28, 28], dtype=np.uint8)
        blank_image[7:23, 7:23] = img
        blank_image = blank_image.reshape(28, 28)
        cv2.imwrite(file, blank_image)
