# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 14:22:01 2017

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

'''Dithering Jarvis, Judice i Ninke'''

M=zeros((5,5))
M[2,3]=7/48
M[2,4]=5/48
M[3,0]=3/48
M[3,1]=5/48
M[3,2]=7/48
M[3,3]=5/48
M[3,4]=3/48
M[4,0]=1/48
M[4,1]=3/48
M[4,2]=5/48
M[4,3]=3/48
M[4,4]=1/48

for ii in range(files):
    for jj in range(columnes):
        zero=zeros([3, 3])
        if ii<2 or jj<2:
            continue
        elif ii>files-3 or jj>columnes-3:
            continue
        elif L[ii,jj]<0.5:
            L[ii-2:ii+3,jj-2:jj+3]+=(0.5-L[ii,jj])*M
            L[ii,jj]=0
        elif L[ii,jj]>=0.5:
            L[ii-2:ii+3,jj-2:jj+3]+=(0.5-L[ii,jj])*M
            L[ii,jj]=1
            
imshow(L,cmap='gray')

tic=time()
print('Temps que triga el programa: {}\n'.format(round(tic-tac,1)))