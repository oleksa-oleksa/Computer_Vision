import numpy as np
import matplotlib.pyplot as plt
import pylab

def dft_matrix(n):
    """
    Implement the Discrete Fourier Transformation with Matrix Multiplication.
    Returns the Discrete Fourier Transformation Matrix of order `n`.
    """
    # your code here
    
    # we can use j as in Matlab to work with complex numbers
    # Wiki: where omega = e**(-2*pi*i/N) is a primitive Nth root of unity in which i**2= -1
    omega = np.exp( - 2 * np.pi * 1J / n )
    
    W = np.ones((n,n), dtype=complex)
    
    for x in range(n):
        for y in range(n):
             # W = (omega**(j*k)) / sqrt(N) where j, k= 0..N-1
            W[x, y] = omega**(x*y)
    return W / np.sqrt(n) 

# got error: Image data of dtype complex128 cannot be converted to float
# ====> plot separately the imag and real part
# https://numpy.org/doc/stable/reference/generated/numpy.real.html
dft_16 = dft_matrix(16)

# sublot with 2 rows and 2 columns
# https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
plt.subplot(221).set_title("16 Real")
plt.imshow(dft_16.real, cmap='jet', interpolation='nearest')
plt.subplot(222).set_title("16 Imag")
plt.imshow(dft_16.imag, cmap='jet', interpolation='nearest')

dft_32 = dft_matrix(32)

plt.subplot(223).set_title("32 Real")
plt.imshow(dft_32.real, cmap='jet', interpolation='nearest')
plt.subplot(224).set_title("32 Imag")
plt.imshow(dft_32.imag, cmap='jet', interpolation='nearest')
plt.show()

#------------
dft_256 = dft_matrix(256)

plt.subplot(121)
plt.imshow(dft_256.real, cmap='jet', interpolation='nearest')
plt.subplot(122)
plt.imshow(dft_256.imag, cmap='jet', interpolation='nearest')
plt.show()

dft_512 = dft_matrix(512)

plt.subplot(121)
plt.imshow(dft_512.real, cmap='jet', interpolation='nearest')
plt.subplot(122)
plt.imshow(dft_512.imag, cmap='jet', interpolation='nearest')
plt.show()