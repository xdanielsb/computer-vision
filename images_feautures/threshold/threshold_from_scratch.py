import cv2
import math as m
import numpy as np
from matplotlib import pyplot as plt

"""
    Script for calc the brightness of an image
"""

CONSTANT = 128
"""
    This function read an image
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)



def threshold(img):
    dimx, dimy = img.shape[0], img.shape[1]
    img_umbr = np.zeros((dimx, dimy), np.uint8) #imagen umbralizada
    img_inv = np.zeros((dimx, dimy), np.uint8) #imagen invertida
    img_max = np.zeros((dimx, dimy), np.uint8) #Imagen de maximos entre la original y la umbralizada 
    img_and_umbr_inv = np.zeros((dimx, dimy), np.uint8) #Imagen result of and between img_umbr y img_inv
    img2  = np.zeros((dimx, dimy), np.uint8)

    for x in range(dimx):
        for y in range(dimy):
           val = img[x,y]
           img_umbr[x,y] = 255 if val > CONSTANT else 0
           img_inv[x,y] = 255  - val
           img_max[x,y] = max(img[x,y], img_umbr[x,y])
           img_and_umbr_inv[x,y] = max(img_inv[x,y], img_umbr[x,y]) - min (img_inv[x,y],img_umbr[x,y])
           img2[x,y] = min(img_inv[x,y],img[x,y])
           


    plt.subplot(331), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.subplot(332), plt.imshow(img_umbr, cmap='gray'), plt.title('Img umbralizada')
    plt.subplot(333), plt.imshow(img_inv, cmap='gray'), plt.title('Img Invertida')
    plt.subplot(334), plt.imshow(img_max, cmap='gray'), plt.title('Img MAX(ORI, UMB')
    plt.subplot(335), plt.imshow(img_and_umbr_inv, cmap='gray'), plt.title('max(inv-umbr)')
    plt.subplot(336), plt.imshow(img2, cmap='gray'), plt.title('img  - inv')

    plt.subplots_adjust(top=0.95, bottom=0.05, left=0.10, right=0.95, hspace=0.25, wspace=0.35)

    plt.show()

if __name__  == "__main__":
    img = readi("../../assets/images/smile.jpg", "gray")
    threshold(img)
