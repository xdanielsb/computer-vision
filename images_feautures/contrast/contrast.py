import cv2
import math as m

"""
    Script for calc the contrast of an image
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


def contrast(img, bright):
    dimy, dimx = img.shape[1], img.shape[0]
    cont = 0
    for x in range(dimx):
        for y in range(dimy):
            cont += (img[x,y] - bright) ** 2  
    
    return m.sqrt(cont/(dimx*dimy))

if __name__ == "__main__":
    img = readi("../../assets/images/smile.png", "gray")
    
    co= contrast(img,brightness(img))
    print("The contrast is %d"%co )

