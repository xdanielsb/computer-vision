from matplotlib import pyplot as plt
import cv2
"""
    Script for equalize a histogram
"""


"""
    This function read an image
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)



def equalize(img):
    dimy, dimx = img.shape[1], img.shape[0]
    equ = cv2.equalizeHist(img)
    

    plt.subplot(2,2,1), plt.imshow(img, cmap=plt.cm.gray), plt.title('Imagen Original')
    plt.subplot(2,2,2), plt.imshow(equ, cmap=plt.cm.gray), plt.title('Imagen Equalizada')
    plt.subplot(2,2,3), plt.hist(img.ravel(),128,[0,256])
    plt.subplot(2,2,4), plt.hist(equ.ravel(),128,[0,256])
    
    plt.show()


if __name__ == "__main__":
    img = readi("../assets/images/smile.png", "gray")
    equalize(img)
