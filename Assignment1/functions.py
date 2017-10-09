import numpy as np
from scipy import misc
img = np.array([])
red = np.array([])
blue = np.array([])
green = np.array([])
count_r = {}
count_g = {}
count_b = {}
def readimg(file):
    global red,blue,green,img
    img = misc.imread(file)
    red = img[:,:,0]
    blue = img[:,:,1]
    green = img[:,:,2]


