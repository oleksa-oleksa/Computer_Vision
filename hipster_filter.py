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
