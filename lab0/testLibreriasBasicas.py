#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:07:58 2019

@author: ger
"""

import os

import math

import numpy as np

import pandas as pd

from pandas import DataFrame

import matplotlib.pyplot as plt
plt.style.use('ggplot')

os.system('clear')

## Drawing the network.
fig1=plt.figure(1)
x=10
y=30
plt.plot(x, y, 'ko', label='Nodes')
textPosX=x; textPosY=y
offsetX=0.5; offsetY=0
cont=0
texto=str(cont+1)
plt.text(textPosX + offsetX, textPosY + offsetY, texto, rotation=0, size=10)
#end

coorXi=10
coorXj=20
coorYi=30
coorYj=40

RC=15

dij=math.sqrt((coorXi-coorXj )**2+( coorYi-coorYj )**2)
        
if dij<=RC:
    plt.plot([coorXi,coorXj],[coorYi,coorYj],'k--')
#end
        
plt.xlabel('X coordinates')
plt.ylabel('Y coordinates')
plt.title('Network')
#plt.legend()
plt.show()

Cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = DataFrame(Cars, columns= ['Brand', 'Price'])

print(df)

a1=math.ceil(10.3)

print(a1)



## Linux version
#os.system("sudo chown -R ger:ger /home/ger/.wine/") 
        
    



