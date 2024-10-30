# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 13:36:28 2017

@author: alber
"""
from __future__ import division, print_function, unicode_literals 
from pylab import * 
from time import time
from skimage.data import lena
from random import *
tic=time()
imatge1=lena() #4 canals amb double, ja està normalitzada

#binaritzem la imatge amb el metode FS de difusio d'error

#dimensions=imatge1.ndim


matriu_FS=[[0.,0.,0.],[0.,1.,7/16],[3/16,5/16,1/16]]

imatge_luminancia= 0.299*imatge1[:,:,0] + 0.587*imatge1[:,:,1] + 0.114*imatge1[:,:,1]





for ii in range(imatge_luminancia.shape[0]):#algorisme unidireccional, degrada la imatge
    for jj in range(imatge_luminancia.shape[1]):
        if ii<2 or jj<2:
            imatge_luminancia[ii,jj]=0
        elif ii>510 or jj>510: 
            imatge_luminancia[ii,jj]=0
        else:
            veinatge=imatge_luminancia[ii-1:ii+2,jj-1:jj+2]
            matriu_pixel1=zeros((3,3))
            if imatge_luminancia[ii,jj]<0.5:
                for k in range(3):
                    matriu_pixel1[1][k]=imatge_luminancia[ii,jj]*matriu_FS[1][k]
                for k in range(3):
                    matriu_pixel1[2][k]=imatge_luminancia[ii,jj]*matriu_FS[2][k]
                matriu_sumada= veinatge+matriu_pixel1
                matriu_sumada[1,1]=0
            elif imatge_luminancia[ii,jj] >= 0.5:
                for k in range(3):
                    matriu_pixel1[1][k]=(imatge_luminancia[ii,jj]-1.)*matriu_FS[1][k]
                for k in range(3):
                    matriu_pixel1[2][k]=(imatge_luminancia[ii,jj]-1.)*matriu_FS[2][k]
                matriu_sumada= veinatge+matriu_pixel1
                matriu_sumada[1,1]=1
            imatge_luminancia[ii-1:ii+2,jj-1:jj+2]=matriu_sumada    


imatge_luminancia=uint8(imatge_luminancia)

#generem una matriu random A1

A1=rand(512,512)

A1=A1>=0.5

#trobem A2

A2=imatge_luminancia^A1

imatge_luminancia2= A1^A2

figure(3, figsize=(15,7))

subplot(1,2,1)
imshow(imatge_luminancia,cmap='gray')
title('Imatge I')

subplot(1,2,2)
imshow(imatge_luminancia2, cmap='gray')
title('Imatge A1^A2')

toc=time()
print('Temps que tarda el programa: {}\n'.format(round(toc-tic,1)))