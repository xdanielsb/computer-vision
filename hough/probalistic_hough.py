import cv2
import numpy as np

img = cv2.imread('../assets/images/sudoku.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = []
for minLineLength in range (10, 100):
    for maxLineGap in range (10,11):
        lines.extend( cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap))

for l in lines:
    for x1,y1,x2,y2 in l:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("Hough transform", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
