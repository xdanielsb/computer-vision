import cv2
import numpy as np
from matplotlib import pyplot as plt


def conv(img, kernel):
    dst = cv2.filter2D(img,-1,kernel)
    return dst


def prewit(img):
    N = np.matrix([[-1 ,-1 , -1], [1 ,-2 , 1], [1 , 1 ,1 ]], np.float32)
    S = np.matrix([[1 ,1 , 1], [1 ,-2 , 1], [-1 , -1 ,-1 ]], np.float32)
    E = np.matrix([[1 ,1 , -1], [1 ,-2 , -1], [1 , 1 ,-1 ]], np.float32)
    O = np.matrix([[-1 ,1 , 1], [-1 ,-2 , 1], [-1 , 1 ,1 ]], np.float32)
    SO = np.matrix([[1 ,1 , 1], [-1 ,-2 , 1], [-1 , -1 ,1 ]], np.float32)
    NO = np.matrix([[-1 ,-1 , 1], [-1 ,-2 , 1], [1 , 1 ,1 ]], np.float32)
    SE = np.matrix([[1 ,1 , 1], [1 ,-2 , -1], [1 , -1 ,-1 ]], np.float32)
    NE = np.matrix([[1 ,-1 , -1], [1 ,-2 , -1], [1 , 1 ,1 ]], np.float32)

    #Kernels
    ms = [N,S,E,O,SO,NO,SE,NE]
    



    img2 = conv(img, N)
    plt.subplot(3,3,2)
    plt.imshow(img2)
    plt.title('Conv with N')

    img3 = conv(img, S)
    plt.subplot(3,3,3)
    plt.imshow(img3)
    plt.title('Conv with S')

    img4 = conv(img, E)
    plt.subplot(3,3,4)
    plt.imshow(img4)
    plt.title('Conv with E')

    img5 = conv(img, O)
    plt.subplot(3,3,5)
    plt.imshow(img5)
    plt.title('Conv with O')

    img6 = conv(img, SO)
    plt.subplot(3,3,6)
    plt.imshow(img6)
    plt.title('Conv with SO')

    img7 = conv(img, NO)
    plt.subplot(3,3,7)
    plt.imshow(img7)
    plt.title('Conv with NO')

    img8 = conv(img, SE)
    plt.subplot(3,3,8)
    plt.imshow(img8)
    plt.title('Conv with SE')

    img9 = conv(img, NE)
    plt.subplot(3,3,9)
    plt.imshow(img9)
    plt.title('Conv with NE')


    convs = [img2, img3, img4 , img5, img6, img7, img8, img9]


    dimx, dimy = len(img2), len(img[0])
    result = np.zeros(shape=(dimx,dimy), dtype=np.uint8)

    for x in range(0,dimx):
        for y in range(0,dimy):
            result[x][y] = max(img2[x][y], img3[x][y], img4[x][y], img5[x][y], \
                               img6[x][y], img7[x][y], img8[x][y], img9[x][y])
                            

    #plt.show()
    cv2.imshow("Result", result)
    cv2.imshow("Real Image", img)
    #print(img9)
    


if (__name__ == "__main__"):

    #Read the image in gray scale   
    img = cv2.imread("../assets/images/smile.jpg", 0)
   # cv2.imshow("Title",img)
    prewit(img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

