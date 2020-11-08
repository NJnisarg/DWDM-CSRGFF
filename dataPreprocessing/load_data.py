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

nonscaled_data = scio.loadmat('Indian_pines_corrected.mat').get('indian_pines_corrected')
corrected_pines = scio.loadmat('Indian_pines_corrected.mat')
corrected_pines = np.array(corrected_pines.get('indian_pines_corrected'))

gt = scio.loadmat('Indian_pines_gt.mat')
gt = np.array(gt.get('indian_pines_gt'))

fig = plt.figure(figsize = (12, 12))

for i in range(1, 1+9):
    fig.add_subplot(3,3, i)
    band = np.random.randint(nonscaled_data.shape[2])
    plt.imshow(nonscaled_data[:,:,band], cmap='nipy_spectral')
    plt.axis('off')
    plt.title(f'Band - {band}')

hash = {}
for i in range(145):
  for j in range(145):
    if hash.get(gt[i, j]) is None:
      hash[gt[i, j]] = 1
    else:
      hash[gt[i, j]] = hash[gt[i, j]] + 1

x = []
y = []
for key in sorted(hash):
  x.append(int(key))
  y.append(int(hash[key]))

plt.bar(x,y,align='center') # A bar chart
plt.xlabel('Class Labels')
plt.ylabel('Frequency')
plt.show()