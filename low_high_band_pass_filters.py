def high_pass(img_ft, n):
    """Removes the low frequencies
    Low-Pass Filtering (Blurring)"""
    ft = img_ft.copy()
    ft[:n, :n] = 0
    ft[-n:, :n] = 0
    ft[-n:, -n:] = 0
    ft[:n, -n:] = 0
    return ft

def low_pass(img_ft, n):
    """Removes the high frequencies
    High pass filters are usually used for sharpening."""
    # your code here
    ft = img_ft.copy()
    # remove center, n is the number of elements that should remain after filter was applied
    # first  take all rows and cut the columns
    ft[:, n:-n] = 0
    # invert mathematic 
    ft[n:-n, :] = 0
    return ft

def band_pass(img_ft, low, high):
    """Only preserve the frequencies between low and high
    Bandpass filtering can be used to enhance edges (suppressing low frequencies) 
    while reducing the noise at the same time (attenuating high frequencies). 
    """
    # your code here
    # cut the low frequencies
    # high_pass: ---low+++++++++++++
    # low_pass:  +++++++++++++high----
    ft = img_ft.copy()
    ft = high_pass(img_ft, low)
    ft = low_pass(img_ft, high)
    return ft