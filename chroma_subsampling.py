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
        # your code here
        return np.stack([y, cb, cr], axis=-1)