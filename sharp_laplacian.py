def sharp_laplacian(img):
    """Perform sharpening with a laplacian filter"""
    # your code here
    # PAGE 310 in Image Processing Book 
    # f (x + 1, y ) + f (x − 1, y ) + f (x , y + 1) + f (x , y − 1) − 4f (x , y )
    kernel1 = np.array(
    [[0, 1, 0],
     [1, -4, 1],
     [0, 1, 0]])
    
    kernel = np.array(
    [[-1,-1,-1],
     [-1,8,-1],
     [-1,-1,-1]
    ])
    
    return scipy.signal.convolve2d(img[:,:], kernel, mode='same', boundary='symm')


def unsharp_masking(img):
    """Perform sharpening by unsharp masking"""
    # your code here
    # because of the initial image was corrupted with noise and blur, 
    # we will use inly blury image
    img = adaptive_median(img)
    
    laplacian = sharp_laplacian(img)
    
    laplacian = (laplacian - np.min(laplacian))
    laplacian = laplacian/np.max(laplacian)
    sharped = img + laplacian
    sharped = sharped - np.min(sharped)
    sharped = sharped * np.max(sharped)