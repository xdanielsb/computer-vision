
"""
    Neighbors for creating the average.
    -2,-2	-1,-2	0,-2	1,-2	2,-2
    -2,-1	-1,-1	0,-1	1,-1	2,-1
    -2,0	-1,0	0,0	1,0	2,0
    -2,1	-1,1	0,1	1,1	2,1
    -2,2	-1,2	0,2	1,2	2,2

    @param
    img ---> images
    x   ---> pos x in the image
    y   ---> pos y in the image
    
    @return
    The value of the pixel using bicubic interpolation
"""
def get_bicubic_pixel(img, x, y):
    dimy, dimx = img.shape[1] -2, img.shape[0] -2

    #Cuantizar
    x = (x // factor) % dimx
    y = (y // factor) % dimy

    #Expresion of the neighbors
    #First neihbors
    directions = [ [-1,0], [1,0], [0,-1], [0,1], [1,1], [-1,-1], [1,-1], [-1,1]]
    directions.extend([[-2,2], [-2,-1],[-2,0],[-2,1],[-2,2],[-1,-2],[0,-2],[1,-2],[2,-2],[2,-1],[2,0],[2,1],[2,2],[-1,2],[0,2],[1,2]])
    suma = 0
    for d in directions:
        ##Check all the borders
        suma += int(img[int(x+d[0])][int(y+d[1])])

    return suma // len(directions);

