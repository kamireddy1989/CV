# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 21:30:03 2023

@author: kamir
"""

import pandas_datareader as pdr
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import time

st=time.time()

#Getting the Data
start=dt.datetime(2018,1,1)

#Pick the tickers of the securities for analysis

tickers=["AAPL","TSLA","NVDA","MSFT","BAC","BA","GOOGL","META"]

df=pdr.get_data_stooq(tickers, start)

df_close=df['Close']

df_close=df_close[::-1]

df_close=df_close.to_numpy()

ret=np.log(df_close[1:,:]/df_close[0:-1,:])

#Statistics            

mn=np.mean(ret,axis=0)
sd=np.std(ret,axis=0).reshape(len(ret[0]),1)
sdmat=np.matmul(sd,np.transpose(sd))

cov=np.matmul(np.transpose(ret-mn),(ret-mn))/len(ret)
cor=cov/sdmat

#Montecarlo Simulation

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

#Data Visualization
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

#Printing the output

print(" Weights of different Securities\n")
for idx,i in enumerate(tickers):
    vl=np.round(wt[idx,sr.argmax()],2)*100
    print(" "+i+":",vl)
    
print("\n Portfolio:",np.round(avg_port[sr.argmax()],2),"\n","Volatility:",np.round(avg_vol[sr.argmax()],2),"\n","Sharp Ratio:",np.round(sr[sr.argmax()],2),'\n')

print(f' Time took to run the code:{code_runtime} sec')

