import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('stock_data.csv',index_col=0,parse_dates=True)

#calculate the difference
df['Delta']=df['Close'].diff()

#calculate the delta value >0 and <0
up=df['Delta'].clip(0)
down=df['Delta'].clip(upper=0)*-1

# calculate the EMA up and down

up_ema=up.ewm(span=13,adjust=False).mean()
down_ema=down.ewm(span=13,adjust=False).mean()

#calculate rs

rs=up_ema/down_ema

#calculate RSI
df['RSI']=100-(100/(1+rs))


#plotting the RSI

fig,(ax,ax2)=plt.subplots(2)
df['Close'].plot(ax=ax,alpha=0.6)
ax.grid()
plt.tight_layout()

df['RSI'].plot(ax=ax2,alpha=0.8)
ax2.axhline(70,c='r',linestyle='--')
ax2.axhline(30,c='r',linestyle='--')
ax2.grid()
plt.show()
