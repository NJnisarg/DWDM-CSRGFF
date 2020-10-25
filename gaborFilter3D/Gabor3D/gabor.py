import math
import numpy as np
from mayavi import mlab

def gabor_fn(freq, sigma=10.0, phase=0.0, size=31, psi=0.0):
    coordinates = np.arange(-size, size + 1)
    (z, y, x) = np.meshgrid(coordinates, coordinates, coordinates)

    k = 1 / float((np.power(sigma, 3) * np.power(2*np.pi, 2/3)))

    gb = k * np.exp(-0.5 * ((x**2 + y**2 + z**2)/(sigma ** 2))) * np.cos(2*np.pi*x*freq + psi)

    mlab.contour3d(gb)
    mlab.show()
    return gb

gabor_fn(0.5)
gabor_fn(0.25)
gabor_fn(0.125)
gabor_fn(0.0625)
