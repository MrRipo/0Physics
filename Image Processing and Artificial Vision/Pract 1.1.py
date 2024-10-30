# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 12:42:27 2017

@author: fis.aules

"""

from __future__ import division, print_function, unicode_literals
from pylab import * 
from time import time
from skimage.data import astronaut

tac=time()

interactive(True)
close('all')

imatge=astronaut()
imatge_double= double(astronaut())

figure(1)
subplot(1,2,1)
imshow(imatge)
subplot(1,2,2)
imshow(imatge_double/255.) 

canalR=imatge[:,:,0]
canalG=imatge[:,:,1]
canalB=imatge[:,:,2]

files=imatge.shape[0]
columnes=imatge.shape[1]
canals=imatge.shape[2]

print('Nombre de pixels (files x columnes) = {} x {}\nLa imatge té {} canals'.format(files, columnes, canals))

matriuR=zeros([files,columnes,canals], dtype=int8)
matriuR[:,:,0]=canalR

matriuG=zeros([files,columnes,canals], dtype=int8)
matriuG[:,:,1]=canalG

matriuB=zeros([files,columnes,canals], dtype=int8)
matriuB[:,:,2]=canalB

figure (2)
subplot(2,1,1)
imshow(matriuR)

subplot(2,2,3)
imshow(matriuG)

subplot(2,2,4)
imshow(matriuB)

mitjana=zeros([files, columnes])
mitjana[:,:]= canalR/3 + canalG/3 + canalB/3

L=zeros([files, columnes])
L[:,:]= 0.299*canalR + 0.587*canalG + 0.114*canalB 

figure(3)
subplot(1,2,1)
imshow(L,cmap='gray')

subplot(1,2,2)
imshow(mitjana,cmap='gray')


#imsave() per guardar la imatge
#savefig() per gravar tot un subplot

tic=time()
print('Temps que triga el programa: {}\n'.format(round(tic-tac,1)))