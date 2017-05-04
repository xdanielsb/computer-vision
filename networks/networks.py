import cv2
import numpy as np
import math

__author__ = "Daniel Santos"

"""
    Find a set of points near to that point
"""
def get_nearest_points(origin):
    EPS = 0.001
    points = []
    for angle in range(1,360):
        ox, oy = origin
        px, py = ox+EPS, oy

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        points.append([qx,qy])
    return points



def neuronal_network():

    inp = [[0,1], [1,0], [0,0], [1,1]]
    out = [1,1,0,0]
    ##add more points to the calc
    for i in range (0, len(inp)):
        nears = get_nearest_points(inp[i])
        #print(nears)
        inp.extend(nears)

        outs = [out[i]]*len(nears)
        #print ("outs: ", outs)
        out.extend(outs)
        

    inputs= np.array( inp ,dtype="float32")
    targets = np.array(out, dtype="float32")
    salidas = np.array( [0]*len(inputs), dtype="float32")
    layer_sizes = np.array([2,1000,1])


    nnxor = cv2.ANN_MLP(layer_sizes)

    step_size = 0.01
    momentum = 0.0    
    nsteps = 10000
    max_err = 0.0001
    condition = cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS

    print("Inputs: ")
    print(inputs)
    print("Targets: ")
    print(targets)

    criteria = (condition, nsteps, max_err)

    # params is a dictionary with relevant things for NNet training.
    params = dict( term_crit = criteria, 
               train_method = cv2.ANN_MLP_TRAIN_PARAMS_BACKPROP, 
               bp_dw_scale = step_size, 
               bp_moment_scale = momentum )

    num_iters  = nnxor.train(inputs, targets, None, params=params)

    print("Num iterations {}".format(num_iters))

    
    predictions = np.empty_like(salidas)
    nnxor.predict(inputs, predictions)
    sols = []
    accuracy = 0
    for p in range (0, len(predictions)):
        val = int(round(predictions[p]))
        sols.append(val)
        if val == out[p]:
            accuracy += 1

    
    print("Solutions: ")
    print(np.array(sols))
    
    accuracy= (accuracy / len(out)) *100
    print("Accurary: {}%".format(accuracy))
    
    
if __name__ == "__main__":
    points = get_nearest_points([0,1])
    print (len(points))
    neuronal_network()
    



