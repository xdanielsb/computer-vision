import sys
import cv2
import glob
import numpy as np
import cPickle
import time
import random
import scipy.cluster.vq as vq
from sklearn import cross_validation
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA


def prepareFiles(rootpath):
	current_GT_id=0
	filenames=[]
	GT_ids=[]
	GT_labels=[]
	classpath = sorted(glob.glob(rootpath+'*'))
	for i in classpath:
		filespath = sorted(glob.glob(i+'/*.jpg'))
		for j in filespath:
			filenames.append(j)
			GT_ids.append(current_GT_id)
			GT_labels.append(i.split('/')[-1])
		current_GT_id+=1
	return(filenames,GT_ids,GT_labels)

def getKeypointsDescriptors(filenames,detector_type,descriptor_type):
  detector=cv2.xfeatures2d.SIFT_create()
  K=[]
  D=[]
  print 'Extracting Local Descriptors'
  init=time.time()
  for filename in filenames:
	  ima=cv2.imread(filename)
	  gray=cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
	  kpts,des=detector.detectAndCompute(gray,None)
	  K.append(kpts)
	  D.append(des)
  end=time.time()
  print 'Done in '+str(end-init)+' secs.'
  return(K,D)

def getLocalColorDescriptors(filenames, keypoints):
	CD=[]
	area=4
	n_bins=16
	print 'Extracting Local Color Descriptors'
	init=time.time()
	cont=0
	for filename in filenames:
		kpts=keypoints[cont]
		cdesc=np.zeros((len(kpts),n_bins),dtype=np.float32)
		ima=cv2.imread(filename)
		hls=cv2.cvtColor(ima,cv2.COLOR_BGR2HLS)
		hue=hls[:,:,0]
		w,h=hue.shape
		cont2=0
		for k in kpts:
			patch=hue[max(0,k.pt[0] - area*k.size):min(w,k.pt[0] + area*k.size),max(0,k.pt[1] - area*k.size):min(h,k.pt[1] + area*k.size)]
			hist,bin_edges=np.histogram(patch,bins=n_bins,range=(0,180))
			cdesc[cont2,:]=hist
			cont2+=1
		cont+=1
		CD.append(cdesc)
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	return(CD)

def getAndSaveCodebook(descriptors,num_samples,k,filename):
	size_descriptors=descriptors[0].shape[1]
	A=np.zeros((num_samples,size_descriptors),dtype=np.float32)
	for i in range(num_samples):
		A[i,:]=random.choice(random.choice(descriptors))
	print 'Computing kmeans on '+str(num_samples)+' samples with '+str(k)+' centroids'
	init=time.time()
	codebook,v=vq.kmeans(A,k,1)
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	cPickle.dump(codebook, open(filename, "wb"))
	return codebook
																																																									
def getAndSaveBoVWRepresentation(descriptors,k,codebook,filename):
	print 'Extracting visual word representations'
	init=time.time()
	visual_words=np.zeros((len(descriptors),k),dtype=np.float32)
	for i in xrange(len(descriptors)):
		words,distance=vq.vq(descriptors[i],codebook)
		visual_words[i,:]=np.bincount(words,minlength=k)
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	cPickle.dump(visual_words, open(filename, "wb"))
	return visual_words

