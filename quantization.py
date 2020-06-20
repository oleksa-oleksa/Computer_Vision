class Quantization:
    def __init__(self, threshold=1):
        # you can use the Q matrix from Wikipedia or invent your own.
        self.q_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                        [12, 12, 14, 19, 26, 58, 60, 55],
                        [14, 13, 16, 24, 40, 57, 69, 56],
                        [14, 17, 22, 29, 51, 87, 80, 62],
                        [18, 22, 37, 56, 68, 109, 103, 77],
                        [24, 35, 55, 64, 81, 104, 113, 92],
                        [49, 64, 78, 87, 103, 121, 120, 101],
                        [72, 92, 95, 98, 112, 100, 103, 99]])
        self.threshold = threshold

    def __call__(self, blocks):
        """Divides the blocks by the `q_matrix` elementwise. Coefficents under the `threshold` will be set to zero."""
        # your code here
        # Returns a true division of the inputs, element-wise.
        # If x1.shape != x2.shape, they must be broadcastable to a common shape (which becomes the shape of the output).
        
        result = np.zeros_like(blocks)
        result = np.divide(blocks, self.q_matrix)
        result[np.abs(result) < self.threshold] = 0
        #result[result < self.threshold] = 0

        return result
    
    def invert(self, blocks):
        """ For inverting multiply your elements piecewise with the Q-Matrix"""
        return np.multiply(blocks, self.q_matrix)