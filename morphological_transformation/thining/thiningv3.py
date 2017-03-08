#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:43:08 2017
@author: jcamox

Algoritmo Moforlógico de Adelgazamiento
"""
#Algoritmo Moforlógico de Adelgazamiento

import math
import numpy as np
import cv2

from matplotlib import pyplot as plt

img_color = cv2.imread('../../assets/images/hand.jpg',1)
img_median = cv2.imread('../../assets/images/hand.jpg',0)

ret,img_bin = cv2.threshold(img_median,50,255, cv2.THRESH_BINARY_INV)

cv2.imshow('Imagen Original', img_median)
cv2.imshow('Imagen Umbral Binario', img_bin)


B1_hit = np.array([ [0,0,0], 
                    [0,1,0], 
                    [1,1,1] ], 'uint8')
B1_miss = np.array([ [1,1,1],
                     [0,0,0], 
                     [0,0,0] ], 'uint8')

B2_hit = np.array([ [0,0,0], 
                    [1,1,0], 
                    [1,1,0] ], 'uint8')

B2_miss = np.array([ [0,1,1], [0,0,1], [0,0,0] ], 'uint8')

B3_hit = np.array([ [1,0,0], [1,1,0], [1,0,0] ], 'uint8')
B3_miss = np.array([ [0,0,1], [0,0,1], [0,0,1] ], 'uint8')

B4_hit = np.array([ [1,1,0], [1,1,0], [0,0,0] ], 'uint8')
B4_miss = np.array([ [0,0,0], [0,0,1], [0,1,1] ], 'uint8')

B5_hit = np.array([ [1,1,1], [0,1,0], [0,0,0] ], 'uint8')
B5_miss = np.array([ [0,0,0], [0,0,0], [1,1,1] ], 'uint8')

B6_hit = np.array([ [0,1,1], [0,1,1], [0,0,0] ], 'uint8')
B6_miss = np.array([ [0,0,0], [1,0,0], [1,1,0] ], 'uint8')

B7_hit = np.array([ [0,0,1], [0,1,1], [0,0,1] ], 'uint8')
B7_miss = np.array([ [1,0,0], [1,0,0], [1,0,0] ], 'uint8')

B8_hit = np.array([ [0,0,0], [0,1,1], [0,1,1] ], 'uint8')
B8_miss = np.array([ [1,1,0], [1,0,0], [0,0,0] ], 'uint8')


# Inicializacion
i = 0
iterations = 57

img_2erode = img_bin

while i <= iterations:
    
    #Complemento de la imagen
    img_2erode_c = 255 - img_2erode
    

    # -- Transformada Hit-or-Miss --
    #B1
    ero_B1_hit = cv2.erode(img_2erode, B1_hit, iterations = 1)
    ero_B1_miss = cv2.erode(img_2erode_c, B1_miss, iterations = 1)
    T_HoM_1 = cv2.bitwise_and(ero_B1_hit, ero_B1_miss)
    
    
    adelgazado_B1 = img_2erode - T_HoM_1
    adelgazado_B1_c = 255 - adelgazado_B1 #complemento
    
    #B2
    ero_B2_hit = cv2.erode(adelgazado_B1, B2_hit, iterations = 1)
    ero_B2_miss = cv2.erode(adelgazado_B1_c, B2_miss, iterations = 1)
    T_HoM_2 = cv2.bitwise_and(ero_B2_hit, ero_B2_miss)
    
    adelgazado_B2 = adelgazado_B1 - T_HoM_2
    adelgazado_B2_c = 255 - adelgazado_B2 #complemento
    
    #B3
    ero_B3_hit = cv2.erode(adelgazado_B2, B3_hit, iterations = 1)
    ero_B3_miss = cv2.erode(adelgazado_B2_c, B3_miss, iterations = 1)
    T_HoM_3 = cv2.bitwise_and(ero_B3_hit, ero_B3_miss)
    
    adelgazado_B3 = adelgazado_B2 - T_HoM_3
    adelgazado_B3_c = 255 - adelgazado_B3 #complemento
    
    #B4
    ero_B4_hit = cv2.erode(adelgazado_B3, B4_hit, iterations = 1)
    ero_B4_miss = cv2.erode(adelgazado_B3_c, B4_miss, iterations = 1)
    T_HoM_4 = cv2.bitwise_and(ero_B4_hit, ero_B4_miss)
    
    adelgazado_B4 = adelgazado_B3 - T_HoM_4
    adelgazado_B4_c = 255 - adelgazado_B4 #complemento
    
    #B5
    ero_B5_hit = cv2.erode(adelgazado_B4, B5_hit, iterations = 1)
    ero_B5_miss = cv2.erode(adelgazado_B4_c, B5_miss, iterations = 1)
    T_HoM_5 = cv2.bitwise_and(ero_B5_hit, ero_B5_miss)
    
    adelgazado_B5 = adelgazado_B4 - T_HoM_5
    adelgazado_B5_c = 255 - adelgazado_B5 #complemento
    
    #B6
    ero_B6_hit = cv2.erode(adelgazado_B5, B6_hit, iterations = 1)
    ero_B6_miss = cv2.erode(adelgazado_B5_c, B6_miss, iterations = 1)
    T_HoM_6 = cv2.bitwise_and(ero_B6_hit, ero_B6_miss)
    
    adelgazado_B6 = adelgazado_B5 - T_HoM_6
    adelgazado_B6_c = 255 - adelgazado_B6 #complemento
    
    #B7
    ero_B7_hit = cv2.erode(adelgazado_B6, B7_hit, iterations = 1)
    ero_B7_miss = cv2.erode(adelgazado_B6_c, B7_miss, iterations = 1)
    T_HoM_7 = cv2.bitwise_and(ero_B7_hit, ero_B7_miss)
    
    adelgazado_B7 = adelgazado_B6 - T_HoM_7
    adelgazado_B7_c = 255 - adelgazado_B7 #complemento
    
    #B8
    ero_B8_hit = cv2.erode(adelgazado_B7, B8_hit, iterations = 1)
    ero_B8_miss = cv2.erode(adelgazado_B7_c, B8_miss, iterations = 1)
    T_HoM_8 = cv2.bitwise_and(ero_B8_hit, ero_B8_miss)
    
    adelgazado_B8 = adelgazado_B7 - T_HoM_8
    adelgazado_B8_c = 255 - adelgazado_B8 #complemento
    
    img_2erode = adelgazado_B8
    
    i += 1

cv2.imshow('Adelgazado', img_2erode)
#cv2.imshow('v', verifying)



k = cv2.waitKey(0) & 0xFF
# ------ -----  PRESS ESC ----- TO EXIT -------
if k == 27:
    cv2.destroyAllWindows()


