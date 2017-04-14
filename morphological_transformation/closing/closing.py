import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    CLOSSING =  DILATE  FOLLOWED BY EROSION
    USEFUL WHEN YOU NEED TO REMOVE BLACK NOISE
"""


"""
    This function read an image
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)


def closing(img):
    kernel = np.ones((5,5),np.uint8)
    result = img
    result = cv2.morphologyEx(result, cv2.MORPH_CLOSE, kernel)
    plt.subplot(1,2,1), plt.imshow(img, cmap="gray"), plt.title("Real Image")
    plt.subplot(1,2,2), plt.imshow(result, cmap="gray"), plt.title("Closed Image =)")
    plt.show()


if __name__ == "__main__":
    img = readi("../../assets/images/black_noise.jpg", "gray")
    closing(img)

