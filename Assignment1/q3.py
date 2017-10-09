import cv2
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
image = cv2.imread('2.JPG',0)
plt.imshow(image,cmap="gray")
plt.axis('off')
plt.title("Original")
filter_w = np.array([1,2,1,2,4,2,1,2,1]).reshape(3,3)
weigh = signal.correlate2d(image,filter_w,mode='same')
fig = plt.figure()
plt.imshow(weigh,cmap="gray")
plt.axis('off')
plt.title("weighted")
plt.savefig("weighted_q3.jpg",bbox_inches='tight')
plt.show()
res = np.zeros(image.shape)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if(not(i==0 or i==image.shape[0]-1 or j==0 or j==image.shape[1]-1)):
            res[i,j]=np.median([image[i-1,j-1],image[i-1,j],image[i-1,j+1],image[i,j-1],image[i,j],image[i,j+1],image[i+1,j-1],image[i+1,j],image[i+1,j+1],])
        else:
            if(i==0 and j==0):
                res[i,j] = np.median([image[i,j],image[i,j+1],image[i+1,j],image[i+1,j+1]])
            elif(i==image.shape[0]-1 and j==0):
                res[i,j] = np.median([image[i,j],image[i-1,j],image[i-1,j+1],image[i,j+1]])
            elif(i==image.shape[0]-1 and j==image.shape[1]-1):
                res[i,j] = np.median([image[i,j],image[i-1,j],image[i-1,j-1],image[i,j-1]])
            elif(i==0 and j==image.shape[1]-1):
                res[i,j] = np.median([image[i,j],image[i+1,j],image[i+1,j-1],image[i,j-1]])
            elif(i==0):
                res[i,j] = np.median([image[i,j-1],image[i,j],image[i,j+1],image[i+1,j],image[i+1,j-1],image[i+1,j+1]])
            elif(i==image.shape[0]-1):
                res[i,j] = np.median([image[i,j-1],image[i,j],image[i,j+1],image[i-1,j],image[i-1,j-1],image[i-1,j+1]])
            elif(j==0):
                res[i,j] = np.median([image[i-1,j],image[i,j],image[i+1,j],image[i,j+1],image[i-1,j+1],image[i+1,j+1]])
            elif(j==image.shape[1]-1):
                res[i,j] = np.median([image[i-1,j],image[i,j],image[i+1,j],image[i,j-1],image[i-1,j-1],image[i+1,j-1]])
fig = plt.figure()
plt.imshow(res,cmap="gray")
plt.axis('off')
plt.title("median")
plt.savefig("median_q3.jpg",bbox_inches='tight')
plt.show()