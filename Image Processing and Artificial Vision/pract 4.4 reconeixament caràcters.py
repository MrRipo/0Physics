# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:50:10 2017

@author: alber
"""
from __future__ import division, print_function, unicode_literals
from pylab import * 
from time import time
tac=time()

text=255-imread('text.jpg')[:,:,1]
ref=255-imread('ref.jpg')[:,:,1]

TF_text=fft2(text)
TF_ref=fft2(ref)

cor=abs(ifftshift(ifft2(TF_text*conjugate(TF_ref))))
cor_fase=abs(ifftshift(ifft2(TF_text*conjugate(TF_ref)/abs(TF_ref))))

tcr=cor_fase/cor_fase.max()
tcrm=tcr>.2

figure(1,figsize=(15,7))
imshow(tcr, cmap='gray')
figure(2,figsize=(15,7))
subplot(2,2,1)
imshow(cor, cmap='gray')
subplot(2,2,2)
imshow(cor_fase, cmap='gray')
subplot(2,2,3)
imshow(tcr, cmap='gray')
subplot(2,2,4)
imshow(tcrm, cmap='gray')

tic=time()
print('Temps que triga el programa: {}\n'.format(round(tic-tac,1)))