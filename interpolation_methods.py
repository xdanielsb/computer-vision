import cv2
import numpy as np
from functools import reduce



def enlarge(img, factor):
    dimy, dimx = int(len(img) * factor), int(len(img[0]) *factor)
    return np.zeros(shape=(dimy,dimx ), dtype=np.uint8)



"""
Neighbors
-1,-1	0,-1	1,-1
-1,0	0,0	1,0
-1,1	0,1	1,1
"""
def getBilinearPixel(img, x,y):
    dimy, dimx = img.shape[1] -1, img.shape[0] -1

    #Cuantizar
    x = (x // factor) % dimx
    y = (y // factor) % dimy

    #Expresion of the neighbors
    directions = [ [-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1], [1,-1], [-1,1]]
    
    suma = 0
    for d in directions:
        ##Check all the borders
        suma += int(img[x+d[0]][y+d[1]])

    return suma // len(directions);


"""
Neighbors
-1,-1	0,-1	1,-1
-1,0	0,0	1,0
-1,1	0,1	1,1

"""

def get_near_neighbor_pixel(img, x,y):
    dimy, dimx = img.shape[1] -1, img.shape[0] -1

    #Cuantizar
    x = (x // factor) % dimx
    y = (y // factor) % dimy

    #Expresion of the neighbors
    directions = [ [-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1], [1,-1], [-1,1]]
    
    vecinos = []
    for d in directions:
        ##Check all the borders
        vecinos.append(img[x+d[0]][y+d[1]])
    
    #Criteria, select the bigger
    return vecinos[-1];


"""
Data neighbors
-2,-2	-1,-2	0,-2	1,-2	2,-2
-2,-1	-1,-1	0,-1	1,-1	2,-1
-2,0	-1,0	0,0	1,0	2,0
-2,1	-1,1	0,1	1,1	2,1
-2,2	-1,2	0,2	1,2	2,2
"""
def get_bicubic_pixel(img, x, y):
    dimy, dimx = img.shape[1] -2, img.shape[0] -2

    #Cuantizar
    x = (x // factor) % dimx
    y = (y // factor) % dimy

    #Expresion of the neighbors
    #First neihbors
    directions = [ [-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1], [1,-1], [-1,1]]
    directions.extend([[-2,2], [-2,-1],[-2,0],[-2,1],[-2,2],[-1,-2],[0,-2],[1,-2],[2,-2],[2,-1],[2,0],[2,1],[2,2],[-1,2],[0,2],[1,2]])
    suma = 0
    for d in directions:
        ##Check all the borders
        suma += int(img[x+d[0]][y+d[1]])

    return suma // len(directions);

    
if (__name__== "__main__"):

    img = cv2.imread("../images/smile.png", 0)
    print(img.shape[0], img.shape[1])    
    #factor 
    factor = 1.6

    #enlarged image
    img_e_1 = enlarge(img, factor)
    img_e_2 = enlarge(img, factor)
    img_e_3 = enlarge(img, factor)
    
    dimx, dimy = img_e_1.shape[0], img_e_1.shape[1] 
    
    
    
    for x in range(1, dimx):
        for y in range (1, dimy):
            img_e_1[x][y] = get_bicubic_pixel(img, x,y)

    for x in range(1, dimx):
        for y in range (1, dimy):
            img_e_2[x][y] = get_near_neighbor_pixel(img, x,y)

    for x in range(1, dimx):
        for y in range (1, dimy):
            img_e_3[x][y] = getBilinearPixel(img, x,y)

    cv2.imshow('image real',img)
    cv2.imshow('Cubic',img_e_1)
    cv2.imshow('Nearest Neighbor',img_e_2)
    cv2.imshow('Bilinear',img_e_3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
