#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bowFunctions import *


if __name__ == "__main__":

    detector='SIFT'
    descriptor='SIFT'
    num_samples=50000
    k=32 #num of word bow
    C=1 #regulation factor SVM

    ftrain, ftest='../week1/train/', '../week1/test/'
    pvocabulary="data/vocabulary_{}_{}_{}_{}.centroids.dat".format(detector, descriptor,num_samples,k)
    #Bag of words train images
    pbagOfWordsTrain="data/bagWordsTrain_{}_{}_{}_{}.centroids.dat".format(detector, descriptor,num_samples,k)
    #Bag of words test images
    pbagOfWordsTest="data/bagWordsTest_{}_{}_{}_{}.centroids.dat".format(detector, descriptor,num_samples,k)


    """
      Given the directory fetch paths,
      ids and category of each image
      in train folder
    """
    fileNamesT,filesIdsT,labelsT = prepareFiles(ftrain)
    kptrain,descTrain = getKeypointsDescriptors(fileNamesT,detector,descriptor)

    """
      Build bag of words based on the descriptors, 
      save a file in disk called the value of pvocabulary
      TODO: Check if the file pvocabulary to comment 
      jump the following line
    """
    CB=getAndSaveCodebook(descTrain, num_samples, k, pvocabulary)

    """
      Obtain the vocabulary of the training images
    """
    VW_train=getAndSaveBoVWRepresentation(descTrain,k,CB,pbagOfWordsTrain)


    """
      Given the directory fetch paths,
      ids and category of each image
      in test folder
    """
    filenamesE,filesIdsE,labelsE = prepareFiles(ftest)
    kptest,descTest = getKeypointsDescriptors(filenamesE,detector,descriptor)
    """
      Build bag of words based on the descriptors, 
      save a file in disk called the value of pvocabulary
      TODO: Check if the file pvocabulary to comment 
      jump the following line
    """
    VW_test=getAndSaveBoVWRepresentation(descTest,k,CB,pbagOfWordsTest)

    """
      Train a clasifier SVM with the training images besides assess this using 
      the  image in the set test, Finally returns the accuracy as a measure 
      of the clasifer
    """
    accuracySVM = trainAndTestLinearSVM(VW_train,VW_test,filesIdsT,filesIdsE,C)

    print "Accuracy BOVW: "+str(accuracySVM)

    """
      The regulation factor C is get by cross validation, and returns the accuracy
    """
    # Parémetros para realizar la validación cruzada en el aprendizaje del clasificaro
    # folds: nº de particioines
    # start, end: valor inicial y final del factor de regularización C que se validarán
    # mumparams: nº de valores diferentes para el factor de regularización C entre start y end que se van a validar
    folds=5
    start=0.01
    end=10
    numparams=30
    accuracySVMF = trainAndTestLinearSVM_withfolds(VW_train,VW_test,filesIdsT,filesIdsE,folds,start,end,numparams)
    print "Accuracy BOVWF: "+str(accuracySVMF)

