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

predicted_classes = np.zeros((NUM_X, NUM_Y))
for i in range(NUM_X):
  for j in range(NUM_Y):
    predicted_classes[i][j] = np.argmax(Z[i][j])

num_true = 0
for i in range(NUM_X):
  for j in range(NUM_Y):
    if(gt[i][j] == predicted_classes[i][j]):
      num_true+=1

print(num_true/IMG_SIZE)