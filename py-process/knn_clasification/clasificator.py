
# Importamos las librerias necesarias para trabajar
import cv2
import numpy as np
from matplotlib import pyplot as plt
from decimal import *
import math
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.colors as mcolors


# -----------------------------------------
#              VARIABLES GLOBALES
# -----------------------------------------

# Conjunto de datos para entretar el clasificador y Conjunto de clases a las cuales pertenecen los datos
samples = np.float32( [[50, 25],[25,75],[75,75] ] )
responses = np.float32( [0, 1, 2] )

# Paso de muestreo
h = 0.2

# -----------------------------------------
#            PROGRAMA PRINCIPAL
# -----------------------------------------


# Creamos el clasificador KNN y lo entrenamos con la muestra que tenemos
KNN_Classifier = cv2.KNearest()
KNN_Classifier.train( samples, responses )

# Definimos nuestra paleta de colores, para graficar, en este caso escogemos los colores en RGB uno para cada clase
cmap_light = mcolors.ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold  = mcolors.ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# Creamos dos arreglos de valores de 0 a 100 con un paso de 0.2 tanto en X como en Y
xx, yy = np.meshgrid( np.arange( 0, 100, h ), np.arange( 0, 100, h ) )

# Encontramos a que clase pertenecen con KNN.find_nearest
retval, results, neigh_resp, dists = KNN_Classifier.find_nearest(  np.float32( np.c_[xx.ravel(), yy.ravel()] ), 1)
results = results.reshape( xx.shape )

# Graficamos para observar los resultados obtenidos
plt.figure()
plt.pcolormesh( xx, yy, results, cmap = cmap_light )

plt.scatter( samples[:,0], samples[:,1], c = responses, cmap = cmap_bold)
plt.xlim( xx.min(), xx.max())
plt.show()

