import numpy as np
"""
    This function help us to create and image with new dimensions

    @param
    img ---> image
    factor ---> the scale that creates the new size of the image.

    @return
    Clean array with new dimensions
"""

def enlarge(img, factor):
    #Get the dimensions of the image
    dimy, dimx = int(len(img) * factor), int(len(img[0]) *factor)
    return np.zeros(shape=(dimy,dimx ), dtype=np.uint8)

