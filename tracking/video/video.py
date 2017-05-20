from variables import *
import variables as var

import numpy as np
import cv2


def nothing(x):
    pass


def video_capture():

    global FINISH, DEBUG, TRACKING, PAUSED, NUM_IMAGE, THRESH_VALUE, ACTUAL_IMAGE, kp1, des1, orb, IMG_TRAIN

    cap = cv2.VideoCapture(1)

    # Initiate SIFT detector
    #orb = cv2.SIFT()

    #Initiate ORB
    #orb = cv2.ORB()

    #Initiate SURF
    var.orb = cv2.SURF(400)

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
            kp2, des2 = var.orb.detectAndCompute(var.ACTUAL_IMAGE,None)

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
