import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    Plot the histogram
    img --> imagen
    fig --> the number of the imagen
"""

"""
    God link
    http://stackoverflow.com/questions/6871201/plot-two-histograms-at-the-same-time-with-matplotlib
"""

def plot (img, fig, name):
    bins = 256
    range_scale = [0,254]

   # plt.figure(fig)
    plt.hist(img.ravel(),bins,range_scale, label=name, alpha=0.5);
    plt.legend(loc='upper right')

"""
    Just the driver of the program
"""

if(__name__=="__main__"):
    name1 = "More Brigth"
    name2 = "Bright"
    name3 = "Less Bright"

    img1 = cv2.imread('../assets/images/hand_1.jpg',  0)
    img2 = cv2.imread('../assets/images/hand_2.jpg',  0)
    img3 = cv2.imread('../assets/images/hand_3.jpg',  0)
    
    plot(img1, 1, name2)
    plot(img2, 2, name1)
    plot(img3, 3, name3)
    
    plt.show()
