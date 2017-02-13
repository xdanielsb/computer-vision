import cv2
import numpy as np
import matplotlib.pyplot as plt


def plot(trainData, testData,responses):
    
    # Take Red families and plot them
    red = trainData[responses.ravel()==0]
    print (red)
    plt.scatter(red[:,0],red[:,1],80,'r','^')

    # Take Blue families and plot them
    blue = trainData[responses.ravel()==1]
    plt.scatter(blue[:,0],blue[:,1],80,'b','s')

    plt.show()



if( __name__ == "__main__"):

    # Feature set containing (x,y) values of 25 known/training data
    #Create arrays of 25x2 of the range (0, 99)
    trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

    # Labels each one either Red or Blue with numbers 0 and 1
    #Create array of data 25x1 fo the range 0,2
    responses = np.random.randint(0,2,(25,1)).astype(np.float32)
    
    plot(trainData, trainData, responses)




