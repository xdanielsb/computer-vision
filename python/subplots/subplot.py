from read_images import *
from matplotlib import pyplot as plt

def sub(img):
    dimy, dimx = img.shape[1], img.shape[0]


    plt.subplot(2,2,1), plt.imshow(img[0:dimx/2, 0:dimy/2], cmap=plt.cm.gray), plt.title('Imagen')
    plt.subplot(2,2,2), plt.imshow(img[dimx/2:, 0:dimy/2], cmap=plt.cm.gray), plt.title('Imagen')
    plt.subplot(2,2,3), plt.imshow(img[0:dimx/2, dimy/2:], cmap=plt.cm.gray), plt.title('Imagen')
    plt.subplot(2,2,4), plt.imshow(img[dimx/2:, dimy/2:], cmap=plt.cm.gray), plt.title('Imagen')
    
    plt.show()


if __name__ == "__main__":
    
    img = readi("../assets/images/smile.jpg", "gray")
    cv2.imshow("Color Image", img)

    sub(img)

    time_show_image()
    close_windows()
    
