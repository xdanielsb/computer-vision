import cv2

def get_hu_moments(img):
    """ Get hu moments given an image"""
    res = cv2.HuMoments(cv2.moments(img))
    return res

def get_convex_hull(contourn):
    """ Get convex hull of a given contourn """
    hull = cv2.convexHull(contourn)
    return hull
