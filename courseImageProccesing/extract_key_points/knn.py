from __future__ import print_function
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

clases  ={"coast":0, "forest":1, "highway":2, "inside_city":3, "mountain":4, "Opencountry":5, "street":6, "tallbuilding":7}
clasest  ={0:"coast", 1:"forest", 2:"highway", 3:"inside_city", 4:"mountain", 5:"Opencountry", 6:"street",7:"tallbuilding"}
sizes = {"SIFT":128}
trainData = []
responses = []

#Getting images of each class
for typei in clases:
  print(typei)
  images = glob.glob("train/"+typei+"/*.jpg")
  
  for pathimg1 in images:
    img1 = cv2.imread(pathimg1,0) 
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, train = sift.detectAndCompute(img1,None)
    for d in train: trainData.append(d.tolist())
    res =  np.array([clases[typei] for x in range(0,len(train))], dtype=np.float32)
    responses+=res.tolist()


"""

bf = cv2.BFMatcher()
"""

#train
trainData = np.array(trainData, dtype=np.float32)
responses = np.array(responses, dtype=np.float32)
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)




#Getting images of each class
for typei in clases:
  images = glob.glob("test/"+typei+"/*.jpg")[:2]
  for pathimg2 in images:
    img2 = cv2.imread(pathimg2,0) 
    kp2, newcomers = sift.detectAndCompute(img2,None)
    resbyimage = []
    for newcomer in newcomers:
      numNeighbors = 5
      
      newcomer = np.array([newcomer], dtype=np.float32)
      ret, results, neighbours ,dist = knn.findNearest(newcomer, 5)
      for x,y in zip(dist[0], neighbours[0]):
        resbyimage.append((x,y))
    resbyimage.sort()
    res = []

    num = len(resbyimage)/2
    for e in resbyimage[:num]:
      res.append(e[1])

    resbyimage = np.array(res)
    
    #find the mode
    counts = np.bincount(res)
    mode =  np.argmax(counts)
    print ("for the image: "+ pathimg2+ " the class is: "+ clasest[mode] + " with code: " +str(mode)+ " taking: "+str(num))

"""
  print ("result class: ", classi,"\n")
  print ("neighbours: ", neighbours,"\n")
  print ("distance: ", dist)
 """
