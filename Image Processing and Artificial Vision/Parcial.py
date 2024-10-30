# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 11:55:34 2017

@author: alber
"""
from __future__ import division, print_function, unicode_literals
from pylab import * 
from skimage.data import camera
from time import time
tac=time()
interactive(True)
close('all')

camera=camera()
files=camera.shape[0]
columnes=camera.shape[1]

ubcamera=unpackbits(camera)

R128=ubcamera[0:files*columnes*8:8]
G64=ubcamera[1:files*columnes*8:8]
B32=ubcamera[2:files*columnes*8:8]
R16=ubcamera[3:files*columnes*8:8]
G8=ubcamera[4:files*columnes*8:8]
B4=ubcamera[5:files*columnes*8:8]
R2=ubcamera[6:files*columnes*8:8]
G1=ubcamera[7:files*columnes*8:8]

R=R128+R16+R2
G=G64+G8+G1
B=B32+B4

R=85*R
G=85*G
B=uint8(around(127.4*B))#d'aquesta manera si B=1 obtinc B=127 però si B=2 obtinc 255 i no 254 que seria 127*2

M=uint8(zeros((files,columnes,3)))
M[:,:,0]=R.reshape(files,columnes)
M[:,:,1]=G.reshape(files,columnes)
M[:,:,2]=B.reshape(files,columnes)

figure(1, figsize=(15,7))
subplot(1,2,1)
imshow(M)
title('Usant les assignacions')
subplot(1,2,2)
imshow(camera,cmap='flag')
title('Usant el colormap flag')

tic=time()
print('Temps que triga el programa: {}\n'.format(round(tic-tac,1)))