#Just a dirty trick
from variables import *
import variables as var
from utilities import *
from useful_functions import *

import numpy as np
import cv2

#Auxiliar variable to help me to intance once
FIRST = True

def nothing(x):
    pass


def choose_matcher():
    var.OPTION_MATCHER = "SIFT"

    if var.OPTION_MATCHER == "ORB":
        var.orb = cv2.ORB()
        var.OPTION_MATCHER = "ORB"

    elif var.OPTION_MATCHER == "SIFT":
        var.orb = cv2.SIFT()
        var.OPTION_MATCHER = "SIFT"
    else:
        var.orb = cv2.SURF(400)
        var.OPTION_MATCHER = "SURF"
    print("The option matcher is: "+ var.OPTION_MATCHER)


def debug(blur):
    global  DEBUG, THRESH_VALUE, FIRST
    if(var.DEBUG):
        cv2.imshow('blur', blur)
        if(FIRST):
            cv2.createTrackbar('THRESH_VALUE','blur',var.THRESH_VALUE,255,nothing)
            FIRST = False
        var.THRESH_VALUE = cv2.getTrackbarPos('THRESH_VALUE','blur')
    else:
        cv2.destroyWindow('blur')
        FIRST = True


def tracking(blur):
    global TRACKING, ACTUAL_IMAGE
    if(var.TRACKING):
        contours = find_contours(blur)
        #DRAW ALL COUNTOURS IN THE IMAGE
        #print(contours)
        var.ACTUAL_IMAGE = draw_contours(var.ACTUAL_IMAGE, contours)


def apply_matcher(bf, des2, kp2):
    global des1, kp1, ACTUAL_IMAGE, img_train

    if(False): #Check this part
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params,search_params)
        matches = flann.knnMatch(var.des1,des2,k=2)
        print (matches)
        # cv2.drawMatchesKnn expects list of lists as matches.
        img3 = cv2.drawMatchesKnn(var.ACTUAL_IMAGE,var.kp1,var.img_train,kp2,good,flags=2)


    else:
        matches = bf.match(var.des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)
        #print("Number of matches: {}".format(len(matches)))
        if len(matches) < 10:
            best_matches = matches
        else:
            best_matches = matches[0:len(matches)/5]
        points = drawMatches(best_matches, var.kp1, kp2)
        if len(points)>0:
            hull = get_convex_hull(points)
            print("hull",hull)



def video_capture():

    global FINISH, DEBUG, TRACKING, PAUSED, NUM_IMAGE, THRESH_VALUE, ACTUAL_IMAGE, kp1, des1, orb, IMG_TRAIN, OPTION_MATCHER

    #Create the instance of the video
    cap = cv2.VideoCapture(1)
    #Choose the method to match
    choose_matcher()
    #Instance the matcher
    bf = cv2.BFMatcher()


    while(var.FINISH == False):
        #Call the key listener for options
        var.options()
        # Capture frame-by-frame
        ret1, var.ACTUAL_IMAGE = cap.read()


        if(var.PAUSED == False):
            _, var.ACTUAL_IMAGE = cap.read()
            frame1 = to_gray(var.ACTUAL_IMAGE)
            _, frame2 = cap.read()
            frame2 = to_gray(frame2)

            #Compute the difference between the images
            difference = cv2.absdiff(frame2, frame1)

            #Threshold the image
            _,thr = threshold_bin(difference, var.THRESH_VALUE)

            #Remove possible noise
            blur = blur_(thr)

            #Read key points image 1
            kp2, des2 = var.orb.detectAndCompute(var.ACTUAL_IMAGE,None)

            #Call debug options
            debug(blur)

            #Call tracking movement
            tracking(blur)

            #Apply matcher in order to match features
            apply_matcher(bf, des2, kp2)

            #Show the image
            cv2.setMouseCallback("VIDEO", click_and_crop)

            if(var.CROP[0] != (0,0)):
                cv2.rectangle(var.ACTUAL_IMAGE, var.CROP[0], var.CROP[1], (0, 255, 0), 2)

            cv2.imshow("VIDEO", var.ACTUAL_IMAGE)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
