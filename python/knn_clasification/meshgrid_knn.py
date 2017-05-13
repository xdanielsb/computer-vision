import cv2
import numpy as np
from matplotlib import pyplot as plt
from decimal import *
import math
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.colors as mcolors
import random


def get_random_colour ():
    return '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))


def get_random_points(num_points = 3):
    points = []
    responses = []
    colours = []
    colours_mesh  = []
    #Creating random point
    for i in range(num_points):
        valx = random.randint(0,101)
        valy = random.randint(0,101)
        points.append([valx, valy])
        responses.append(i)

    #Creating random colours, mesh
    chars = '0123456789ABCDEF'
    for i in range(num_points):
        colour = get_random_colour()
        colours.append(colour)

    #Creating random colours, points in the mesh
    for i in range(num_points):
        colour = get_random_colour()
        colours_mesh.append(colour)

    return np.float32(points), np.float32(responses), mcolors.ListedColormap(colours), mcolors.ListedColormap(colours_mesh)


def get_points_grid():
    step = 0.2
    values  = np.arange( 0, 100, step )
    x_values, y_values = np.meshgrid( values ,values )
    #Create pairs of points 
    pairs = np.float32(np.c_[x_values.ravel(), y_values.ravel()])
    dim  = x_values.shape
    return pairs, dim, x_values, y_values





if __name__ == "__main__":
    #Creat random points
    points, responses, colours, colours_points = get_random_points(1000)
    
    #Create and train clasifier
    KNN_Classifier = cv2.KNearest()
    KNN_Classifier.train( points, responses )

    #Get points of the grid
    points_grid, dim, x_values, y_values = get_points_grid()
    
    retval, results, neigh_resp, dists = KNN_Classifier.find_nearest( points_grid , 1)
    results = results.reshape(dim)

    # Graficamos para observar los resultados obtenidos
    plt.figure()
    plt.pcolormesh( x_values, y_values, results, cmap = colours )

    x_values_sample, y_values_sample = points[:,0], points[:,1]
    plt.scatter( x_values_sample, y_values_sample, c = responses, cmap = colours_points)
    plt.xlim( x_values.min(), x_values.max())
    plt.show()

