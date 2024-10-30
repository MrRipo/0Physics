# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 14:31:45 2017

@author: Ripo
"""
from __future__ import division, print_function, unicode_literals
from pylab import *
from time import time
from scipy.ndimage.measurements import histogram
from skimage.data import astronaut
from skimage.filters.rank import entropy
astro=astronaut()

astro_verd=astro[:,:,1]

entropi_1=0
histogram_1=histogram(astro_verd,0,255,bins=256)
probab=histogram_1/(histogram_1.sum()) #divdir per 512*512 és el mateix
ent=-(probab*log2(probab)).sum()
for kk in probab:
    if kk==0:
        s_1=0
    else:
        s_1=-kk*log2(kk)
    entropi_1=entropi_1 +s_1
    
print(ent,entropi_1)
'''

#hem de fer veínatges de 11x11 per cada nivell de grisos
#numpy.pad per crear una matriu mes gran i desprès retallar per arreglar el problema de les vores

S=zeros((512,512))
for ii in range(513):#range(imatge.shape[0 o 1])
    for jj in range(513):
        entropi=0
        #pixels 0-4 i 507-512
        if ii<5 or jj<5:
            continue
        elif ii>506 or jj>506:
            continue
        else:
            astro_verd_veinatge=astro_verd[ii-5:ii+6,jj-5:jj+6]
            astro_verd_histog=histogram(astro_verd_veinatge,0,255,bins=256)
            probab=astro_verd_histog/121#( dividir per astro_verd_histog.sum())
            for k in probab:
                if k==0:
                    s=0
                else:
                    s=-k*log2(k)
                entropi=entropi+s
            S[ii,jj]=entropi    
 
 
 
 
 
figure(1,figsize=(15,7))  

imshow(S)
colorbar()     

#en la funcio entropy():
#en comptes d'un quadrat, també li pots enviar una matriu de uns i zeros on allà hi hagi un 1 et calcula l'entropia i on hi hagi un zero no ho calcula
entropia=entropy(astro_verd, square(11))#en un disc de diametre 5,quadrat de 11
figure(2)
imshow(entropia)
colorbar()

S_sum=0
S_mes=0
S_mesigual=0
for pi in histo_normalitzat:
    S_sum=(pi*log2(pi)).sum()
    S_mes=S_mes+pi*log2(pi)
    S_mesigual+=pi*log2(pi)
print(-S_sum,-S_mes,-S_mesigual)
'''