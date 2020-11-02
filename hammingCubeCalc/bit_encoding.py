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

def build_Q_real_img():
  quadrant = np.zeros((NUM_FREQ,4 + 1))
  Q_real = np.zeros((NUM_FREQ, NUM_X, NUM_Y, BANDS))
  Q_img = np.zeros((NUM_FREQ, NUM_X, NUM_Y, BANDS))
  for val in range(NUM_FREQ):
    real_G_out = real_G_out_arr[val]
    img_G_out = img_G_out_arr[val]
    for i in range(NUM_X):
      for j in range(NUM_Y):
        for k in range(BANDS):
          if img_G_out[i, j, k] >=0 and real_G_out[i, j, k]>=0:
            # I Quadrant
            Q_real[val, i, j, k] = 1
            Q_img[val, i, j, k] = 1
            quadrant[val][0] = 1
          elif img_G_out[i, j, k] <0 and real_G_out[i, j, k]>=0:
            # II Quadrant
            Q_real[val, i, j, k] = 0
            Q_img[val, i, j, k] = 1
            quadrant[val][1] = 1
          elif img_G_out[i, j, k] <0 and real_G_out[i, j, k]<0:
            # III Quadrant
            Q_real[val, i, j, k] = 0
            Q_img[val, i, j, k] = 0
            quadrant[val][2] = 1
          elif img_G_out[i, j, k] >=0 and real_G_out[i, j, k]<0:
            # IV Quadrant
            Q_real[val, i, j, k] = 1
            Q_img[val, i, j, k] = 0
            quadrant[val][3] = 1
          else:
            print(angle)
            quadrant[val][4] = 1

  print(quadrant)
  return (Q_real, Q_img)