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

plot_G_out = real_G_out_arr[1]
maxx = plot_G_out.max()
minn = plot_G_out.min()
for i in range(plot_G_out.shape[0]):
  for j in range(plot_G_out.shape[1]):
    for k in range(plot_G_out.shape[2]):
      plot_G_out[i, j, k] = (plot_G_out[i, j, k] - minn)/(maxx - minn)

fig = plt.figure(figsize = (12, 12))
fig.suptitle('Convolution with Gabor Filter of Frequ 0.25', fontsize=20)
for i in range(1, 1+9):
    fig.add_subplot(3,3, i)
    band = np.random.randint(plot_G_out.shape[2])
    plt.imshow(plot_G_out[:,:,band], cmap='nipy_spectral')
    plt.axis('off')
    plt.title(f'Band - {band}')


real_G_out_arr = np.array([scnd.convolve(corrected_pines, real_gabor_arr[x]) for x in range(NUM_FREQ)])
img_G_out_arr = np.array([scnd.convolve(corrected_pines, img_gabor_arr[x]) for x in range(NUM_FREQ)])

img_G_out_arr = np.array([scnd.convolve(corrected_pines, img_gabor_arr[x]) for x in range(NUM_FREQ)])

real_sqr = np.array([ np.square(real_G_out_arr[x]) for x in range(NUM_FREQ)])
img_sqr = np.array([ np.square(img_G_out_arr[x]) for x in range(NUM_FREQ)])

# We will use this in the Confidence Cube Calculation
M_feat_arr = np.array([ np.sqrt( real_sqr[x] + img_sqr[x] ) for x in range(NUM_FREQ)]) 