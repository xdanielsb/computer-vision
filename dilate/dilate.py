import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    This script helps to find if there in difference between a kernel  of ones 3x3 and 5x5.
"""

if (__name__ =="__main__"):

    #Loading the image
    img1  = cv2.imread("smile.png",0)
    
    #todo lo que este abajo de 127  llevelo a 0 
    #todo lo que este arriba de 127  llevelo a 1
    #255 a donde lo queremos mandar
    h, img = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)

    
    kernel = np.ones((5,5), np.uint8)
    dilatation1 = cv2.dilate(img, kernel, iterations =1)

    kernel = np.ones((3,3), np.uint8)
    dilatation2 = cv2.dilate(img, kernel, iterations =2)

    #plt.figure(1)
    

    plt.subplot(1,3,1)
    plt.imshow(dilatation1, cmap="gray")

    plt.subplot(1,3,2)
    plt.imshow(dilatation2, cmap="gray")

    solucion  = dilatation1- dilatation2
    
    print ("The max number in the array is: {} ".format(solucion.max()))
    plt.subplot(1,3,3)
    plt.imshow(solucion, cmap="gray")

    plt.show()


