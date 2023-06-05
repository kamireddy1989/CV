# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:58:44 2021

@author: kamir
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dt=pd.read_csv('C:/Users/kamir/OneDrive/Desktop/Python/mreg1.csv')
x=dt.to_numpy()
y=x[:,-1]
c=np.ones(len(x))
mat=np.column_stack([c,x[:,0:-1]])

res=np.matmul(np.linalg.inv(np.matmul(np.transpose(mat),mat)),np.matmul(np.transpose(mat),y))

res1=np.linalg.inv(np.matmul(np.transpose(mat),mat))
k=np.matmul(mat,res)
    
err=y-k

sse=np.sum((y-k)**2)
x1=np.arange(1,len(x)+1,1)
plt.plot(x1,y,'o')
plt.grid()
plt.plot(x1,k)
plt.legend(['Actual','Predicted'])
    

#mat1=np.column_stack([c,x,y])   
#mat2=mat1[:,0:1]

