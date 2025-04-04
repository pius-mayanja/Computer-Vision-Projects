import numpy as np
import cv2


def get_limits(color): # color is the array of values [BGR]
    
    color_arr = np.uint8([[color]])             # Forms a 2D array which creates a 1X1 image using the provided pixels
                                                # unit8 coverts values into 8-bit unsigned integers that OpenCV understands
    hsv_image = cv2.cvtColor(color_arr, cv2.COLOR_BGR2HSV)      #converts the 1x1 BGR Image into a HSV image
    
    hue = hsv_image[0][0][0]
    
    if hue >= 165:
        lower_limit = np.array([hue-10, 100, 100], dtype= np.uint8)
        upper_limit = np.array([180, 255, 255])
    
    elif hue <= 15:
        lower_limit = np.array([0, 100, 100], dtype=np.uint8)
        upper_limit = np.array([hue+10, 255, 255])
    
    else:
        lower_limit = np.array([hue-10, 100, 100], dtype=np.uint8)
        upper_limit = np.array([hue+10, 255,255], dtype=np.uint8)
    
    return lower_limit, upper_limit

