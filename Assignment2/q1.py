from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.figure as fig
img = np.array(Image.open('bg1.jpg'))
"""
Normalized channels
"""
R = img[:,:,0]/np.max(img[:,:,0])
G = img[:,:,1]/np.max(img[:,:,1])
B = img[:,:,2]/np.max(img[:,:,2])

Hue = np.arccos(((2*R)-G-B)/2*np.sqrt(np.square(R-G)+np.multiply((R-G),(G-B))))
Intensity = np.mean(img/255,axis=2)
Imin = np.min(img/255,axis=2)
Intensity[Intensity==0]=0.1 #avoiding zero error
Saturation = 1 - (Imin/Intensity)
fig = plt.figure()
ax = fig.add_subplot(111)
n,bins,p = ax.hist(Saturation.flatten())
ax.set_xbound(0,1)
ax.plot(bins)
print(np.max(Intensity))
plt.show()
print(Intensity)
print(Saturation)
