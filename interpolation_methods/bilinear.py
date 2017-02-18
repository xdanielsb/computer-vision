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
    The value of the pixel using bilinear interpolation
"""
def getBilinearPixel(img, x,y):
    dimy, dimx = img.shape[1] -1, img.shape[0] -1

    #Cuantizar
    x = (x // factor) % dimx
    y = (y // factor) % dimy

    #Expresion of the neighbors
    directions = [ [-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1], [1,-1], [-1,1]]
    
    suma = 0
    for d in directions:
        ##Check all the borders
        suma += int(img[int(x+d[0])][int(y+d[1])])

    return suma // len(directions);


