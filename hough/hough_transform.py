import cv2
import numpy as np

imgc = cv2.imread('../assets/images/sudoku.png', 1)
img = cv2.imread('../assets/images/sudoku.png', 0)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

kernel = np.ones((3,3),np.uint8)

edges = cv2.Canny(th2,50,150,apertureSize = 3)

maxo = 0
ie = 0
aux = []

for i in range (140, 250):
    lines = cv2.HoughLines(edges,1,np.pi/180,i)
    aux.extend(lines)
    

for l in aux:
    for rho,theta in l:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(imgc,(x1,y1),(x2,y2),(0,0,0),1)

cv2.imshow("Hough transform", imgc)
cv2.waitKey(0)
cv2.destroyAllWindows()
