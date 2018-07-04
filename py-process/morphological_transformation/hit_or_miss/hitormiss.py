from scipy.ndimage.morphology import binary_hit_or_miss
from  scipy import ndimage
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    Basic operation for detecting shapes
"""

def get_structure(name="rectangular"):
    # Rectangular Kernel
    if name == "rectangular":
        print("1")
        return cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    if name == "elliptical":
        print("2")
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    if name == "cross-shaped":
        print("3")
        return cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    print ("write a valid name\n")

"""
    HIT OR MISS
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)

def hm(img):
    s1 = get_structure("rectangular")
    s2 = get_structure("elliptical")
    s3 = get_structure("cross-shaped")
    result1 = ndimage.binary_hit_or_miss(img, structure1=s1).astype(np.int)
    result2 = ndimage.binary_hit_or_miss(img, structure1=s2).astype(np.int)
    result3 = ndimage.binary_hit_or_miss(img, structure1=s3).astype(np.int)
    plt.subplot(2,2,1), plt.imshow(img, cmap="gray"), plt.title("Real Image")
    plt.subplot(2,2,2), plt.imshow(result1, cmap="gray"), plt.title("rectangular kernel")
    plt.subplot(2,2,3), plt.imshow(result2, cmap="gray"), plt.title("elliptical kernel")
    plt.subplot(2,2,4), plt.imshow(result3, cmap="gray"), plt.title("cross-shaped kernel")
    plt.show()
    
if __name__ == "__main__":
    img = readi("../../assets/images/letterA.jpg", "gray")
    hm(img)


