import cv2 # OpenCV for perspective transform
import numpy as np
import scipy.misc # For saving images as needed
import glob  # For reading in a list of images from a folder

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#---------------------
path = './IMG/*.jpg'
import matplotlib.pyplot as plt
img_list = glob.glob(path) # list of all images in the path
image = mpimg.imread(img_list[0]) #gets the first image

plt.imshow(image)
