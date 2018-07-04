import cv2
from matplotlib import pyplot as plt

"""
    This function read an image
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)


def add(img2 , img1):
  
    dimx, dimy = img1.shape[0], img1.shape[1]
    #resize the image
    img3 = cv2.resize(img2, (dimy,dimx))

    #cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
    #Awesome sum img5 = img1*0.2 + img3*0.3 + 0
    img5 = cv2.addWeighted(img1, 0.2, img3, 0.3,0)

    #Normal sum
    img4 = cv2.add(img1,img3)

    plt.subplot(2,2,1), plt.imshow(img1, cmap="gray"), plt.title("Img 1")
    plt.subplot(2,2,2), plt.imshow(img2, cmap="gray"), plt.title("Img 2")
    plt.subplot(2,2,3), plt.imshow(img4, cmap="gray"), plt.title("Img 4")
    plt.subplot(2,2,4), plt.imshow(img5, cmap="gray"), plt.title("Img 5")

    plt.show()


if __name__ == "__main__":
    img1 = readi ("../assets/images/hand_1.png", "gray")
    img2 = readi ("../assets/images/smile.jpg", "gray")
    add(img1, img2)
    
