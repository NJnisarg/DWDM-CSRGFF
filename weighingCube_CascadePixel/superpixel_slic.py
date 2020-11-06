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

def superpixel_slic(segment_sizes=SEGMENT_SIZES, show_plot=False):

  segment_arr = []
  for numSegments in segment_sizes:
    # apply SLIC and extract (approximately) the supplied number
    # of segments
    segments = slic(reshaped_pca_pines, n_segments = numSegments, sigma = 5)
    segment_arr.append(segments)
    if(show_plot):
    # show the output of SLIC
      fig = plt.figure("Superpixels -- %d segments" % (numSegments))
      ax = fig.add_subplot(1, 1, 1)
      ax.imshow(mark_boundaries(reshaped_pca_pines, segments))
      plt.axis("off")
  # show the plots
  if(show_plot):
    plt.show()
  return segment_arr