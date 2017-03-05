import cv2
from matplotlib import pyplot as plt
import numpy as np
"""
    Reference http://felix.abecassis.me/2011/09/opencv-morphological-skeleton/
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)

def get_structure(name="rectangular"):
    # Rectangular Kernel
    if name == "rectangular":
        return cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    if name == "elliptical":
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    if name == "cross-shaped":
        return cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    print ("write a valid name\n")

def skeleton(img,iters=1, invertir_color=False):
    s1 = get_structure("cross-shaped")

    img2 = img
    temp = np.zeros((img.shape[0], img.shape[1]), np.uint8) 
    skel = np.zeros((img.shape[0], img.shape[1]), np.uint8) 


    for i in range(iters):

        eroded = cv2.erode(img, s1, iterations  = 1)
        temp   = cv2.dilate(eroded, s1, iterations  = 1)
        temp   = cv2.subtract(img, temp);
        skel   = cv2.bitwise_or(skel, temp);
        
        img = eroded
        
    if(invertir_color):
        ret,img2 = cv2.threshold(img2,200,255,cv2.THRESH_BINARY_INV)
        ret,skel = cv2.threshold(skel,200,255,cv2.THRESH_BINARY_INV)
    
    plt.subplot(1,2,1), plt.imshow(img2, cmap="gray"), plt.title("Real Image")
    plt.subplot(1,2,2), plt.imshow(skel, cmap="gray"), plt.title("Skeleton")

    plt.show()

if __name__ == "__main__":
    img = readi("../../assets/images/silouete.png", "gray")
    invertir_color = True   #Cuando el fondo es negro lo aplicamos
    iters = 500
    if (invertir_color):
        ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
        skeleton(thresh1,iters, invertir_color)
    else: 
        ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
        skeleton(thresh1,iters, invertir_color)

    

