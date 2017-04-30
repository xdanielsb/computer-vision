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
    img_real = readi("../assets/images/hand.jpg", "color")
    img = readi("../assets/images/hand.jpg", "gray")
    _, thr= cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imshow("Thershold", thr)
    res = cv2.HuMoments(cv2.moments(thr)).flatten()
    print (res)

    
    time_show_image()
    close_windows()
    