def getAndSaveBoVW_SPMRepresentation(descriptors,keypoints,k,codebook,filename,files):
	print 'Extracting visual word representations with SPM'
	init=time.time()
	visual_words=np.zeros((len(descriptors),k*21),dtype=np.float32)
	for i in xrange(len(descriptors)):
		ima=cv2.imread(files[i])
		w,h,_=ima.shape
		words,distance=vq.vq(descriptors[i],codebook)
		idx_bin1=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(0*w/2)) & (x[0]<(1*w/2)) & (x[1]>=(0*h/2)) & (x[1]<(1*h/2)) )]
		idx_bin2=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(1*w/2)) & (x[0]<(2*w/2)) & (x[1]>=(0*h/2)) & (x[1]<(1*h/2)) )]
		idx_bin3=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(0*w/2)) & (x[0]<(1*w/2)) & (x[1]>=(1*h/2)) & (x[1]<(2*h/2)) )]
		idx_bin4=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(1*w/2)) & (x[0]<(2*w/2)) & (x[1]>=(1*h/2)) & (x[1]<(2*h/2)) )]

		idx_bin5=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(0*w/4)) & (x[0]<(1*w/4)) & (x[1]>=(0*h/4)) & (x[1]<(1*h/4)) )]
		idx_bin6=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(1*w/4)) & (x[0]<(2*w/4)) & (x[1]>=(0*h/4)) & (x[1]<(1*h/4)) )]
		idx_bin7=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(2*w/4)) & (x[0]<(3*w/4)) & (x[1]>=(0*h/4)) & (x[1]<(1*h/4)) )]
		idx_bin8=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(3*w/4)) & (x[0]<(4*w/4)) & (x[1]>=(0*h/4)) & (x[1]<(1*h/4)) )]

		idx_bin9=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(0*w/4)) & (x[0]<(1*w/4)) & (x[1]>=(1*h/4)) & (x[1]<(2*h/4)) )]
		idx_bin10=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(1*w/4)) & (x[0]<(2*w/4)) & (x[1]>=(1*h/4)) & (x[1]<(2*h/4)) )]
		idx_bin11=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(2*w/4)) & (x[0]<(3*w/4)) & (x[1]>=(1*h/4)) & (x[1]<(2*h/4)) )]
		idx_bin12=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(3*w/4)) & (x[0]<(4*w/4)) & (x[1]>=(1*h/4)) & (x[1]<(2*h/4)) )]

		idx_bin13=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(0*w/4)) & (x[0]<(1*w/4)) & (x[1]>=(2*h/4)) & (x[1]<(3*h/4)) )]
		idx_bin14=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(1*w/4)) & (x[0]<(2*w/4)) & (x[1]>=(2*h/4)) & (x[1]<(3*h/4)) )]
		idx_bin15=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(2*w/4)) & (x[0]<(3*w/4)) & (x[1]>=(2*h/4)) & (x[1]<(3*h/4)) )]
		idx_bin16=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(3*w/4)) & (x[0]<(4*w/4)) & (x[1]>=(2*h/4)) & (x[1]<(3*h/4)) )]

		idx_bin17=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(0*w/4)) & (x[0]<(1*w/4)) & (x[1]>=(3*h/4)) & (x[1]<(4*h/4)) )]
		idx_bin18=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(1*w/4)) & (x[0]<(2*w/4)) & (x[1]>=(3*h/4)) & (x[1]<(4*h/4)) )]
		idx_bin19=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(2*w/4)) & (x[0]<(3*w/4)) & (x[1]>=(3*h/4)) & (x[1]<(4*h/4)) )]
		idx_bin20=[j for j,x in enumerate([keypoints[i][m].pt for m in range(len(keypoints[i]))]) if ((x[0]>=(3*w/4)) & (x[0]<(4*w/4)) & (x[1]>=(3*h/4)) & (x[1]<(4*h/4)) )]


		visual_words[i,:]=np.hstack((np.bincount(words,minlength=k), np.bincount(words[idx_bin1],minlength=k), np.bincount(words[idx_bin2],minlength=k), np.bincount(words[idx_bin3],minlength=k), np.bincount(words[idx_bin4],minlength=k), np.bincount(words[idx_bin5],minlength=k), np.bincount(words[idx_bin6],minlength=k), np.bincount(words[idx_bin7],minlength=k), np.bincount(words[idx_bin8],minlength=k), np.bincount(words[idx_bin9],minlength=k), np.bincount(words[idx_bin10],minlength=k), np.bincount(words[idx_bin11],minlength=k), np.bincount(words[idx_bin12],minlength=k) , np.bincount(words[idx_bin13],minlength=k), np.bincount(words[idx_bin14],minlength=k), np.bincount(words[idx_bin15],minlength=k), np.bincount(words[idx_bin16],minlength=k), np.bincount(words[idx_bin17],minlength=k), np.bincount(words[idx_bin18],minlength=k), np.bincount(words[idx_bin19],minlength=k) , np.bincount(words[idx_bin20],minlength=k)  ))

	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	cPickle.dump(visual_words, open(filename, "wb"))
	return visual_words

def trainAndTestLinearSVM(train,test,GT_train,GT_test,c):
	print 'Training and Testing a linear SVM'
	init=time.time()
	stdSlr = StandardScaler().fit(train)
	train = stdSlr.transform(train)
	clf = svm.SVC(kernel='linear', C=c).fit(train, GT_train)
	accuracy = 100*clf.score(stdSlr.transform(test), GT_test)
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	return accuracy

