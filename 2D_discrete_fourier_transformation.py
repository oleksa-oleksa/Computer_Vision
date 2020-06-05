# my DFT Matrix code from assignment 6
def dft_matrix(n):
    omega = np.exp( - 2 * np.pi * 1J / n )
    W = np.ones((n,n), dtype=complex)
    
    for x in range(n):
        for y in range(n):
             # W = (omega**(j*k)) / sqrt(N) where j, k= 0..N-1
            W[x, y] = omega**(x*y)
    return W / np.sqrt(n) 

# new code for inverse DFT Matrix
def dft_inverse(n):
    omega = np.exp(2 * np.pi * 1J / n )
    W = np.ones((n,n), dtype=complex)
    
    for x in range(n):
        for y in range(n):
             # W = (omega**(j*k)) / sqrt(N) where j, k= 0..N-1
            W[x, y] = omega**(x*y)
    return W / n 

def dft2d(img):
    """
    Returns the 2d discrete fourier transformation
    """
    # your code here
    # die Dft Matrix braucht nur so viele Spalten, wie das Bild Reihen hat
    size = max(img.shape[0],img.shape[0])
    #size = max(img.shape[0], img.shape[0])

    W = dft_matrix(img.shape[0])
    W2 = dft_matrix(img.shape[1])
    
    dft = np.dot(W, img)
    dft2d = np.dot(dft, W2)
    return dft2d
    
    # check solution with numpy
    #return numpy_fft2(img)

def inv_dft2d(x):
    """
    Returns the 2d inverse discrete fourier transformation
    """
    # your code here
    #size = max(x.shape[0],x.shape[0])
    #size = max(img.shape[0], img.shape[0])

    W_inv = dft_inverse(x.shape[0])
    W_inv2 = dft_inverse(x.shape[1])
    
    dft_inv = np.dot(W_inv, x)
    dft2d_inv = np.dot(dft_inv, W_inv2)
    return dft2d_inv
    
    # check solution with numpy
    #return numpy_ifft2(x)


def chess_board(n=8, field_size=32):
    board = np.zeros((n*field_size, n*field_size))
    s = field_size
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i*s:(i+1)*s, j*s:(j+1)*s] = 1
    return board

# plot all functions: chess board, dft2d and inverse 
plt.subplot(321)
plt.imshow(np.real(chess_board()), cmap='gray')
plt.subplot(322)
plt.imshow(np.imag(chess_board()), cmap='gray')
plt.subplot(323)
plt.imshow(np.real(dft2d(chess_board())), cmap='gray')
plt.subplot(324)
plt.imshow(np.imag(dft2d(chess_board())), cmap='gray')
plt.subplot(325)
plt.imshow(np.real(inv_dft2d(dft2d(chess_board()))), cmap='gray')
plt.subplot(326)
plt.imshow(np.imag(inv_dft2d(dft2d(chess_board()))), cmap='gray')
plt.show