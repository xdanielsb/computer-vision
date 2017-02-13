import cv2


print (cv2.__version__)
img = cv2.imread("smile.jpg", 0)
dimy = len(img)
dimx = len(img[0])

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print (img)
