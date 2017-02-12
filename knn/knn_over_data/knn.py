from __future__ import print_function 
from operator import itemgetter
import math 

"""
    Pretty good links to learn about the algorithms.
    https://github.com/scottelundgren/knn/blob/master/knn.py
    https://www.dataquest.io/blog/k-nearest-neighbors-in-python/
"""


"""
    Improvements
    Create a method for accuracy
"""


__author__ = "Daniel Santos"

import pandas as pa
import numpy as nu


"""
    Load the set in a csv file.
"""
def load_data_set(name):
    return pa.read_csv(name);

"""
    Get the training set
"""
def get_training_set(porcentaje, data):
    return data.sample(frac=porcentaje)


"""
    Get sample set for testing the algorithm
"""
def get_test_set(training_set, data):
    #This script just give me the set removing the sample.
    return data.loc[~data.index.isin(training_set.index)]

"""
    Just a simple euclidean function
"""
def euclidean_distance(row, data_to_predict):
    inner_value = 0 
    distance_columns = ["a", "b", "c", "d"]
    for k in distance_columns:
        inner_value += (row[k] - data_to_predict[k]) ** 2
    
    return math.sqrt(inner_value)


"""
    Applying knn
"""

def knn(training_set, test_set, k):
    #Save the predictions
    predictions  = []
    
    #Iter over the data that we need to predict 
    for index, x in test_set.iterrows():
        data_to_predict = x
        distances = []
        #Iter over the the training set
        for index2, row in training_set.iterrows(): 
            distances.append((euclidean_distance(row, data_to_predict), index2)) 
        
        distances.sort()
        predictions.append(( index, distances[:k]))

    return predictions

if (__name__ == "__main__"):

    #All the sample
    data = load_data_set("flowers.csv")
    
    #The training set is going to be the 99 %
    training_set = get_training_set(0.99, data)

    #The test set
    test_set = get_test_set(training_set, data) 
    
    

    k= 20
    predictions = knn(training_set, test_set, k)
    for predict in predictions:
        print("Data to  predict")
        
        id_to = predict[0]
        k_nearest = predict[1]
        print (data.loc[id_to])
        print("\n")
        
        
        print ("\tK-nearest-neighbors")
        for n in k_nearest:
            distance = n[0]
            id_neigh = n[1]
            print ("Distance to the neighbor {} is {} \n".format(n[1], n[0]))
            print (data.loc[id_neigh])
            print()


