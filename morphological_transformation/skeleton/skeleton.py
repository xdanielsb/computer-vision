import cv2
from matplotlib import pyplot as plt
"""
    Reference http://felix.abecassis.me/2011/09/opencv-morphological-skeleton/
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)

def get_structure(name="rectangular"):
    # Rectangular Kernel
    if name == "rectangular":
        return cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    if name == "elliptical":
        return cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    if name == "cross-shaped":
        return cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
    print ("write a valid name\n")

def skeleton(img, num_iter=1):
    s1 = get_structure()
    result_er = cv2.erode(img, s1, iterations  = num_iter)
    result = cv2.morphologyEx(result_er, cv2.MORPH_OPEN, s1)
    plt.subplot(1,3,1), plt.imshow(img, cmap="gray"), plt.title("Real Image")
    plt.subplot(1,3,2), plt.imshow(result_er, cmap="gray"), plt.title("Erosions Image")
    plt.subplot(1,3,3), plt.imshow(result, cmap="gray"), plt.title("Skeleton Image")
    plt.show()

if __name__ == "__main__":
    img = readi("../../assets/images/letterB.png", "gray")
    skeleton(img,4)

