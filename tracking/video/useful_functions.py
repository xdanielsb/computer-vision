import cv2
import numpy as np

def get_hu_moments(img):
    """ Get hu moments given an image"""
    res = cv2.HuMoments(cv2.moments(img))
    return res

def get_convex_hull(contourn):
    """ Get convex hull of a given contourn """
    hull = cv2.convexHull(contourn)
    return hull


def min_rect(contourn):
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    #cv2.drawContours(img,[box],0,(0,0,255),2)
    return box


def find_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    return contours


def draw_contours(img, contours):
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    return img


def draw_convex_hull(img, hull):
    num_points = len(hull)
    for i in range (0,num_points):
        start = hull[i %num_points]
        end = hull[(i+1)%num_points]

        cv2.line(img, (start[0][0], start[0][1]),(end[0][0], end[0][1]),[0,255,0],2)
