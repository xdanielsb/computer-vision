import numpy as np
import cv2

FINISH = False
DEBUG = False
TRACKING = False
PAUSED = False
NUM_IMAGE = 0
THRESH_VALUE = 20
ACTUAL_IMAGE = None
CROP = [(0,0),(0,0)]
SIFT_IMG = None

def nothing(x):
    pass

def options():
    global FINISH
    global DEBUG
    global TRACKING
    global PAUSED
    global NUM_IMAGE
    global ACTUAL_IMAGE

    key  = chr(cv2.waitKey(33) & 0xFF)

    if (key != '\xff'):
        if(key == "d" or key  == "D"):
            DEBUG = not DEBUG
            if(DEBUG): print("DEBUG ACTIVATED") 
            else: print("DEBUG DISACTIVATE")
            
        if(key == "t" or key  == "T"):
            TRACKING = not TRACKING
            if(TRACKING): print("TRACKING ACTIVATED") 
            else: print("TRACKING DISACTIVATE")

        if(key == "f" or key  == "F"):
            FINISH  = not FINISH
            if(FINISH): print("BYE BYE") 

        if(key == "p" or key  == "P"):
            PAUSED = not PAUSED
            if(PAUSED): print("THE PROGRAM IS PAUSED") 
            else: print("UNPAUSED")
            

        if(key == "W" or key  == "w"): 
            name_image = str(NUM_IMAGE)+'.png' 
            cv2.imwrite(name_image ,ACTUAL_IMAGE)
            print("The image {} was saved.".format(name_image))




def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    global ACTUAL_IMAGE
    global CROP
    
 
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        CROP[0] = (x,y)


 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        print(x,y)
        CROP[1] = (x,y)
        result = ACTUAL_IMAGE[CROP[0][1]:CROP[1][1], CROP[0][0]:CROP[1][0]]
        cv2.imshow('CROP IMAGE', result)

def video_capture():

    global FINISH
    global DEBUG
    global TRACKING
    global PAUSED
    global NUM_IMAGE
    global THRESH_VALUE
    global ACTUAL_IMAGE

    cap = cv2.VideoCapture(0)
    sift = cv2.SIFT()
    FIRST = True

    while(FINISH == False):
        # Capture frame-by-frame
        options()
        ret1, ACTUAL_IMAGE = cap.read()


        if(PAUSED == False):
            ret1, ACTUAL_IMAGE = cap.read()
            frame1 = cv2.cvtColor(ACTUAL_IMAGE, cv2.COLOR_BGR2GRAY)
            ret2, frame2 = cap.read()
            frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            #Compute the difference between the images
            difference = cv2.absdiff(frame2, frame1)
            
            #Threshold the image
            ret,thresh1 = cv2.threshold(difference,THRESH_VALUE,255,cv2.THRESH_BINARY)
            
            #Remove possible noise
            blur = cv2.blur(thresh1,(5,5))

            if(DEBUG):
                                
                cv2.imshow('difference', difference)
                cv2.imshow('threshold', thresh1)
                cv2.imshow('blur', blur)
                
                if(FIRST):
                    cv2.createTrackbar('THRESH_VALUE','threshold',THRESH_VALUE,255,nothing)
                    FIRST = False
                
                THRESH_VALUE = cv2.getTrackbarPos('THRESH_VALUE','threshold')

            else:
                cv2.destroyWindow('gray')
                cv2.destroyWindow('difference')
                cv2.destroyWindow('threshold')
                cv2.destroyWindow('blur')
                FIRST = True


            if(TRACKING):
                contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                #DRAW ALL COUNTOURS IN THE IMAGE
                cv2.drawContours(ACTUAL_IMAGE, contours, -1, (0,255,0), 3)
        


            
            #Show the image
            cv2.setMouseCallback("VIDEO", click_and_crop)
            cv2.rectangle(ACTUAL_IMAGE, CROP[0], CROP[1], (0, 255, 0), 2)
            cv2.imshow("VIDEO", ACTUAL_IMAGE)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


video_capture()
