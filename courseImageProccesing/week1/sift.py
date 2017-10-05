import cv2
import numpy as np
import time

# Read image and convert to grayscale

pathimg1 = "train/forest/bost98.jpg"
ima=cv2.imread(pathimg1)
gray=cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)

# Create detector and descriptor structures to compute SIFT
detector=cv2.xfeatures2d.SIFT_create()

# Detect keypoints with SIFT and sort them according to their response
print 'Extracting Keypoints'
init=time.time()
kpts, _ = detector.detectAndCompute(gray,None)
kpts = sorted(kpts, key = lambda x:x.response)

end=time.time()
print 'Extracted '+str(len(kpts))+' keypoints.'
print 'Done in '+str(end-init)+' secs.'
print ''

# Compute SIFT descriptor for all keypoints
print 'Computing SIFT descriptors'
init=time.time()
kpts, des = detector.detectAndCompute(gray,None)
end=time.time()
print 'Done in '+str(end-init)+' secs.'

# Show result of detecting keypoints
im_with_keypoints = cv2.drawKeypoints(ima, kpts, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey()


