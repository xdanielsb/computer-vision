import cv2

FINISH = False
DEBUG = False
TRACKING = False
PAUSED = False
NUM_IMAGE = 0
THRESH_VALUE = 130
ACTUAL_IMAGE = None
CROP = [(0,0),(0,0)]
SIFT_IMG = None
IMG_TRAIN = None
kp1 = None
des1 = None
orb = None


def options():
    global FINISH, DEBUG, TRACKING, PAUSED, NUM_IMAGE, ACTUAL_IMAGE

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
