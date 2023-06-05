import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/home/sri/Documents/Python/stock_data.csv',index_col=0,parse_dates=True)

ret=df['Adj Close'].values
ret=np.log(ret[1:]/ret[0:-1])*100

ls=[7,21,50]

for i in ls:
    df['Mavg_'+str(i)]=df['Close'].rolling(i).mean()
    df['Mavg_'+str(i)].plot()

df['Signal']=df['Close']>df['Mavg_21']

df['Close'].plot()
plt.legend(df.columns[6:-1])
plt.grid()
plt.show()
