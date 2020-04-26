import numpy as np
import matplotlib.pyplot as plt
import pylab
import math
pylab.rcParams['figure.figsize'] = (12, 12)   # This makes the plot bigger

def rgb_to_hsv(x):
    """
    Converts the numpy array `x` from RGB to the HSV. 
    """
    # separating channels
    R = x[:,:,0]
    G = x[:,:,1]
    B = x[:,:,2]
    
    
    # h, s, v = hue, saturation, value 
    # initial arrays for h, s and v filled with 0.0
    # we take R array just as 2D sample for copying the shape
    H = np.full_like(R, 0.0, dtype=np.double)
    S = np.full_like(R, 0.0, dtype=np.double)
    V = np.full_like(R, 0.0, dtype=np.double)
    
    HSV = np.full_like(x, 0.0, dtype=np.double)
 
    # np.max/min and axis=2 creates a 2D matrix
    C_max = np.max(x, axis=2)    # maximum of r, g, b 
    C_min = np.min(x, axis=2)    # minimum of r, g, b 
    Diff = C_max - C_min       # diff of cmax and cmin. 
    
    # Formula:
    # https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
    
    # if cmax and cmax are equal (R=G=B) then h = 0 
    H[np.isclose(C_max, R, 0.0001)] = 0   
        
    # if cmax equal r 
    m = np.isclose(C_max, R, 0.0001)&(Diff!=0)
    H[m] = (60 * ((G[m] - B[m]) / Diff[m]) + 360) % 360
    

    # if cmax equal g 
    m = np.isclose(C_max, G, 0.0001)&(Diff!=0)
    H[m] = (60 * ((B[m] - R[m]) / Diff[m]) + 120) % 360
  
    # if cmax equal b 
    m = np.isclose(C_max, B, 0.0001)&(Diff!=0)
    H[m] = (60 * ((R[m] - G[m]) / Diff[m]) + 240) % 360
    
    # if cmax equal zero 
    S[C_max == 0] = 0
    
    # else
    m = (C_max != 0)
    S[m] = (Diff[m] / C_max[m])
  
    # compute v 
    V = C_max
    
    # building new 3D picture
    HSV[:,:,0] = H
    HSV[:,:,1] = S
    HSV[:,:,2] = V
    
    return HSV