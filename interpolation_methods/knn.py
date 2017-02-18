"""
    Neighbors for creating the average.
    -1,-1	0,-1	1,-1
    -1,0	0,0	1,0
    -1,1	0,1	1,1

    @param
    img ---> images
    x   ---> pos x in the image
    y   ---> pos y in the image
    
    @return
    The value of the pixel using k-nearest-neighbor interpolation

"""

def get_near_neighbor_pixel(img, x,y, factor):
    dimy, dimx = img.shape[1] -1, img.shape[0] -1

    #Cuantizar
    x = (x // factor) % dimx
    y = (y // factor) % dimy

    #Expresion of the neighbors
    directions = [ [-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1], [1,-1], [-1,1]]
    
    vecinos = []
    for d in directions:
        ##Check all the borders
        vecinos.append(img[int(x+d[0])][int(y+d[1])])
    
    #Criteria, select the bigger
    return vecinos[-1];
