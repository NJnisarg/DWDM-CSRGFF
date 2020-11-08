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

def scale_data(corrected_pines):
  scaled_data = np.zeros((NUM_X, NUM_Y, BANDS))
  for i in range(NUM_X):
    for j in range(NUM_Y):
      mn = 0
      sd = 0
      for k in range(BANDS):
        mn += corrected_pines[i][j][k]
      mn/=BANDS

      for k in range(BANDS):
        sd += ((corrected_pines[i][j][k] - mn)**2)
      sd/=BANDS
      sd = math.sqrt(sd)

      for k in range(BANDS):
        sd += ((corrected_pines[i][j][k] - mn)**2)
      sd/=BANDS
      sd = math.sqrt(sd)

      for k in range(BANDS):  
        scaled_data[i][j][k] = (corrected_pines[i][j][k] - mn)/sd
  
  return scaled_data


corrected_pines = scale_data(corrected_pines)