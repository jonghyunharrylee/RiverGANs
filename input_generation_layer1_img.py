'''
Original Dmatrix 1: right, 2: down, 3: left, 4: up
Sung Eun Kim, Jonghyun Harry Lee
'''

import sys
from scipy.io import loadmat, savemat
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import h5py

beta = 0.0001 # or 1000
rnet = loadmat(('input_%s.mat' % (beta)), squeeze_me=True)

# size to 12 by 12 
img=[]
            
for i in range(1000):
    data = rnet['I%04d'%(i+1)]
    img=[*img,data]

savemat(('input_layer1_img_%s.mat' % (beta)), dict([('ti', img)]))
