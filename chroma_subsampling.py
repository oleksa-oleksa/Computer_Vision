class ChromaSubsampling:
    """See https://en.wikipedia.org/wiki/YCbCr."""
    ycbcr = np.array([
        [0.299,  0.587,  0.114],
        [-0.168736, -0.331264,  0.5],
        [0.5, -0.418688, -0.0813],
    ])
    def __call__(self, rgb_img):
        """Transforms the rgb image to YCbCr. The cb and cr channels have half the resolution of the Y-channel.
           You can simply use the mean of four neighbours.
        """
        shape = rgb_img.shape
        
        ycbcr_img = np.dot(self.ycbcr, rgb_img.reshape(-1, 3).T)
        ycbcr_img = ycbcr_img.T.reshape(shape)
        ycbcr_img[:,:, [1,2]] += 128
        # subsample the cb and cr channel, so that they have half the resolution of the Y-channel.
        # A simple thing might be to use the mean of 4 neighbours.
        # your code here
        # 4:2:2 has half the chroma
        # https://medium.com/@sddkal/chroma-subsampling-in-numpy-47bf2bb5af83
        sub_img = ycbcr_img.copy()
        # Vertically, every second element equals to element above itself.
        sub_img[1::2, :] = sub_img[::2, :] 
        # Horizontally, every second element equals to the element on its left side.
        sub_img[:, 1::2] = sub_img[:, ::2]
        # y, cb, cr
        return sub_img[:, :, 0], sub_img[:, :, 1], sub_img[:, :, 2]
    
     def invert(self, inputs):
        y, cb, cr = inputs
        # debug
        #print(y.shape)
        
        # your code here
        rgb_matrix = np.array([
            [1, 0, 1.402], 
            [1, -0.34414, -0.71414], 
            [1, 1.772, 0]
        ])

        shape = (y.shape[0], y.shape[1], 3)
        rgb_img = np.zeros(shape, dtype=np.double)
        
        print(rgb_img.shape)
        rgb_img[:,:,0] = y
        rgb_img[:,:,1] = cb
        rgb_img[:,:,2] = cr

        rgb_img[:,:, [1,2]] -= 128

        rgb_img = rgb_img.dot(rgb_matrix.T)
        '''
        cb_mod = cb - 128
        cr_mod = cr - 128
        r = y + 1.402 * cr_mod
        g = y - 0.34414 * cb_mod - 0.71414 * cr_mod
        b = y + 1.772 * cb_mod

        rgb_img[:,:,0] = r
        rgb_img[:,:,1] = g
        rgb_img[:,:,2] = b
        '''
        np.putmask(rgb_img, rgb_img > 255, 255)
        np.putmask(rgb_img, rgb_img < 0, 0)
        return np.uint8(rgb_img)