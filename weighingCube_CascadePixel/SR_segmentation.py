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

def get_s_graph(segments, nC):
  s_graph = [[] for x in range(nC)]

  for i in range(NUM_X):
    for j in range(NUM_Y):
      try:
        s_graph[segments[i][j]].append((i,j))
      except:
        print("err")
        print(segments[i][j])
        print(nC)
  return s_graph

def SR(gt, train_test_set, s_graph, W, K):
  U = np.zeros((NUM_X, NUM_Y, CLASSES))
  for i in range(K):
    sk = s_graph[i]
    num_common_samples = 0
    common_samples = []

    # Num of common samples
    for (x,y) in sk:
      if(train_test_set[x][y] == 1):
          num_common_samples += 1
          common_samples.append((x,y))
    
    if(num_common_samples == 1):
      u = np.zeros((CLASSES))
      c = gt[common_samples[0][0]][common_samples[0][1]]
      u[c] = 1

      for (x,y) in sk:
        U[x][y] = u
    else:
      mn = 0
      num_samples = 0
      for (x,y) in sk:
        num_samples += 1
        for c in range(CLASSES):
          mn += W[x][y][c]

        mn = mn/CLASSES
        U[x][y] = np.array([mn/num_samples for x in range(CLASSES)])

  
  return U


Z = np.zeros((NUM_X, NUM_Y, CLASSES))
segment_arr = superpixel_slic(SEGMENT_SIZES, True)
for i in range(len(segment_arr)):

  mx = np.max(segment_arr[i])
  s_graph = get_s_graph(segment_arr[i], mx+1)
  Z += SR(gt, train_test_set, s_graph, weighing_cube, mx+1)