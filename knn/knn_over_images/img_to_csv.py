from __future__ import print_function
import cv2


img = cv2.imread("data.png")
dimy = len(img)
dimx = len(img[0])

for y in range(0,dimy):
    for x in range(0,dimx):
        print ("{},{}".format(x,y),end="")
        for val in img[y][x]:
            print(","+str(val), end="")
        print()
    
