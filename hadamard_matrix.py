import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy.linalg
from skimage.color import rgb2gray
from skimage.data import chelsea
from scipy.fftpack import dct, idct
from numpy.fft import fft2 as numpy_fft2

pylab.rcParams['figure.figsize'] = (12, 12)   # This makes the plot bigger


import math

def hadamard_matrix(n):
    """Returns the Hadamard matrix. N is a power of two.
    Hadamard matrix Hn is a n × n matrix (scaled by a normalization factor) can be defined recursively, 
    or by using the binary (base-2) representation exist only for n = 1, n = 2, or n = 4k, with k ∈ N"""
    # your code here
    
    if not math.log(n, 2).is_integer(): 
        print("ValueError: n must be an positive integer, and n must be a power of 2")
        return

    H1 = 1
    H_total = np.zeros((n, n))
    for i in range(n):
        for x in range(2):
            for y in range(2):
                
    
    return scipy.linalg.hadamard(n) / np.sqrt(n)

plt.subplot(121)
plt.imshow(hadamard_matrix(2), cmap='gray')
plt.subplot(122)
plt.imshow(hadamard_matrix(32), cmap='gray')
plt.show()