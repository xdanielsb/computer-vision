import cv2
import numpy as np
from useful_functions import get_hu_moments

FINISH = False
DEBUG = False
TRACKING = False
PAUSED = False
ACTIVE_METHODS = True
ACTIVE_FOLLOW = False

NUM_IMAGE = 0
THRESH_VALUE = 50
ACTUAL_IMAGE = None
CROP = [(0,0),(0,0)]
SIFT_IMG = None
IMG_TRAIN = None
OPTION_MATCHER = None



#Matchers
orb = None
kp_orb = None
des_orb = None
ACTIVE_ORB = True

surf = None
kp_surf = None
des_surf = None
ACTIVE_SURF = True

sift = None
kp_sift = None
des_sift = None
ACTIVE_SIFT = True


def options():
    global FINISH, DEBUG, TRACKING, PAUSED, NUM_IMAGE, ACTUAL_IMAGE
    global OPTION_MATCHER,  IMG_TRAIN
    global orb, sift, surf, kp_orb, kp_sift, kp_surf, des_orb, des_sift
    global des_surf, ACTIVE_ORB, ACTIVE_SIFT, ACTIVE_SURF
    global ACTIVE_METHODS, ACTIVE_FOLLOW

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

        if(key == "o" or key  == "O"):
            ACTIVE_ORB = not ACTIVE_ORB
            if ACTIVE_ORB == True:
                print("Method 1 of tracking was desactivated.")
            else:
                print("Method 1 of tracking  was activated")

        if(key == "u" or key  == "U"):
            ACTIVE_SURF = not ACTIVE_SURF
            if ACTIVE_SURF == True:
                print("Method 2 of tracking  was desactivated")
            else:
                print("Method 2 of tracking  was activated")

        if(key == "s" or key  == "S"):
            ACTIVE_SIFT = not ACTIVE_SIFT
            if ACTIVE_SIFT == True:
                print("Method 3 of tracking  was desactivated")
            else:
                print("Method 3 of tracking  was activated")

        if(key == "f" or key  == "F"):
            ACTIVE_FOLLOW = not ACTIVE_FOLLOW
            if ACTIVE_FOLLOW == True:
                print("Follow was activated")
            else:
                print("Follow  was desactivated")

        if (key == "m" or key == "M"):
            ACTIVE_METHODS = not ACTIVE_METHODS
            if ACTIVE_METHODS == True:
                print("VISUALIZATION OF METHODS  was activated")
            else:
                print("VISUALIZATION OF METHODS was desactivated")


def drawMatches(matches, kp1, kp2, c):
    global ACTUAL_IMAGE

    points = []
    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:

        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt
        points.append([x2,y2])

        # print("Detected point",x1,y1)
        if ACTIVE_METHODS:
            cv2.circle(ACTUAL_IMAGE, (int(x2),int(y2)), 4, c, 3)

    return np.array(points, dtype=np.float32), points


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping, ACTUAL_IMAGE, CROP, IMG_TRAIN
    global orb, sift, surf, kp_orb, kp_sift, kp_surf, des_orb, des_sift
    global des_surf, ACTIVE_ORB, ACTIVE_SIFT, ACTIVE_SURF

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(x,y)
        CROP[0] = (x,y)

    if event == cv2.EVENT_MOUSEMOVE:
        if(CROP[0] != (0,0)):
            CROP[1] = (x,y)
            #cv2.rectangle(ACTUAL_IMAGE, CROP[0], CROP[1], (0, 255, 0), 2)


    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:

        result = ACTUAL_IMAGE[CROP[0][1]:CROP[1][1], CROP[0][0]:CROP[1][0]]

        CROP = [(0,0),(0,0)]
        if(result.shape[0] >5):
            print("HU MOMENT ")
            print(get_hu_moments(result))
            cv2.imshow('Image to track', result)
            cv2.moveWindow('Image to track', 10, 500)

        # trainImage
        IMG_TRAIN = result

        # find the keypoints and descriptors with SIFT
        if ACTIVE_ORB:
            kp_orb, des_orb = orb.detectAndCompute(IMG_TRAIN,None)
        if ACTIVE_SURF:
            kp_surf, des_surf = surf.detectAndCompute(IMG_TRAIN,None)
        if ACTIVE_SIFT:
            kp_sift, des_sift = sift.detectAndCompute(IMG_TRAIN,None)
