import cv2
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
image = cv2.imread('1.jpg')
plt.imshow(image)
plt.axis('off')
plt.title("Original")
#normalizing channels and typecasting to integer8
image5 = np.uint8(np.power(image/255.0,5)*255)
image02= np.uint8(np.power(image/255.0,0.2)*255)
plt.imshow(image5)
plt.axis('off')
plt.title("Gamma 5")
plt.savefig("Gamma_5.jpg",bbox_inches='tight')
fig = plt.figure()
plt.imshow(image02)
plt.axis('off')
plt.title("Gamma 0.2")
plt.savefig("Gamma_02.jpg",bbox_inches='tight')
plt.show()

