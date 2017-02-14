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
def euclidean_distance(row, data_to_predict, distance_columns):
    inner_value = 0 
    for k in distance_columns:
        inner_value += (row[k] - data_to_predict[k]) ** 2
    
    return math.sqrt(inner_value)


"""
    Applying knn
    training_set -> Classified data -->  DataFrame
    test_set -> Data for testing the model -->  DataFrame
    k -> number of neighbors --> int
    columns -> Features for applying the euclidean distance


    Return
    The k_neighbors
"""

def knn(training_set, test_set, k, columns):
    #Save the predictions
    predictions  = []
    
    #Iter over the data that we need to predict 
    for index, x in test_set.iterrows():
        data_to_predict = x
        distances = []
        #Iter over the the training set
        for index2, row in training_set.iterrows(): 
            distances.append((euclidean_distance(row, data_to_predict, columns), index2)) 
        
        #Sort for later get the less distances
        distances.sort()
        ###It is necesary if there are at least k neighbors
        if (len(distances) >= k):
            k_neighbors = distances[:k]

        n = []  #Store the data serie of each neighbore based on his id 
               
        
        for k in k_neighbors:
            id_n = k[1]
            distance_n = k[0]
            neig = training_set.loc[id_n]
            n.append((neig, distance_n))
        

        

        #index --> of the item of the test that we want to predict
        predictions.append(( index, n )) ##Select the k neighbors
    print (predictions)
    
    return predictions



