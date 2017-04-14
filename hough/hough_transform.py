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


def Hough_transform(img, imgc):


    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    kernel = np.ones((3,3),np.uint8)

    edges = cv2.Canny(th2,50,150,apertureSize = 3)

    maxo = 0
    ie = 0
    aux = []

    for i in range (140, 250):
        lines = cv2.HoughLines(edges,1,np.pi/180,i)
        aux.extend(lines)


    for l in aux:
        for rho,theta in l:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(imgc,(x1,y1),(x2,y2),(0,0,0),1)

    cv2.imshow("Hough transform", imgc)



if __name__ == "__main__":

    imgc = readi('../assets/images/sudoku.png')
    img = readi('../assets/images/sudoku.png', "gray")
    Hough_transform(img,imgc)
    time_show_image()
    close_windows()
