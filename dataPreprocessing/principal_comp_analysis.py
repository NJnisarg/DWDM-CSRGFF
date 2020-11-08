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

d2_pines = corrected_pines.reshape(-1, corrected_pines.shape[2])

pca = PCA(n_components = 3)
pca_pines = pca.fit_transform(d2_pines)

maxx = pca_pines.max()
minn = pca_pines.min()
for i in range(pca_pines.shape[0]):
  for j in range(pca_pines.shape[1]):
    pca_pines[i, j] = (pca_pines[i, j] - minn)/(maxx - minn)
  
print(pca_pines.shape)

reshaped_pca_pines = np.reshape(pca_pines, (145, 145, 3))
print(reshaped_pca_pines.shape)
