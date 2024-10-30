# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:07:46 2017

@author: alber
"""
from __future__ import division, print_function, unicode_literals
from pylab import * 
from skimage.data import astronaut, camera
from scipy.signal import order_filter,medfilt
from time import time
tac=time()

astro=astronaut()
camera=camera()
subplot(1,2,1)
canalR=astro[:,:,0]
canalG=astro[:,:,1]
canalB=astro[:,:,2]
files=astro.shape[0]
columnes=astro.shape[1]
canals=astro.shape[2]
red=unpackbits(canalR,axis=1)
green=unpackbits(canalG)
blue=unpackbits(canalB)
ubcamera=unpackbits(camera)

red[6:files*columnes*8:8]=ubcamera[0:files*columnes*8:8]
red[7:files*columnes*8:8]=ubcamera[1:files*columnes*8:8]
green[6:files*columnes*8:8]=ubcamera[2:files*columnes*8:8]
green[7:files*columnes*8:8]=ubcamera[3:files*columnes*8:8]
blue[6:files*columnes*8:8]=ubcamera[4:files*columnes*8:8]
blue[7:files*columnes*8:8]=ubcamera[5:files*columnes*8:8]

canalR=packbits(red).reshape((files,columnes))
canalG=packbits(green).reshape((files,columnes))
canalB=packbits(blue).reshape((files,columnes))

im=zeros([files,columnes,canals], dtype=int8)
im[:,:,0]=canalR
im[:,:,1]=canalG
im[:,:,2]=canalB
imshow(im,cmap='gray')

tic=time()
print('Temps que triga el programa: {}\n'.format(round(tic-tac,1)))