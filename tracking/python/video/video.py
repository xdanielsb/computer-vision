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
img_train = cv2.imread('0.png',0)
kp1 = None
des1 = None
orb = None


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
            NUM_IMAGE  +=  1



def drawMatches(matches, kp1, kp2):
    global ACTUAL_IMAGE


    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:

        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        # x - columns
        # y - rows
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt
        print("Detected point",x1,y1)

        # Draw a small circle at both co-ordinates
        # radius 4
        # colour blue
        # thickness = 1
           
        cv2.circle(ACTUAL_IMAGE, (int(x2),int(y2)), 4, (255,0,0 ), 1)   
        #cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)
        #print this is the code that   need theh e teh


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    global ACTUAL_IMAGE
    global CROP
    global img_train
    global kp1
    global des1
    global orb
 
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
        CROP = [(0,0),(0,0)]
        cv2.imshow('CROP IMAGE', result)
        
        # trainImage
        img_train = result
        
        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(result,None)




def video_capture():

    global FINISH
    global DEBUG
    global TRACKING
    global PAUSED
    global NUM_IMAGE
    global THRESH_VALUE
    global ACTUAL_IMAGE
    global kp1
    global des1
    global orb
    global img_train

    cap = cv2.VideoCapture(0)
    
    # Initiate SIFT detector
    orb = cv2.ORB()
     
    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

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

            #Read key points image 1
            kp2, des2 = orb.detectAndCompute(ACTUAL_IMAGE,None)

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
        
            
            matches = bf.match(des1,des2)
            matches = sorted(matches, key = lambda x:x.distance)
            drawMatches(matches, kp1, kp2)



            
            #Show the image
            cv2.setMouseCallback("VIDEO", click_and_crop)
            cv2.rectangle(ACTUAL_IMAGE, CROP[0], CROP[1], (0, 255, 0), 2)
            cv2.imshow("VIDEO", ACTUAL_IMAGE)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


video_capture()
