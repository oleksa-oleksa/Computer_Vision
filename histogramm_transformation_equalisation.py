def sigmoid_mapping(gain = 10, cutoff = 0.5):
    """
    Returns a 1-dimensional numpy array. The value of the array at the n-position 
    is  `1/(1 + exp*(gain*(cutoff - (n/len(array)))))`.
    """
    # your code here
    sig_array = np.zeros(255)
    
    for n in range(len(sig_array)):
        sig_array[n] = 1/(1 + exp(gain*(cutoff - (n/len(sig_array)))))
    
    return sig_array


 def apply_pixel_mapping(image, mapping):
    """Returns the image transformed according to the mapping array. 
       `mapping` is a one dimensional numpy array. `image` can be 2 or 3-dimensional.
       The values of the image are in range 0 to 1. 
       If the mapping has for example 255 items, then all pixel with a value from 0 to 1/255 are assigned to 
       the value mapping[0]. If the pixel is between n / 255 and (n+1) / 255 then the value in the output image should 
       be mapping[n]
    """
    # your code
    # prepare the holder for the resulting data
    pixel_array = np.zeros_like(image)
    # print(len(mapping))
    
    # numpy array dimensions are (height, width)
    # image can be 2 or 3-dimensional.
    # check the image dimension
    
    # only integers, integer or boolean arrays are valid indicesm ==> round with ceil()
    # len(mapping)-1 for sending correct index into mapping()
    if(image.ndim == 2):
        for row in range(image.shape[0]):
            for column in range(image.shape[1]):
                scaled_pixel = floor(image[row, column]*(len(mapping)-1))
                pixel_array[row, column] = mapping[scaled_pixel]
                #print(pixel_array[row, column])
    
    elif(image.ndim == 3):
        for row in range(image.shape[0]):
            for column in range(image.shape[1]):
                for channel in range(image.shape[2]):
                    # scale to map function resolution
                    scaled_pixel = floor(image[row, column, channel]*(len(mapping)-1))
                    pixel_array[row, column, channel] = mapping[scaled_pixel]
    return pixel_array