from __future__ import print_function 
import math 

"""
    Pretty good links to learn about the algorithms.
    https://github.com/scottelundgren/knn/blob/master/knn.py
    https://www.dataquest.io/blog/k-nearest-neighbors-in-python/
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
def get_training_set(porcentaje):
    return colors.sample(frac=porcentaje)


"""
    Get sample set for testing the algorithm
"""
def get_test_set(training_set):
    #This script just give me the set removing the sample.
    return colors.loc[~colors.index.isin(training_set.index)]

"""
    Just a simple euclidean function
"""
def euclidean_distance(row):
    inner_value = 0 
    distance_columns = ["x", "y"]
    data_to_predict = {"x": 123, "y":127};
    for k in distance_columns:
        inner_value += (row[k] - data_to_predict[k]) ** 2

    return math.sqrt(inner_value)


"""
    Applying knn
"""

def knn(training_set, test_set):
    k = 3
    predictions  = []
    
    for index, x in test_set.iterrows():
        data_to_predict  = x
        distances = training_set.apply(euclidean_distance, axis =1); 

if (__name__ == "__main__"):
    colors = load_data_set("colors.csv")
    training_set = get_training_set(0.1)
    test_set = get_test_set(training_set)
    
    knn(training_set, test_set)
    
    


#    print(type(colors))
 #   print(training_set)
  #  print(test_set)
    
