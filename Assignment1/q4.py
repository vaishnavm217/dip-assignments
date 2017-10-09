import cv2
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
image = cv2.imread('1.jpg',0)
plt.imshow(image,cmap="gray")
plt.axis('off')
plt.title("Original")
"""
Gradient
"""
filter_x = np.array([0,0,0,0,1,-1,0,0,0]).reshape(3,3)
filter_y = np.array([0,-1,0,0,1,0,0,0,0]).reshape(3,3)
print(filter_x)
print(filter_y)
grad_x = signal.correlate2d(image,filter_x,mode='same')
fig = plt.figure()
plt.imshow(grad_x,cmap="gray")
plt.axis('off')
plt.title("X grad")
grad_y = signal.correlate2d(image,filter_y,mode='same')
fig = plt.figure()
plt.imshow(grad_y,cmap="gray")
plt.axis('off')
plt.title("Y grad")
final = np.sqrt(np.power(grad_x,2)+np.power(grad_y,2))
fig = plt.figure()
plt.imshow(final,cmap="gray")
plt.axis('off')
plt.title("Gradient")
"""
Laplacian
"""
filter_la = np.array([0,1,0,1,-4,1,0,1,0]).reshape(3,3)
fil_la = signal.correlate2d(image,filter_la,mode='same')
fil_la = np.abs(fil_la)
fig = plt.figure()
plt.imshow(fil_la,cmap="gray")
plt.axis('off')
plt.title("La Placian")
plt.show()