# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:55:10 2017

@author: Ripo
"""
from __future__ import division, print_function, unicode_literals
from pylab import * 
from skimage.data import lena
from scipy.signal import order_filter,medfilt
from time import time
tac=time()

interactive(True)
close('all')

imatge=lena()

canalR=imatge[:,:,0]
canalG=imatge[:,:,1]
canalB=imatge[:,:,2]

files=imatge.shape[0]
columnes=imatge.shape[1]

mitjana=zeros([files, columnes])
mitjana[:,:]= canalR/3 + canalG/3 + canalB/3

L=zeros([files, columnes])
L[:,:]= 0.299*canalR + 0.587*canalG + 0.114*canalB 

domain=ones([5,5])
x=order_filter(L,domain,12)
y=medfilt(L,kernel_size=[5,5])

figure(1)
subplot(1,2,1)
imshow(x,cmap='gray')
subplot(1,2,2)
imshow(y,cmap='gray')

tic=time()
print('Temps que triga el programa: {}\n'.format(round(tic-tac,1)))