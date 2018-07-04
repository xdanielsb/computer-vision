"""
    Tracking over images, this project
    track and object in movement
"""

import cv2

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def threshold_bin(img, THRESH_VALUE):
    return cv2.threshold(img,THRESH_VALUE,255,cv2.THRESH_BINARY)

def blur_(img):
    return cv2.blur(img,(5,5))


#find intersection
#https://stackoverflow.com/questions/8552364/opencv-detect-contours-intersection
