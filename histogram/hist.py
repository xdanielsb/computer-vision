import cv2
import numpy as np
from matplotlib import pyplot as plt



if(__name__=="__main__"):
    img = cv2.imread('../assets/images/hand_1.jpg',  1)
    plt.figure(1)
    
    plt.hist(img.ravel(),256,[0,256]); 

    plt.figure(2)

    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
