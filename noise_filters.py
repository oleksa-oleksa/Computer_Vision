#---- helper functions ----
def get_filter_frame(img, position_x, position_y):
    # convolution requires values from pixels outside of the image boundaries
    # we will cut the picture in advance and the filtered image will be smaller
    
    frame = np.ones_like(basic_kernel)
    filtered_x = position_x - 1
    filtered_y = position_y - 1
    
    # no exeptions if we call function without cutting
    if position_x == 0 or position_y == 0 or position_x == img(shape[1]-1) or position_y == img(shape[0]-1):
        # frame of ones returns
        # probably not the best solution but will help to escape the exeptions
        return(frame)
    
    # filter frame is not outside the image boundaries
    # copy the 9 pixels surrounding central pixel into filter frame
    else:
        for row in range(basic_kernel(shape[0])):
            for column in range(basic_kernel(shape[1])):
                frame[row, column] = img[filtered_x, filtered_y]
                filtered_y = filtered_y + 1
            filtered_y = position_y - 1
            filtered_x = filtered_x + 1
    return frame
    

#--------------------------

def arithmetic_mean(img):
    kernel = basic_kernel * 1/9
    
    # Numpy is not a solution because it works only with 1D array (object too deep for desired array)
    #return np.convolve(img[:,:], kernel, mode="same")
    return scipy.signal.convolve2d(img[:,:], kernel, mode='same')