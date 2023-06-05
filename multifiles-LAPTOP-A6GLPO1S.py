# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:25:07 2021

@author: kamir
"""

import pandas as pd
import numpy as np
import glob2 as glob
#from fileext import fileext
import matplotlib.pyplot as plt
import time

st=time.time()

path='C:\\Users\\kamir\\OneDrive\\Desktop\\Certificates\\Srinu\\Matlab\\Covariance\\*.csv'
files=glob.glob(path)
#files=fileext('C:/Users/kamir/OneDrive/Desktop/Certificates/Srinu/Matlab/Covariance/ETF','csv',True)
dt=pd.concat((pd.read_csv(file) for file in files),ignore_index=True,axis=1)
cols=np.arange(5,len(dt.columns),7)

dt1=dt.iloc[:,cols]

dt1=dt1.to_numpy()


ret=np.log(dt1[1:,:]/dt1[0:-1,:])

              

mn=np.mean(ret,axis=0)
sd=np.std(ret,axis=0).reshape(len(ret[0]),1)
sdmat=np.matmul(sd,np.transpose(sd))

cov=np.matmul(np.transpose(ret-mn),(ret-mn))/len(ret)
cor=cov/sdmat


n=25000

wt=np.random.random([ret.shape[1],n])

wt/=np.sum(wt,axis=0)

avg_port=np.matmul(np.transpose(wt),mn)*252*100

i=0
avg_vol=np.zeros(n)
while(i<n):
    avg_vol[i]=np.sqrt(np.matmul((np.matmul(np.transpose(wt[:,i]),cov)),wt[:,i])*252)*100
    i+=1
    
sr=avg_port/avg_vol

fig,ax=plt.subplots(2,1)

ax[0].scatter(avg_vol,avg_port,c=sr,alpha=0.5)
ax[0].scatter(avg_vol[sr.argmax()],avg_port[sr.argmax()],c='r',alpha=0.5)
ax[0].grid()
ax[0].set_xlabel('Avg_Volatility')
ax[0].set_ylabel('Avg_Return')
ax[0].scatter(avg_vol,avg_port,c=sr,alpha=0.5)
ax[0].scatter(avg_vol[sr.argmax()],avg_port[sr.argmax()],c='r',alpha=0.5)
ax[1].scatter(np.arange(n),sr,c=sr,alpha=0.5)
ax[1].scatter(sr.argmax(),sr[sr.argmax()],c='r',alpha=0.5)
ax[1].set_xlabel('Number of Portfolios')
ax[1].set_ylabel('Sharp Ratio')
ax[1].grid()

code_runtime=round(time.time()-st,2)

print(np.round(wt[:,sr.argmax()],3)*100,avg_port[sr.argmax()],avg_vol[sr.argmax()],sr[sr.argmax()],'\n')

print(f'Time took to run the code:{code_runtime} sec')

