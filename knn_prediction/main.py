from knn_images import *

if (__name__ =="__main__"):
    
    factor = 2 ## x2 the image
    img1 = cv2.imread("../datasets/smile.jpg", 0)
    img2 = zoom_image(img1,factor)
    knn(img1, img2, factor)

    cv2.imshow('image',img1)
    cv2.imshow('image2',img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

