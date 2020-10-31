import math
import random
import scipy.io as scio
import numpy as np
import scipy.ndimage as scnd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from skimage.segmentation import mark_boundaries
from skimage.segmentation import slic

NUM_X = 145
NUM_Y = 145
IMG_SIZE = 130*130
CLASSES = 16
BANDS = 200
FREQ = np.array([0.5,0.25,0.125,0.0625])
NUM_FREQ = (FREQ.shape)[0]
SEGMENT_SIZES = np.array([50,100,150,200,250,300,350,400,450,500]) # In steps of 50

def build_svm(train_test_set, M_feat_arr, gt, idx):
  svc = SVC(kernel='rbf', decision_function_shape='ovo')
  num_samples = np.count_nonzero(train_test_set == 1)
  ctr = 0
  train_X = np.zeros((num_samples, BANDS))
  train_Y = np.zeros((num_samples))
  for i in range(NUM_X):
    for j in range(NUM_Y):
      if(train_test_set[i][j] == 1):
        train_X[ctr] = nonscaled_data[i][j] # M_feat_arr[idx][i][j]
        train_Y[ctr] = gt[i][j]
        ctr+=1
  svc.fit(train_X, train_Y)
  return svc

  svc_arr = np.array([build_svm(train_test_set, M_feat_arr, gt, x) for x in range(NUM_FREQ)])

  def test_svm(train_test_set, M_feat_arr, gt, idx, svc):
  num_samples = NUM_X*NUM_Y - np.count_nonzero(train_test_set == 1)
  ctr = 0
  test_X = np.zeros((num_samples, BANDS))
  test_Y = np.zeros((num_samples))
  for i in range(NUM_X):
    for j in range(NUM_Y):
      if(train_test_set[i][j] == 0):
        test_X[ctr] = nonscaled_data[i][j]
        test_Y[ctr] = gt[i][j]
        ctr+=1
  acc = svc.score(test_X, test_Y)
  return acc

  test_svm(train_test_set, M_feat_arr, gt, 0, svc_arr[0])