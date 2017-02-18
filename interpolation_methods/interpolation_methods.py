import cv2
import numpy as np
from bicubic import *
from bilinear import *
from methods import *
from knn import *
import time #Use for measure the time



def test_bicubic(img, factor):
    img_e_1 = enlarge(img, factor)
    dimx, dimy = img_e_1.shape[0], img_e_1.shape[1] 
    for x in range(1, dimx):
        for y in range (1, dimy):
            img_e_1[x][y] = get_bicubic_pixel(img, x,y)
    cv2.imshow('Cubic',img_e_1)


def test_bilinear(img, factor):
    img_e_3 = enlarge(img, factor)
    dimx, dimy = img_e_3.shape[0], img_e_3.shape[1] 
    for x in range(1, dimx):
        for y in range (1, dimy):
            img_e_3[x][y] = getBilinearPixel(img, x,y)
    cv2.imshow('Bilinear',img_e_3)


def test_nearest_neighbors(img, factor):
    img_e_2 = enlarge(img, factor)
    dimx, dimy = img_e_2.shape[0], img_e_2.shape[1] 
    for x in range(1, dimx):
        for y in range (1, dimy):
            img_e_2[x][y] = get_near_neighbor_pixel(img, x,y)
    cv2.imshow('Nearest Neighbor',img_e_2)




if (__name__== "__main__"):

    img = cv2.imread("../assets/images/smile.png", 0)
    if (img == None):
        print("Oppss, the image was nos loaded.")
    else:
        cv2.imshow('Real Image',img)
        
        start_time = time.time()
        #factor 
        factor = 1.6

        #test_bicubic(img, factor)
        #test_bilinear(img, factor)
        #test_nearest_neighbors(img, factor)

        print("---  The running time in seconds was: %s " % (time.time() - start_time))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

