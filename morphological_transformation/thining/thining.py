import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.morphology import binary_hit_or_miss
from  scipy import ndimage


"""
    THINING = IMAGE - (IMAGE DILATE STRUCTURAL ELEMENT)
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)

def get_structure(name="rectangular"):
    # Rectangular Kernel
    if name == "rectangular":
        return cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    if name == "elliptical":
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    if name == "cross-shaped":
        return cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    print ("write a valid name\n")


def thining(img):
    s1 = get_structure("rectangular")
    result1 = ndimage.binary_hit_or_miss(img, structure1=s1).astype(np.int)
    dimx,dimy  = result1.shape[0], result1.shape[1]

    thin = np.zeros((dimx,dimy), np.uint8) 

    for x in range(dimx):
        for y in range(dimy):
            thin[x,y] = img[x,y] - thin[x,y]

    plt.subplot(1,3,1), plt.imshow(img, cmap="gray"), plt.title("Real Image")
    plt.subplot(1,3,2), plt.imshow(result1, cmap="gray"), plt.title("Hit_or_miss Image")
    plt.subplot(1,3,3), plt.imshow(thin, cmap="gray"), plt.title("Adelgazamiento Image")

    plt.show()


if __name__ == "__main__":
    img = readi("../../assets/images/letterA.jpg", "gray")
    thining(img)


