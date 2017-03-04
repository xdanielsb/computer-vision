import cv2
"""
    Script for calc the brightness of an image
"""


"""
    This function read an image
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)


def brightness(img):
    dimy, dimx = img.shape[1], img.shape[0]
    bright = 0
    for i in range(dimx):
        for j in range(dimy):
            bright  +=  img[i,j]
    return bright/(dimx*dimy)


if __name__ == "__main__":
    img = readi("../assets/images/smile.png", "gray")
    print ("The brightness is :%d " %brightness(img))

