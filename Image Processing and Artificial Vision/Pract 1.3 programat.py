# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 12:01:48 2017

@author: Ripo
"""

from __future__ import division, print_function, unicode_literals
from pylab import * 
from skimage.data import astronaut
from scipy.ndimage.measurements import histogram

imatge=astronaut()
canalG=imatge[:,:,1]

files=imatge.shape[0]
columnes=imatge.shape[1]
canals=imatge.shape[2]

matriuG=zeros([files,columnes,canals], dtype=int8)
matriuG[:,:,1]=canalG

def equalitzhistogram(imatge):
    histo=histogram(imatge,0,255,bins=256)
    histoac=histo.cumsum()
    imatge_eq=uint8(255*histoac[imatge]/histoac.max())
    histo_eq=histogram(imatge_eq,0,255,bins=256)
    return (imatge_eq,histo,histo_eq)
    
imatge_eq,histo_def,histo_eq=equalitzhistogram(imatge)

histoG=histogram(canalG,0,255,bins=256)
histo=histogram(imatge,0,255,bins=256)
histo_normalitzat=histo/(files*columnes)
'''
figure(1)
subplot(2,2,1)
imshow(imatge)
subplot(2,2,2)
imshow(canalG)
subplot(2,2,3)
imshow(matriuG)
subplot(2,2,4)
plot(histoG,'g')
plot(histo_def,'r')
plot(histo,'b')
axis([0,255,0,20000])

figure (2)
subplot(2,2,1)
imshow(imatge)
subplot(2,2,2)
imshow(imatge_eq)
subplot(2,2,3)
plot(histo)
axis([0,255,0,20000])
subplot(2,2,4)
plot(histo_eq)
axis([0,255,0,20000])
'''
