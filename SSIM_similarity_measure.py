def ssim(img, filtered_img):
    """The SSIM similarity measure. Use the parameters from the paper 
    as on the second to last slide from the lecture"""
    # your code
    # img is original
    """
    Suppose x and y are two non-negative image signals, which have been aligned with eachother 
    (e.g., spatial patches extracted from each image). If we consider one of the signals 
    to have perfect quality, then the similarity measure can serve as a quantitative measurement 
    of the quality of the second signal. 
    """
    
    img = rgb2grey(img)
    filtered_img = rgb2grey(filtered_img)

    mu_orig = np.mean(img)
    mu_filtered = np.mean(filtered_img)
    
    std_orig = np.std(img, dtype = np.float32)
    std_filtered = np.std(filtered_img, dtype = np.float32)

    # As in the luminance and contrast measures, we have introduced a small constant 
    # in both denominator and numerator.  In discrete form, σ_xy can be estimated as:
    # σ_xy = (1/(N−1))* sum ((x_i − μ_x) * (y_i − μ_y)) 
    
    amount_of_pixels_xy = img.shape[0] * img.shape[1] - 1
    std_xy = np.sum((img - mu_orig) * (filtered_img - mu_filtered))/amount_of_pixels_xy
    

    # From papper: Image Quality Assessment: From Error Visibility to Structural Similarity 
    # For luminance comparison, we definel(x,y) = (2 * μ_x * μ_y + C1)/(μ_x^2 + μ_y^2 + C1)
    # where the constant C1 is included to avoid instability when μ2x+μ2y is very close to zero. 
    # Specifically, we choose C1= (K_1 * L)**2
    # where L is the dynamic range of the pixel values (255 for8-bit grayscale images), 
    # and K_1 < 1 is a small constant.
    
    luminance_c1 = (0.000005 * 255) ** 2
    
    # The contrast comparison function takes a similar form:
    # c(x,y) = (2 * σ_xy + C2)/(σ_x^2 + σ_y^2 + C2)
    # where C2= (K2_2 * L)**2, and K_2 < 1.
    
    contrast_c2 = (0.00025 * 255) ** 2
    
    
    # specific form of the SSIM index (In order to simplify the expression,we set α = β = γ = 1 
    # and C3 = C2/2 in this paper)
    # Specific form of the SSIM for calculation:
    # SSIM(x,y) =((2 * μ_x * μ_y + C1)*(2 * σ_xy + C2))/((μ_x^2 + μ_y^2 + C1)*(σ_x^2 + σ_y^2 + C2))

    ssim_numerator = (2 * mu_orig * mu_filtered + luminance_c1) * (2 * std_xy  + contrast_c2)
    ssim_denominator = (mu_orig**2 + mu_filtered**2 + luminance_c1) * (std_orig**2 + std_filtered**2 + contrast_c2)
    
    ssim_result = float(ssim_numerator / ssim_denominator)
    
    # debug for calculated similarity
    print(ssim_result)
    
    return ssim_result
    