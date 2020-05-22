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
    
    lap_derivative = scipy.signal.convolve2d(img[:,:], kernel, mode='same', boundary='symm')
    return img + lap_derivative


def unsharp_masking(img):
    """Perform sharpening by unsharp masking
    Recall our definition of sharpness (”more blur = less sharp”)
    A simple method of adding the detail that might have been lost due to blur is:
    Blur the original
    Subtract the blurred image from the original 
    Add the result to the original """
    
    # Blur the original
    blurred = gaussian(img , 1.6)
    
    # Subtract the blurred image from the original
    unsharped = img - blurred
    # normalise
    #unsharped = unsharped/np.max(unsharped)
    
    # Add the result to the original
    amplifier = 4
    sharped = img + amplifier*unsharped
 
    return np.clip(sharped, 0,1)