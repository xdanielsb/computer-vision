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