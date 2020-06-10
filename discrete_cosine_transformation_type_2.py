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
 

