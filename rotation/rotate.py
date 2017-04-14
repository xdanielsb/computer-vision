import math as m
import cv2
import numpy as np


"""
    t ---> angle in degrees
"""
def rotate(x,y,t):
    t = m.radians(t)
    mat = [ [m.cos(t), -m.sin(t)], 
            [m.sin(t), m.cos(t)] ]

    vect = [x,y]

    result = np.dot(mat, vect)
    return int(result[0]), int(result[1])

"""
    Structure of a matrix
    (0,0) (0,1) (0,2)
    (1,0) (1,1) (1,2)
    (2,0) (2,1) (2,2)
"""

def rotation(img, angle):
    dimy, dimx = len(img), len(img[0])
    h = m.hypot(dimx,dimy)
    img_rot = np.zeros(shape=(h +1 , h +1), dtype=np.uint8)

    xmin, ymin  = 0, 0
    
    for x in range(0, dimx):
        for y in range(0, dimy):
            vector = rotate(x, y, 90 - angle)
            if (dimy + int(vector[1])) > xmin:
                xmin = dimy + int(vector[1])
            if (dimx - int(vector[0])) > ymin:
                ymin = dimx - int(vector[0])
                
    
    for x in range(0, dimx):
        for y in range(0, dimy):
            vector = rotate(x, y, 90 - angle)
            img_rot[dimx - int(vector[0]) - ymin][dimy + int(vector[1]) - xmin] = img[y][x]
    

    return img_rot

if (__name__=="__main__"):
    img = cv2.imread("../assets/images/hand.jpg",0)
    angle = 72
    img_rotate = rotation(img, angle)
    cv2.imshow("Real Image", img)
    cv2.imshow("Rotate Image", img_rotate)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()



