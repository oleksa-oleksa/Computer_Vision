def dct1d(line):
    """
    Returns the discrete cosine transformation
    https://en.wikipedia.org/wiki/Discrete_cosine_transform#DCT-II
    """
    N = len(line)
    result = np.zeros(N, dtype=float)
    
    ns = np.arange(N)
    for k in range(N):
        result[k] = np.sum(line[ns]*np.cos((np.pi*(ns+0.5)*k)/N))
        
    return result

def dct2d(img):
    """
    Returns the 2d discrete cosine transformation
    https://en.wikipedia.org/wiki/Discrete_cosine_transform#M-D_DCT-II
    """
    # your code here
    N1 = img.shape[0]
    N2 = img.shape[1]
    first = np.ones([N1, N2], dtype=float)
    second = np.ones([N1, N2], dtype=float)
      
    # the one-dimensional DCT-II performed along the rows
    first = np.apply_along_axis(dct1d, 0, img)
    # along the columns
    second = np.apply_along_axis(dct1d, 1, first)
    # print("debug")
    return second
 

def inv_dct1d(line):

    N = len(line)
    result = np.zeros(N, dtype=float)
    
    ns = np.arange(1, N)
    for k in range(N):
        result[k] = (0.5 * line[0]) + np.sum(line[ns]*np.cos((np.pi*(k+0.5)*ns)/N))
        
    return result 
    
    
def inv_dct2d(x):
    """
    Returns the 2d inverse discrete cosine transformation
    The inverse of DCT-II is DCT-III multiplied by 2/N an
    """
    # your code here
    N1 = x.shape[0]
    N2 = x.shape[1]
    first = np.ones([N1, N2], dtype=float)
    second = np.ones([N1, N2], dtype=float)
      
    first = np.apply_along_axis(inv_dct1d, 0, x)
    second = np.apply_along_axis(inv_dct1d, 1, first)
    return second

def chess_board(n=8, field_size=32):
    board = np.zeros((n*field_size, n*field_size))
    s = field_size
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i*s:(i+1)*s, j*s:(j+1)*s] = 1
    return board



for pic in [chess_board(), rgb2gray(chelsea())/255]:
    #plt.imshow(dct2d(pic), cmap='gray')
    plt.imshow(inv_dct2d(dct2d(pic)), cmap='gray')
    plt.show()