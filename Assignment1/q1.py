import cv2
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from collections import Counter
image = cv2.imread('1.jpg')
plt.imshow(image)
plt.axis('off')
plt.title("Original")
image2 = image
c_r = Counter(image2[:,:,0].flatten())
c_b = Counter(image2[:,:,1].flatten())
c_g = Counter(image2[:,:,2].flatten())
temp = image[:,:,0].flatten()
maxc = max(c_r)
maxf = c_r[maxc]
for i in c_r:
    c_r[i]/=image.shape[0]*image.shape[1]
uni = sorted(c_r.keys())
cdf = {}
for i in uni:
    m=0
    for j in uni[:uni.index(i)]:
        m+=c_r[j]
    cdf[i]=m*maxc
for i in cdf:
    np.place(temp,temp==i,cdf[i])
image2[:,:,0] = np.uint8(temp.reshape(image[:,:,0].shape))
maxc = max(c_b)
maxf = c_b[maxc]
temp = image[:,:,1].flatten()
for i in c_b:
    c_b[i]/=image.shape[0]*image.shape[1]
uni = sorted(c_b.keys())
cdf = {}
for i in uni:
    m=0
    for j in uni[:uni.index(i)]:
        m+=c_b[j]
    cdf[i]=m*maxc
for i in cdf:
    np.place(temp,temp==i,cdf[i])
image2[:,:,1] = np.uint8(temp.reshape(image[:,:,0].shape))
maxc = max(c_g)
maxf = c_g[maxc]
temp = image[:,:,2].flatten()
for i in c_g:
    c_g[i]/=image.shape[0]*image.shape[1]
uni = sorted(c_g.keys())
cdf = {}
for i in uni:
    m=0
    for j in uni[:uni.index(i)]:
        m+=c_g[j]
    cdf[i]=m*maxc
for i in cdf:
    np.place(temp,temp==i,cdf[i])
image2[:,:,2] = np.uint8(temp.reshape(image[:,:,0].shape))
fig = plt.figure()
plt.imshow(image2)
plt.axis('off')
plt.title("Histogram eq")
plt.show()