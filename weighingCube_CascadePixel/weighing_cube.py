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

def get_weighing_cube(C,H):
  W = np.zeros((NUM_X, NUM_Y, CLASSES))
  for i in range(NUM_FREQ):
    W += C[i] - H[i]
  return W

weighing_cube = get_weighing_cube(confidence_cube_arr, hamming_cube_arr)