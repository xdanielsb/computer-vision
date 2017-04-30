import cv2
import numpy as np

img = cv2.imread('../../tracking/python/video/0.png')


#gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.imread('../../tracking/python/video/part2.png')
sift = cv2.SIFT()
kp = sift.detect(gray,None)
img_s=cv2.drawKeypoints(gray,kp)


cv2.imshow("SIFT", img_s)
cv2.imshow("Detect Patterns", gray)
cv2.imshow("Real Image", img)
cv2.waitKey(0)

