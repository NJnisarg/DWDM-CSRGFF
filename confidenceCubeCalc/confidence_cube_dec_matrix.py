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

def get_decision_matrix(decision_fn_res):

    decision_matrix = np.zeros((CLASSES, CLASSES))
    counter = 0
    for i in range(0,CLASSES):
        for j in range(i+1, CLASSES):
            decision_matrix[i][j] = abs(decision_fn_res[0][counter])
            decision_matrix[j][i] = abs(decision_fn_res[0][counter])
            counter+=1

    return decision_matrix

def get_confidence_score(decision_matrix, cls):
  nc_arr = np.count_nonzero(decision_matrix != 0, axis = 1) # axis=1 gives the count per row.
  nc = nc_arr[cls]
  score = 0
  val = 0
  for i in range(NUM_FREQ):
    for j in range(CLASSES):
      val += decision_matrix[cls][j]
    val = val/(2*nc)
    score = val + (math.sqrt(nc)/(2 * CLASSES))
  return score

def get_confidence_cube():
  confidence_cube_arr = np.zeros((NUM_FREQ,NUM_X,NUM_Y,CLASSES))
  for i in range(0,NUM_FREQ):
    svc = svc_arr[i]

    ctr = 0
    num_samples = NUM_X*NUM_Y
    test_X = np.zeros((num_samples, BANDS))
    test_Y = np.zeros((num_samples))
    for j in range(NUM_X):
      for k in range(NUM_Y):
        if(train_test_set[i][j] == 0):
          test_X[ctr] = M_feat_arr[i][j][k]
          test_Y[ctr] = gt[j][k]
          ctr+=1
    ctr = 0
    for j in range(0,NUM_X):
      for k in range(0,NUM_Y):
        decision_fn_res = svc.decision_function(np.array([test_X[ctr]])) # For a single Pixel
        decision_matrix = get_decision_matrix(decision_fn_res)
        ctr+=1
        for c in range(0,CLASSES):
          confidence_cube_arr[i][j][k][c] = get_confidence_score(decision_matrix, c)

  return confidence_cube_arr


confidence_cube_arr = get_confidence_cube()