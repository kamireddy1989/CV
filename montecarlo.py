# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:47:35 2023

@author: kamir
"""

import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt


n=500

mu=np.array([0.0869,0.04])
co=np.array([[0.0215,-0.00205],[-0.00205,0.0049]])
#sp=(1+np.random.normal(0.0879,0.1465,[n,30]))
amt=np.array([500,500])
amt1=np.array([700,300])
i=0
y=np.ones([n,30])
#y1=np.ones([n,30])

while i<30:
    y[:,i]=np.sum(amt*(1+np.random.multivariate_normal(mu,co,[n])),axis=1)
    #y1[:,i]=np.sum(amt1*(1+np.random.multivariate_normal(mu,co,[n])),axis=1)
    i+=1
    
#y=np.sum(y,axis=1)
#y1=np.sum(y1,axis=1)


#bonds=(1+np.random.normal(0.04,0.07,[n,30]))

#y=np.prod(sp,axis=1)*1000
#y1=np.prod(bonds,axis=1)*300

#res_1=np.array([np.mean(y),np.std(y),np.min(y),np.max(y),np.percentile(y,5),np.percentile(y,95)])
#res_2=np.array([np.mean(y1),np.std(y1),np.min(y1),np.max(y1),np.percentile(y1,5),np.percentile(y1,95)])

#res=np.array([res_1,res_2])

#print(res)


# x=(1+x)*1000
# var=np.linspace(1,6,6)
# pro=np.linspace(95,100,6)
# y=np.percentile(x,[var,pro])
# z=np.array([1.65,1.96,1.98,2.33,2.58])
# skew=sp.skew(x)
# kurt=sp.kurtosis(x)
# stats=np.array([np.mean(x),np.std(x),np.min(x),np.max(x),np.percentile(x,5),np.percentile(x,95)])
# ci=[np.mean(x)-(z*(np.std(x)/(np.sqrt(len(x))))),np.mean(x)+(z*(np.std(x)/(np.sqrt(len(x)))))]
