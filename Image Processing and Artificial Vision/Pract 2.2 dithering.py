# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:31:47 2017

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

L=zeros([files, columnes])
L[:,:]= 0.299*canalR + 0.587*canalG + 0.114*canalB 
L=L/255
dreta=7/16
diag_esq=3/16
diag_dret=1/16
baix=5/16


for ii in range(files):
    for jj in range(columnes):
        zero=zeros([3, 3])
        if ii<1 or jj<1:
            continue
        elif ii>files or jj>columnes:
            continue
        elif L[ii,jj]<0.5:
            zero[2,1]=dreta*L[ii,jj]
            zero[2,0]=diag_esq*L[ii,jj]
            zero[2,1]=baix*L[ii,jj]
            zero[2,2]=diag_dret*L[ii,jj]
            zero[1,1]=0.
            L[ii-1:ii+2,jj-1:jj+2]=zero
        elif L[ii,jj]>=0.5:
            zero[2,1]=dreta*L[ii,jj]
            zero[2,0]=diag_esq*L[ii,jj]
            zero[2,1]=baix*L[ii,jj]
            zero[2,2]=diag_dret*L[ii,jj]
            zero[1,1]=1.
            L[ii-1:ii+2,jj-1:jj+2]=zero
            
figure(1)       
imshow(L,cmap='gray')

tic=time()
print('Temps que triga el programa: {}\n'.format(round(tic-tac,1)))