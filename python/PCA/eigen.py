import cv2 as cv
import numpy as np
import sympy

def find_eigen(matrix):
    eigen_valor, eigen_vect = np.linalg.eig(matrix)
    return eigen_valor, eigen_vect

def read_matrix():
    filep = open("data", "r")
    mat = []
    for l in filep:
        mat.append([float(y) for y in l.split()])

    arr = np.array(mat)
    return arr

def init():
    arr = read_matrix()
    print(arr)
    cov = np.cov(arr.transpose())

    eigen_valor, eigen_vect = find_eigen(cov)
    print("eigen valores:")
    print(eigen_valor)

    print("eigen vectores:")
    print(eigen_vect)

if __name__ == "__main__":
    init()

