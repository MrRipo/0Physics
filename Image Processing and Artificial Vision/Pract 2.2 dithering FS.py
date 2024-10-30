# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:12:19 2017

@author: alber
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

L=zeros([files, columnes])
L[:,:]= 0.299*canalR + 0.587*canalG + 0.114*canalB 
L=L/255

'''Dithering Floyd i Steinberg'''

M=zeros((3,3))
M[1,2]=7/16
M[2,0]=3/16
M[2,1]=5/16
M[2,2]=1/16

for ii in range(files):
    for jj in range(columnes):
        zero=zeros([3, 3])
        if ii==0 or jj==0:
            continue
        elif ii==files-1 or jj==columnes-1:
            continue
        elif L[ii,jj]<0.5:
            L[ii-1:ii+2,jj-1:jj+2]+=(0.5-L[ii,jj])*M
            L[ii,jj]=0
        elif L[ii,jj]>=0.5:
            L[ii-1:ii+2,jj-1:jj+2]+=(0.5-L[ii,jj])*M
            L[ii,jj]=1

imshow(L,cmap='gray')

tic=time()
print('Temps que triga el programa: {}\n'.format(round(tic-tac,1)))