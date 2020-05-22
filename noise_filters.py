import scipy.signal

basic_kernel = np.ones((3, 3))
basic_kernel_size = np.size(basic_kernel)
lower_y = 1
lower_x = 1

#---- helper functions ----
def get_filter_frame(img, position_row, position_column):
    # convolution requires values from pixels outside of the image boundaries
    # we will cut the picture in advance and the filtered image will be smaller
    
    frame = np.ones_like(basic_kernel)
    filtered_row = position_row - 1
    filtered_column = position_column - 1
    
    # no exeptions if we call function without cutting
    if position_row == 0 or position_column == 0 or position_row == img(shape[1]-1) or position_column == img(shape[0]-1):
        # frame of ones returns
        # probably not the best solution but will help to skip the exeptions
        return(frame)
    
    # filter frame is not outside the image boundaries
    # copy the 9 pixels surrounding central pixel into filter frame
    else:
        for row in range(basic_kernel(shape[0])):
            for column in range(basic_kernel(shape[1])):
                frame[row, column] = img[filtered_row, filtered_column]
                filtered_column = filtered_column + 1
            filtered_column = position_column - 1
            filtered_row = filtered_row + 1
    return frame
    
#--------------------------

def arithmetic_mean(img):
    kernel = basic_kernel * 1/9
    
    # Numpy is not a solution because it works only with 1D array (object too deep for desired array)
    #return np.convolve(img[:,:], kernel, mode="same")
    return scipy.signal.convolve2d(img[:,:], kernel, mode='same')


 def geometric_mean(img):
    result = np.zeros_like(img)
    upper_x = result.shape[1]-1
    upper_y = result.shape[0]-1

    for row in range(lower_y, upper_y):
        for column in range(lower_x, upper_x):
            img_frame = get_filter_frame(img, row, column)
            result[row, column] = np.prod(img_frame).astype(np.float) ** (1 / float(basic_kernel_size))
    return result


 def contraharmoic_mean(img, q=None):
    pepper_noise = 0.8
    salt_noise = -0.8
    # Your need to select the q yourself
    # Q is the order of the filter.
    # Positive values of Q eliminate pepper noise. Negative values of Q eliminate salt noise.
    # It cannot eliminate both simultaneously.
    result = np.zeros_like(img)
    upper_x = result.shape[1]-1
    upper_y = result.shape[0]-1
    
    if q is None or q == 0:
        q = pepper_noise
    

    for row in range(lower_y, upper_y):
        for column in range(lower_x, upper_x):
            img_frame = get_filter_frame(img, row, column)
            nominator = np.sum(img_frame ** (q + 1)) / float(basic_kernel_size)
            denominator = np.sum(img_frame ** q) / float(basic_kernel_size)
            
            # RuntimeWarning: divide by zero encountered in true_divide -> set demominator manually to a very small value
            if denominator == 0:
                denominator = 0.0001
                
            result[row, column] = nominator / denominator
    return result

 def adaptive_median(img):
    result = np.zeros_like(img)
    upper_x = result.shape[1]-1
    upper_y = result.shape[0]-1
    
    # maximum allowed size of Sxy
    Smax = 17
    Sxy = basic_kernel_size # 9 by default, set by global variable
    
    for row in range(lower_y, upper_y):
        for column in range(lower_x, upper_x):            
            while (True):
                img_frame = get_filter_frame(img, row, column)
                
                # median of grey levels in Sxy
                Zmed = np.median(img_frame)
                Zmin = np.min(img_frame)
                Zmax = np.max(img_frame)
                # grey level at coordinates (x, y)
                Zxy = img[row,column]

                A1 = Zmed - Zmin
                A2 = Zmed - Zmax

                if (A1 > 0 and A2 < 0):
                    # If A1 > 0 and A2 < 0, Go to stage B
                    B1 = Zxy - Zmin
                    B2 = Zxy - Zmax
                    
                    # stage B
                    if (B1 > 0 and B2 < 0):
                        # If B1 > 0 and B2 < 0, output zxy
                        result[row,column] = Zxy
                        break
                    else:
                        # Else output zmed
                        result[row,column] = Zmed
                        break
                
                # else continue stage A              
                # if window size ≤ Smax repeat stage A
                elif (Sxy < Smax):
                    # increase the window size
                    Sxy = Sxy + 4 # 9- 13 - 17 - 21
                else:
                    # Else output zmed
                    result[row, column] = Zmed
                    break
                
    return np.clip(result, 0, 1)

def adaptive_mean(img):
    result = np.zeros_like(img)
    upper_x = result.shape[1]-1
    upper_y = result.shape[0]-1
    # Operate on a local and based on
    # 1. The value of the noisy image at pixel (x,y) 
    # 2. The variance of the noise
    # 3. The local mean of the pixels in the local region
    # 4. The local variance
    
    var = np.var(img)
    
    for row in range(lower_y, upper_y):
        for column in range(lower_x, upper_x):            
            img_frame = get_filter_frame(img, row, column)
            local_var = np.var(img_frame)
            local_mean = np.mean(img_frame)
            # the value of noisy image is accessible in the loop

            # zero-noise case, copy-paste the original pixel into result
            if var == 0:
                result[row, column] = img[row, column]
            # if the local variance is high relative to global variance, the filter should return the value close
            # to g(x, y). A high local variance typically is accossiated with edges and those should be preserved
            if local_var > var:
                result[row-1 : row+2, column-1 : column+2] = img_frame - ((var**2 / local_var**2) * (img_frame - local_mean))
            # it the two variances are equal, we want a filter to return the arithmetic mean value of S(x, y)
            # this condition occurs when the local area has the same properties as the overall image, 
            # and the local noise is to be reduced simply by averaging
            if local_var == var:
                result[row, column] = local_mean
            
    return np.clip(result, 0, 1)
