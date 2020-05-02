def affine_transformation(img, matrix):
    # note: matrix is a transformation matrix
    # catch the scaling factor
    # Python's math module contain handy functions like floor & ceil. 
    # These functions take a floating point number and return the nearest integer below or above it.
    
    s = img.shape
    # save 4 corners of the original image in homogeneous coordinates 
    # we want to find the new borders based on the transformed 4 corners
    corners = np.array([[0, 0, 1], [0, s[1], 1], [s[0], 0, 1], [s[0], s[1], 1]]).T
    
    # map affine transformation with original corners
    new_corners = matrix @ corners
    # find the maximal corner of the new transformed image
    m = np.ceil(np.max(new_corners, axis=1)).astype(np.int)[:2]
    
    inv_m = np.linalg.inv(matrix)
    
    # build a list of vectors representing every point in the new image
    # np.indices(m) returns an array wih the cootdinates of every point of the image
    # reshape(2, -1) reshapes the returned array into the row vector
    vecs = np.indices(m).reshape(2, -1)
    # np.vstack adds row of "1" a third dimension to perform transromation using homogeneous coordinates
    vecs = np.vstack((vecs, np.ones(vecs.shape[1])))
    # matrix multiplication: map points from the new image to the original and remove homogeneous component
    vecs = (inv_m@vecs)[:2, :]
    # row vector is converted to the form of 2 D matrix of the same size as new image, where every cell contains 
    # coordinates mapped to the original image
    # Other words: it maps every pixel in the position on the original image
    vecs = vecs.T.reshape(m[0], m[1], -1)
    # apply bicubic interpolation
    return bicubic_interpolation(img, vecs)