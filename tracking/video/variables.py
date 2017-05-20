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

        cv2.circle(ACTUAL_IMAGE, (int(x2),int(y2)), 4, (255,0,0 ), 3)
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
        CROP[0] = (x,y)



    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        print(x,y)
        CROP[1] = (x,y)
        result = ACTUAL_IMAGE[CROP[0][1]:CROP[1][1], CROP[0][0]:CROP[1][0]]
        CROP = [(0,0),(0,0)]
        cv2.imshow('CROP IMAGE', result)

        # trainImage
        IMG_TRAIN = result

        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(result,None)