def trainAndTestLinearSVM_withfolds(train,test,GT_train,GT_test,folds,start,end,numparams):
	print 'Training and Testing a HI SVM'
	init=time.time()
	stdSlr = StandardScaler().fit(train)
	train = stdSlr.transform(train)
	kernelMatrix = histogramIntersection(train, train)
	tuned_parameters = [{'kernel': ['linear'], 'C':np.linspace(start,end,num=numparams)}]
	clf = GridSearchCV(svm.SVC(), tuned_parameters, cv=folds,scoring='accuracy')
	clf.fit(kernelMatrix, GT_train)
	predictMatrix = histogramIntersection(stdSlr.transform(test), train)
	SVMpredictions = clf.predict(predictMatrix)
	correct = sum(1.0 * (SVMpredictions == GT_test))
	accuracy = (correct / len(GT_test))*100
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	return accuracy

def histogramIntersection(M, N):
	m = M.shape[0]
	n = N.shape[0]
	result = np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			temp = np.sum(np.minimum(M[i], N[j]))
			result[i][j] = temp
	return result

def SPMKernel(M, N,k):
	m = M.shape[0]
	n = N.shape[0]

	result = np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			temp = ((.25*np.sum(np.minimum(M[i,0:k], N[j,0:k]))) + (.25*np.sum(np.minimum(M[i,k:k*5], N[j,k:k*5]))) + (.5*np.sum(np.minimum(M[i,k*5:k*21], N[j,k*5:k*21]))))
			result[i][j] = temp
	return result

def trainAndTestHISVM(train,test,GT_train,GT_test,c):
	print 'Training and Testing a HI SVM'
	init=time.time()
	stdSlr = StandardScaler().fit(train)
	train = stdSlr.transform(train)
	kernelMatrix = histogramIntersection(train, train)
	clf = svm.SVC(kernel='precomputed',C=c)
	clf.fit(kernelMatrix, GT_train)
	predictMatrix = histogramIntersection(stdSlr.transform(test), train)
	SVMpredictions = clf.predict(predictMatrix)
	correct = sum(1.0 * (SVMpredictions == GT_test))
	accuracy = correct / len(GT_test)
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	return accuracy

def trainAndTestHISVM_withfolds(train,test,GT_train,GT_test,folds):
	print 'Training and Testing a HI SVM'
	init=time.time()
	stdSlr = StandardScaler().fit(train)
	train = stdSlr.transform(train)
	kernelMatrix = histogramIntersection(train, train)
	tuned_parameters = [{'kernel': ['precomputed'], 'C':np.linspace(0.0001,0.2,num=10)}]
	clf = GridSearchCV(svm.SVC(), tuned_parameters, cv=folds,scoring='accuracy')
	clf.fit(kernelMatrix, GT_train)
	print(clf.best_params_)
	predictMatrix = histogramIntersection(stdSlr.transform(test), train)
	SVMpredictions = clf.predict(predictMatrix)
	correct = sum(1.0 * (SVMpredictions == GT_test))
	accuracy = correct / len(GT_test)
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	return accuracy

def trainAndTestSPMSVM(train,test,GT_train,GT_test,c,k):
	print 'Training and Testing a SPMKernel SVM'
	init=time.time()
	stdSlr = StandardScaler().fit(train)
	train = stdSlr.transform(train)
	kernelMatrix = SPMKernel(train, train,k)
	clf = svm.SVC(kernel='precomputed',C=c)
	clf.fit(kernelMatrix, GT_train)
	predictMatrix =SPMKernel(stdSlr.transform(test), train,k)
	SVMpredictions = clf.predict(predictMatrix)
	correct = sum(1.0 * (SVMpredictions == GT_test))
	accuracy = correct / len(GT_test)
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	return accuracy

def trainAndTestSPMSVM_withfolds(train,test,GT_train,GT_test,k,folds):
	print 'Training and Testing a SPMKernel SVM'
	init=time.time()
	stdSlr = StandardScaler().fit(train)
	train = stdSlr.transform(train)
	kernelMatrix = SPMKernel(train, train,k)
	tuned_parameters = [{'kernel': ['precomputed'], 'C':np.linspace(0.0001,0.2,num=10)}]
	clf = GridSearchCV(svm.SVC(), tuned_parameters, cv=folds,scoring='accuracy')
	clf.fit(kernelMatrix, GT_train)
	print(clf.best_params_)
	predictMatrix =SPMKernel(stdSlr.transform(test), train,k)
	SVMpredictions = clf.predict(predictMatrix)
	correct = sum(1.0 * (SVMpredictions == GT_test))
	accuracy = correct / len(GT_test)
	end=time.time()
	print 'Done in '+str(end-init)+' secs.'
	return accuracy
