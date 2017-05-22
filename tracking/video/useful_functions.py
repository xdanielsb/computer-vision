import cv2

def get_hu_moments(img):
    """ Get hu moments given an image"""
    res = cv2.HuMoments(cv2.moments(img))
    return res
