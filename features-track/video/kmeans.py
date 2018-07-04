
def kmeans_init(points):
    num_iterations = 10
    epsilon = 0.1
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, num_iterations, epsilon)
    flags = cv2.KMEANS_RANDOM_CENTERS)
    #Apply kmeans
    compactness,labels,centers = cv2.kmeans(points,2,None,criteria,10,flags)
