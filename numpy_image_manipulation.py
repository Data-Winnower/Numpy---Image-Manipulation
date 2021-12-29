# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:23:09 2021

@author: kalep
"""

import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# import an image to manipulate
camaro = io.imread("camaro.jpg")
plt.imshow(camaro)
plt.show()


# pull out the different color channels
red = np.zeros(camaro.shape, dtype = "uint8")
red[:,:,0] = camaro[:,:,0]
plt.imshow(red)
plt.show()

green = np.zeros(camaro.shape, dtype = "uint8")
green[:,:,1] = camaro[:,:,1]
plt.imshow(green)
plt.show()

blue = np.zeros(camaro.shape, dtype = "uint8")
blue[:,:,2] = camaro[:,:,2]
plt.imshow(blue)
plt.show()

rg = np.zeros(camaro.shape, dtype = "uint8")
rg[:,:,0:2] = camaro[:,:,0:2]
plt.imshow(rg)
plt.show()

rb = np.zeros(camaro.shape, dtype = "uint8")
rb[:,:,0] = camaro[:,:,0]
rb[:,:,2] = camaro[:,:,2]
plt.imshow(rb)
plt.show()

bg = np.zeros(camaro.shape, dtype = "uint8")
bg[:,:,1:3] = camaro[:,:,1:3]
plt.imshow(bg)
plt.show()

# combine the different channels
# into a 'rainbow' array
rainbow1 = np.vstack((red,rg,green,bg,blue,rb))
rainbow2 = np.vstack((rg,green,bg,blue,rb,red))
rainbow3 = np.vstack((green,bg,blue,rb,red,rg))
rainbow4 = np.vstack((bg,blue,rb,red,rg,green))
rainbow5 = np.vstack((blue,rb,red,rg,green,bg))
rainbow6 = np.vstack((rb,red,rg,green,bg,blue))
rainbow = np.hstack((rainbow1, rainbow2,rainbow3,rainbow4, rainbow5,rainbow6))
plt.imshow(rainbow)
plt.show()

# Save the resulting image to my drive
# as a jpeg
io.imsave("camaro_rainbow.jpg", rainbow)
