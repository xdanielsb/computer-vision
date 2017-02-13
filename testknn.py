from knn.from_scratch_knn import *

if (__name__ == "__main__"):

    #All the sample
    data = load_data_set("datasets/flowers.csv")
    
    #The training set is going to be the 99 %
    training_set = get_training_set(0.99, data)

    #The test set
    test_set = get_test_set(training_set, data) 
    
    

    k= 3
    #This columns are the selected features  for doing the euclidean distance.
    #columns = ["a", "b", "c", "d"]
    columns = ["a", "b"]
    predictions = knn(training_set, test_set, k, columns)
    for predict in predictions:
        print("Data to  predict")
        
        id_to = predict[0]
        k_nearest = predict[1]
        print (data.loc[id_to])
        print("\n")
        
        
        
        print ("\tK-nearest-neighbors")
        for n in k_nearest:
            distance = n[0]
            id_neigh = n[1]
            print ("Distance to the neighbor {} is {} ".format(n[1], n[0]))
            #print (data.loc[id_neigh])
            #print()


