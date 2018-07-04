import cv2
import numpy as np
import matplotlib.pyplot as plt

# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,100,(25,4)).astype(np.float32)

# Labels each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

print("train data")
print(trainData)
print("responses")
print(responses)

newcomer = np.random.randint(0,100,(1,4)).astype(np.float32)
print("new Commer")
print(newcomer)

#train
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
numNeighbors = 5
ret, results, neighbours ,dist = knn.findNearest(newcomer, 5)
print "result class: ", results,"\n"
print "neighbours: ", neighbours,"\n"
print "distance: ", dist

