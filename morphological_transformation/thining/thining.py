from __future__ import print_function
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.morphology import binary_hit_or_miss
from  scipy import ndimage


"""
    THINING = IMAGE - (IMAGE HIT OR MISS STRUCTURAL ELEMENT)
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)


def print_img(img):
    for y in img:
        for x in y:
            print (x, end ="")
        print()

def thining(img):
    ss = []
    s = np.array([ [1,1], [1,1]], 'uint8')
    
    plt.subplot(1,2,1), plt.imshow(img, cmap="gray"), plt.title(str(2))
    for i in range(12):
        img = ndimage.binary_hit_or_miss(img, structure1=s).astype(np.uint8)

    plt.subplot(1,2,2), plt.imshow(img, cmap="gray"), plt.title(str(2))
    plt.show()


if __name__ == "__main__":


   
    img = readi("../../assets/images/hand.jpg", "gray")
    ret,img_bin = cv2.threshold(img,50,255, cv2.THRESH_BINARY_INV)
    #print_img(img_bin)"""
    
    thining(img_bin)


