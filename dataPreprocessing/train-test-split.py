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

def get_train_test_idx(gt):

  train_test_set = np.zeros(gt.shape)

  samples_per_class = 15
  pixel_to_class_map = [[] for x in range(CLASSES)]
  training_class_list = [[] for x in range(CLASSES)]
  for c in range(CLASSES):
    num_samples = 0
    for i in range(NUM_X):
      for j in range(NUM_Y):
        if(gt[i][j] == c):
          num_samples += 1
          pixel_to_class_map[c].append((i,j))
    
    class_list = random.sample(pixel_to_class_map[c], int(samples_per_class))
    training_class_list[c] = class_list
    for (x,y) in class_list:
      train_test_set[x][y] = 1  

  return (train_test_set,training_class_list)

train_test_set,training_class_list = get_train_test_idx(gt)