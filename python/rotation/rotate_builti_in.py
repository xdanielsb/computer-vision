import cv2

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
    This code rotate an image 
"""
def rotate(img, angle):
    rows,cols = img.shape[0], img.shape[1]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst
    

if __name__ == "__main__":
    
    img1 = readi("../assets/images/hand.jpg")
    img1 = rotate(img1, 90)
    cv2.imshow("Color Image", img1)
    
    img2 = readi("../assets/images/hand.jpg", "gray")

    angle = 30
    img_rotate = rotate(img2, angle)
    
    cv2.imshow("Rotated image", img_rotate)

    time_show_image()
    close_windows()


