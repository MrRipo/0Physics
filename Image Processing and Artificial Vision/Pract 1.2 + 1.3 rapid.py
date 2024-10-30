# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 10:15:08 2017

@author: Ripo
"""
from __future__ import division, print_function, unicode_literals
from pylab import *
from time import time
from scipy.ndimage.measurements import histogram
from skimage.data import camera
from skimage.morphology import disk,square

close('all')
interactive(True)

'''EXERCICI 2 '''

camer=camera()

imatge_binaria=camer<128
#imatge_binaria1=imatge_binaria*camer

figure('Exercici 2: Contrast')
imshow(imatge_binaria, cmap='gray')

'''EXERCICI 3 '''

camer=camera()
histog=histogram(camer, 0, 255, 256)

cdf = cumsum(histog)

figure('Imatge en gris, histo i histo acumulat', figsize=(15,7))
subplot(3,2,1)
imshow(camer, cmap='gray')
subplot(3,2,3)
plot(histog)
subplot(3,2,4)
plot(cdf)

