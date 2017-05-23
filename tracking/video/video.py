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

    if var.ACTIVE_ORB:
        var.orb = cv2.ORB()
    if var.ACTIVE_SIFT:
        var.sift = cv2.SIFT()
    if var.ACTIVE_SURF:
        var.surf = cv2.SURF(400)


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


def find_matches(bf, des1, des2, kp1 , kp2, color):
    matches = bf.match(des1,des2)
    matches = sorted(matches, key = lambda x:x.distance)
    #print("Number of matches: {}".format(len(matches)))
    if len(matches) < 10:
        best_matches = matches
    else:
        best_matches = matches[0:len(matches)/5]
    points = drawMatches(best_matches, kp1, kp2, color)
    if len(points)>0:
        hull = get_convex_hull(points)
        draw_convex_hull(var.ACTUAL_IMAGE, hull)


def video_capture():

    global FINISH, DEBUG, TRACKING, PAUSED, NUM_IMAGE, THRESH_VALUE, ACTUAL_IMAGE
    global kp1, des1, orb, IMG_TRAIN, OPTION_MATCHER
    global orb, sift, surf, kp_orb, kp_sift, kp_surf, des_orb, des_sift
    global des_surf, ACTIVE_ORB, ACTIVE_SIFT, ACTIVE_SURF

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
            if var.ACTIVE_ORB:
                kp_orb2, des_orb2 = var.orb.detectAndCompute(var.ACTUAL_IMAGE,None)
                find_matches(bf, var.des_orb, des_orb2, var.kp_orb, kp_orb2, (237, 241, 20))

            if var.ACTIVE_SURF:
                kp_surf2, des_surf2 = var.surf.detectAndCompute(var.ACTUAL_IMAGE,None)
                find_matches(bf, var.des_surf, des_surf2, var.kp_surf, kp_surf2, (33, 218, 215))


            if var.ACTIVE_SIFT:
                kp_sift2, des_sift2 = var.sift.detectAndCompute(var.ACTUAL_IMAGE,None)
                find_matches(bf, var.des_sift, des_sift2, var.kp_sift, kp_sift2, (252, 89, 9))



            #Call debug options
            debug(blur)

            #Call tracking movement
            tracking(blur)

            #Show the image
            cv2.setMouseCallback("VIDEO", click_and_crop)

            if(var.CROP[0] != (0,0)):
                cv2.rectangle(var.ACTUAL_IMAGE, var.CROP[0], var.CROP[1], (0, 255, 0), 2)

            cv2.imshow("VIDEO", var.ACTUAL_IMAGE)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
