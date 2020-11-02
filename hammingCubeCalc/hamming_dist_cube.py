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

def hamming_distance(Re_pp, Img_pp, Re_qq, Img_qq):
  h = 0.0
  for z in range(BANDS):
    h += (int(Re_pp[z])^int(Re_qq[z]) + int(Img_pp[z])^int(Img_qq[z]))
  h /= (2*BANDS)
  return h

def get_hamming_cube():
  hamming_dist_arr = np.zeros((NUM_FREQ, NUM_X, NUM_Y, CLASSES))
  for val in range(NUM_FREQ):
    Q_real = Q_real_arr[val]
    Q_img = Q_img_arr[val]
    for i in range(NUM_X):
      for j in range(NUM_Y):
        Re_pp = Q_real[i, j]
        Img_pp = Q_img[i, j]
        for c in range(CLASSES):
          h_min = 1.0
          for (x,y) in training_class_list[c]:
            Re_qq = Q_real[x, y]
            Img_qq = Q_img[x, y]
            h_min = min(h_min, hamming_distance(Re_pp, Img_pp, Re_qq, Img_qq))
          hamming_dist_arr[val, i, j, c] = h_min
  return hamming_dist_arr

hamming_cube_arr = get_hamming_cube()