import cv2
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



def hough_transform(img, real):
    edges = cv2.Canny(img,50,150,apertureSize = 3)
    aux = 0
    margen = 95
    circles  = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=aux,maxRadius=aux+margen)
    
    #circles = np.uint16(np.around(circles))
    print("These are the circles.")
    print(circles)

    if circles != None:
        for i in circles[0,:]:
           cv2.circle(real,(i[0],i[1]),i[2],(0,255,0),1) # draw the outer circle
           cv2.circle(real,(i[0],i[1]),2,(0,0,255),3) # draw the center of the circle

    cv2.imshow("Hough transform", real)


if __name__ == "__main__":

    img = readi('../assets/images/circles.png', "gray")
    hough_transform(img, readi('../assets/images/circles.png'))
    time_show_image()
    close_windows()

