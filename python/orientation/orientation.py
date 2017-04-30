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


if __name__ == "__main__":
    #Read the image
    img_real = readi("../assets/images/hand.jpg", "color")
    img = readi("../assets/images/hand.jpg", "gray")
    ##cv2.imshow("Color Image", img)

    #Now threshold the image
    _, thr= cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ##cv2.imshow("Threshold Image", thr)

    #Now find countours
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Draw contours in the image
    #1 means draw the countour 1
    cv2.drawContours(img_real, contours, 1, (0,255,0), 3)
    ##cv2.imshow("Contours image", img_real)

    countour_hand = contours[1]
    cov = get_covariance(countour_hand)

    #Moments of the image 
    M = cv2.moments(countour_hand)
    #Centroid of the image
    
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    center  = (cx, cy)
    radius = 2
    #Draw a point in the mass center
    cv2.circle(img_real,center,radius,(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    



    #Now draw the lines 
    
    eigen_values, eigen_vect = find_eigen(cov)
    
    x_1 = int(cx + 0.02* float(eigen_vect[0][0] * eigen_values[0]))
    y_1 = int(cy + 0.02*float(eigen_vect[0][1] * eigen_values[0]))
    x_2 = int(cx + 0.02*float(eigen_vect[1][0] * eigen_values[1]))
    y_2 = int(cy + 0.02*float(eigen_vect[1][1] * eigen_values[1]))

    
    print(x_1, y_1)
    print(x_2, y_2)
    #print(eigen_vect)
    #print(eigen_values)
    

    cv2.line(img_real, center, (x_2, y_2), (255,0,0))
    cv2.line(img_real, center, (x_1, y_1), (255,0,0))
    
    
    
    angle = m.atan2(y_2,x_2)
    angle2 = "%.2f theta" % angle
    cv2.putText(img_real,angle2, center, font,1, (0,0,255), 2)
    
    
    cv2.imshow("Direction image", img_real)

    time_show_image()
    close_windows()
    

