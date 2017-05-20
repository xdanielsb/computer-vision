from variables import *
# from utilities import drawMatches, click_and_crop
import variables as var

import numpy as np
import cv2


def nothing(x):
    pass


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

        cv2.circle(var.ACTUAL_IMAGE, (int(x2),int(y2)), 4, (255,0,0 ), 3)
        #cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)
        #print this is the code that   need theh e teh


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping, ACTUAL_IMAGE, CROP, IMG_TRAIN, kp1, des1, orb

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        var.CROP[0] = (x,y)



    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        print(x,y)
        var.CROP[1] = (x,y)
        result = var.ACTUAL_IMAGE[var.CROP[0][1]:var.CROP[1][1], var.CROP[0][0]:var.CROP[1][0]]
        var.CROP = [(0,0),(0,0)]
        cv2.imshow('CROP IMAGE', result)

        # trainImage
        var.IMG_TRAIN = result

        # find the keypoints and descriptors with SIFT
        var.kp1, var.des1 = orb.detectAndCompute(result,None)

def video_capture():

    global FINISH, DEBUG, TRACKING, PAUSED, NUM_IMAGE, THRESH_VALUE, ACTUAL_IMAGE, kp1, des1, orb, IMG_TRAIN

    cap = cv2.VideoCapture(1)

    # Initiate SIFT detector
    #orb = cv2.SIFT()

    #Initiate ORB
    #orb = cv2.ORB()

    #Initiate SURF
    orb = cv2.SURF(400)

    # create BFMatcher object
    bf = cv2.BFMatcher()

    FIRST = True


    #img1 = cv2.imread('whole.png',0)
   # kp1, des1 = orb.detectAndCompute(img1,None)


    while(var.FINISH == False):
        # Capture frame-by-frame
        var.options()
        ret1, var.ACTUAL_IMAGE = cap.read()


        if(var.PAUSED == False):
            ret1, var.ACTUAL_IMAGE = cap.read()
            frame1 = cv2.cvtColor(var.ACTUAL_IMAGE, cv2.COLOR_BGR2GRAY)
            ret2, frame2 = cap.read()
            frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            #Compute the difference between the images
            difference = cv2.absdiff(frame2, frame1)

            #Threshold the image
            ret,thresh1 = cv2.threshold(difference,THRESH_VALUE,255,cv2.THRESH_BINARY)

            #Remove possible noise
            blur = cv2.blur(thresh1,(5,5))

            #Read key points image 1
            kp2, des2 = orb.detectAndCompute(var.ACTUAL_IMAGE,None)

            if(var.DEBUG):

                cv2.imshow('difference', difference)
                cv2.imshow('threshold', thresh1)
                cv2.imshow('blur', blur)

                if(FIRST):
                    cv2.createTrackbar('THRESH_VALUE','threshold',THRESH_VALUE,255,nothing)
                    FIRST = False

                THRESH_VALUE = cv2.getTrackbarPos('THRESH_VALUE','threshold')

            else:
                cv2.destroyWindow('difference')
                cv2.destroyWindow('threshold')
                cv2.destroyWindow('blur')
                FIRST = True


            if(var.TRACKING):
                contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                #DRAW ALL COUNTOURS IN THE IMAGE
                cv2.drawContours(var.ACTUAL_IMAGE, contours, -1, (0,255,0), 3)


            if(False): #Check this part
                FLANN_INDEX_KDTREE = 1
                index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
                search_params = dict(checks=50)   # or pass empty dictionary
                flann = cv2.FlannBasedMatcher(index_params,search_params)
                matches = flann.knnMatch(des1,des2,k=2)
                print (matches)
                # cv2.drawMatchesKnn expects list of lists as matches.
                img3 = cv2.drawMatchesKnn(ACTUAL_IMAGE,kp1,img_train,kp2,good,flags=2)


            else:
                matches = bf.match(var.des1,des2)
                matches = sorted(matches, key = lambda x:x.distance)
                drawMatches(matches, var.kp1, kp2)


            #Show the image
            cv2.setMouseCallback("VIDEO", click_and_crop)
            cv2.rectangle(var.ACTUAL_IMAGE, CROP[0], CROP[1], (0, 255, 0), 2)
            cv2.imshow("VIDEO", var.ACTUAL_IMAGE)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


video_capture()
