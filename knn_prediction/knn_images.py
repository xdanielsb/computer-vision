from __future__ import print_function
import cv2 
import numpy as np


"""
    img1 -> is the image
    factor -> zoom that we want to do by defaul is 1
    return :the enlarged image
"""

def zoom_image(img1, factor=1):
    #Get the size of the images
    dimy, dimx = len(img1), len(img1[0])
    #Create the array to resize the image
    img2 = np.zeros(shape=(dimy * factor +2 ,dimx * factor +2), dtype=np.uint8)
    
    #Iterate over the first image
    for x in range(0, dimx):
        for y in range(0,  dimy):
            #Multiply by the factor
            img2[y*factor+1][x*factor+1] = int(img1[y][x])

    return img2

"""
    img1 -> Real image
    img2 -> Enlarge image so the img with zoom
"""
def knn(img1, img2, f):
    dx1, dx2, dy1, dy2 = len(img1[0]), len(img2[0]), len(img1), len (img2)

    #iterate over the image 1
    for x in range (0, dx1):
        xa = x*f +1
        for y in range(0, dy1):
            ya = y*f +1 
            
            #8 neighbors
            img2[ya-1][xa ] = img2[ya][xa]
            img2[ya-1][xa-1 ] = img2[ya][xa]
            img2[ya-1][xa+1 ] = img2[ya][xa]
            img2[ya+1][xa] = img2[ya][xa]
            img2[ya+1][xa-1] = img2[ya][xa]
            img2[ya+1][xa +1] = img2[ya][xa]
            img2[ya][xa-1] = img2[ya][xa]
            img2[ya][xa+1] = img2[ya][xa]


