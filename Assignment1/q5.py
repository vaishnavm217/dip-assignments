import cv2
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
def dist(img_dim,u,v):
    return ((((img_dim[0]/2.0)-u)**2.0)+(((img_dim[1]/2.0)-v)**2.0))**0.5
image = cv2.imread('1.jpg',0)
plt.imshow(image,cmap="gray")
plt.axis('off')
plt.title("Original")
#plt.show()
ft_image = np.fft.fft2(image)
D = float(input("Enter the D0 value"))
image_dim = image.shape
print("Image dimensions:",image_dim)
#ideal low pass filter
res_img_ideal = np.zeros(image_dim).astype(np.complex)
res_img_butterworth = np.zeros(image_dim).astype(np.complex)
res_img_gaussian = np.zeros(image_dim).astype(np.complex)
a = np.arange(image_dim[0])
b = np.arange(image_dim[1])
order_n=1.2
for i in range(image_dim[0]):
    for j in range(image_dim[1]):
        if(dist(image_dim,i,j) <= D):
            res_img_ideal[i,j] = ft_image[i,j]
        res_img_butterworth[i,j] = ft_image[i,j]*(1.0/(1+(dist(image_dim,i,j)/D)**(2*order_n)))
        res_img_gaussian[i,j] = ft_image[i,j]*np.exp(-1*((dist(image_dim,i,j)**2)/(2*(D**2))))
low_pass_ideal_img = np.real(np.fft.ifft2(res_img_ideal))
low_pass_butterw_img = np.real(np.fft.ifft2(res_img_butterworth))
low_pass_gaussian_img = np.real(np.fft.ifft2(res_img_gaussian))
fig = plt.figure()
plt.imshow(low_pass_ideal_img,cmap="gray")
plt.title("Ideal low pass")
plt.axis('off')
plt.savefig("Ideal_low_pass.jpg",bbox_inches='tight')
fig = plt.figure()
plt.imshow(low_pass_butterw_img,cmap="gray")
plt.title("Butterworth low pass")
plt.axis('off')
plt.savefig("butterworth_low_pass.jpg",bbox_inches='tight')
fig = plt.figure()
plt.imshow(low_pass_gaussian_img,cmap="gray")
plt.title("gaussian low pass")
plt.axis('off')
plt.savefig("gaussian_low_pass.jpg",bbox_inches='tight')
plt.show()

        