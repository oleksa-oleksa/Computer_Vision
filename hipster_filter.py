import numpy as np
import matplotlib.pyplot as plt
import pylab
import ssl
from urllib.request import urlopen
from skimage.data import astronaut
from skimage.data import chelsea
from skimage.color import rgb2gray, rgb2hsv, hsv2rgb

pylab.rcParams['figure.figsize'] = (12, 12)   # This makes the plot bigger

img = astronaut() / 255.
cat = chelsea() / 255.

img2 = rgb2hsv(cat)

# Transform the V-Channel with sigmoid_mapping and gain = 10.
img2[:, :, 2] = apply_pixel_mapping(img2[:, :, 2], sigmoid_mapping(gain = 10))

plt.imshow(cat) # original image
plt.show()

plt.imshow(hsv2rgb(img2)) # show the result from step 2
plt.show()

# Transform the S-Channel with sigmoid_mapping and gain = 10, cufoff=0.35
img3 = np.copy(img2)
img3[:, :, 1] = apply_pixel_mapping(img2[:, :, 1], sigmoid_mapping(gain = 10, cutoff=.35))
plt.imshow(hsv2rgb(img3))     # show the result from step 3
plt.show()

here V is the resulting V-Channel from step 2.
img4 = np.copy(img3)

# the input array must be have a shape == (.., ..,[ ..,] 3))
color_hsv = hsv2rgb([[[0.05,1,1]]])

for row in range(img4.shape[0]):
    for column in range(img4.shape[1]):
        img4[row, column, 0] += color_hsv[0,0,0]*0.5*(1 - img2[row, column, 2])
        img4[row, column, 1] += color_hsv[0,0,1]*0.5*(1 - img2[row, column, 2])
        img4[row, column, 2] += color_hsv[0,0,2]*0.5*(1 - img4[row, column, 2])


plt.imshow(np.clip((hsv2rgb(img4)), 0, 1))      # show the result from step 4
plt.show()

# plot the original image
plt.imshow(cat)

#=====================

import random

def hipster_filter(image):
    
    f_img = np.copy(image)
      
    # reduce red color 
    f_img[:, :, 0] = f_img[:, :, 0] - f_img[:, :, 0]*0.25

    # tune green and blue so that we will have some blue background (was found experimentally)
    # we have to reduce green part and increase blue channel
    f_img[:, :, 1] = f_img[:, :, 1] - f_img[:, :, 1]*0.10
    f_img[:, :, 2] = f_img[:, :, 2] + f_img[:, :, 1]*0.20

    # convert into hsv so that we can play with brightness and hue
    f_img = rgb2hsv(f_img)

    """
    1/360 = 0.0027
    I want to make a cat more red, so the red color hue is betweeen 25 grad and 45 grad 
    (using picker https://www.google.com/search?q=color+picker+rgb&oq=color+picker+rgb&aqs=chrome..69i57j35i39j0l6.5163j0j1&sourceid=chrome&ie=UTF-8)
    """
    hue = f_img[:, :, 0]
    low_reddy = 25 * 0.0027
    up_reddy = 45 * 0.0027

    for row in range(hue.shape[0]):
        for column in range(hue.shape[1]):
            # if the pixel has some red hue - set random hue from the red "catty" color gamut
            if hue[row, column] < up_reddy:
                hue[row, column] = random.uniform(low_reddy, up_reddy) # randomize
                f_img[row, column, 1] = f_img[row, column, 1] * 1.25 # increase the saturation in the original image

    # replace the original hue channel with modified channel
    f_img[:, :, 0] = hue
    # increase the saturation of the whole image
    f_img[:, :, 1] = f_img[:, :, 1] * 1.2
    # rise the brightness 
    f_img[:, :, 2] = f_img[:, :, 2] * 1.6

    
    # convert to rgb and cut the pixels that overlapped 1 
    f_img = np.clip((hsv2rgb(f_img)), 0, 1)
    
    return f_img

hipster_cat = hipster_filter(cat)
plt.imshow(hipster_cat) # show the result from step 4
plt.show()
plt.imshow(cat) # plot the original image
plt.show()

woman = hipster_filter(img)
plt.imshow(woman) # show the result from step 4
plt.show()
plt.imshow(img) # plot the original image
plt.show()