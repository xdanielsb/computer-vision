import cv2
import math as m
import numpy as np

"""
    This function read an image
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)


"""
    Show image for a certain time
    time -> miliseconds
    0 is an execption
"""
def time_show_image(time = 0):
    #0 means, show the image indefenetely until any keypress
    #25 means, show the image for 25 miliseconds
    if time == 0:
        print("\n\tPlease, press any key for finish the program")
    cv2.waitKey(time) 
    
"""
    Close windows and de-allocate memory asociated with it.
"""
def close_windows():
    cv2.destroyAllWindows() 


"""
    Rotate an image
"""

def rotate(img, angle):
    rows,cols = img.shape[0], img.shape[1]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst

"""
    Get covariance matrix
"""
def get_covariance(matrix):
    new = []
    for a in matrix:
        new.append(a[0])
    arr = np.array(new)

    #Need process for get the correct format of the matrix

    #print(np.cov(arr.transpose()))
    return np.cov(arr.transpose())


"""
    Find Eigen vectores and Eigen values
"""
def find_eigen(matrix):
    eigen_valor, eigen_vect = np.linalg.eig(matrix)
    return eigen_valor, eigen_vect


def nothing(x):
    pass

    

if __name__ == "__main__":
    #Read the image

    angle_r = 152
    img_real = readi("../assets/images/hand.jpg", "color")
    img_real2 = readi("../assets/images/hand.jpg", "color")
    img = readi("../assets/images/hand.jpg", "gray")
    img_c  = readi("../assets/images/hand.jpg", "gray")
    FIRST = True

    
    img_real = rotate(img_real2, angle_r)
    img = rotate(img_c, angle_r)
    _, thr= cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img_real, contours, 1, (0,255,0), 3)
    
    countour_hand = contours[1]
    cov = get_covariance(countour_hand)

    M = cv2.moments(countour_hand)
    
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    center  = (cx, cy)
    radius = 2
   
    cv2.circle(img_real,center,radius,(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    

    eigen_values, eigen_vect = find_eigen(cov)
    
    x_1 = int(cx + 0.02* float(eigen_vect[0][0] * eigen_values[0]))
    y_1 = int(cy + 0.02*float(eigen_vect[0][1] * eigen_values[0]))
    x_2 = int(cx + 0.02*float(eigen_vect[1][0] * eigen_values[1]))
    y_2 = int(cy + 0.02*float(eigen_vect[1][1] * eigen_values[1]))


    cv2.line(img_real, center, (x_2, y_2), (255,0,0))
    cv2.line(img_real, center, (x_1, y_1), (255,0,0))
    
        
    angle = m.atan2(y_2,x_2)
    angle2 = "%.2f theta" % angle
    cv2.putText(img_real,angle2, center, font,1, (0,0,255), 2)
    
    
    cv2.imshow("Direction image", img_real)
    
    
    time_show_image()
    close_windows()
    

