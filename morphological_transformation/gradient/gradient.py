import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    GRADIENT = DIFFERENCE BETWEEN DILATION AND EROSION
                OF THE IMAGE
"""


"""
    This function read an image
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)



def gradient(img):
    kernel = np.ones((5,5),np.uint8)
    result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    plt.subplot(1,2,1), plt.imshow(img, cmap="gray"), plt.title("Real Image")
    plt.subplot(1,2,2), plt.imshow(result, cmap="gray"), plt.title("Gradient Image")
    plt.show()


if __name__ == "__main__":
    img = readi("../../assets/images/letterA.jpg", "gray")
    gradient(img)


