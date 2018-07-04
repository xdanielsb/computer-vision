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



if __name__ == "__main__":
    #Read the image 
    img_real = readi("../../assets/images/hand.jpg", "color")
    img = readi("../../assets/images/hand.jpg", "gray")
    ##cv2.imshow("Color Image", img)

    #Now threshold the image
    _, thr= cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ##cv2.imshow("Threshold Image", thr)

    #Now find countours
    contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Draw contours in the image
    #1 means draw the countour 1
    cv2.drawContours(img_real, contours, 1, (0,255,0), 3)

    

    countour_hand = contours[1]

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
    cv2.putText(img_real,"Mass center", center, font,1, (0,0,255), 2)

    cv2.imshow("Contours in tthe image", img_real)

    print(cx,cy)

    time_show_image()
    close_windows()
    

