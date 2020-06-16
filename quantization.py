class Quantization:
    def __init__(self, threshold=1):
        # you can use the Q matrix from Wikipedia or invent your own.
        self.q_matrix = []
        self.threshold = threshold

    def __call__(self, blocks):
        """Divides the blocks by the `q_matrix` elementwise. Coefficents under the `threshold` will be set to zero."""
        # your code here
        return blocks
    
    def invert(self, blocks):
        """ For inverting multiply your elements piecewise with the Q-Matrix"""
        return blocks