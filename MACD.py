import pandas as pd
import matplotlib.pyplot as plt

#MACD days use either(12,21,9) or (8,17,9) 

#reading the file in the data frame)
dt=pd.read_csv('stock_data.csv',index_col=0,parse_dates=True)

#perform exponential smoothing
exp1=dt['Close'].ewm(span=8,adjust=False).mean()
exp2=dt['Close'].ewm(span=17,adjust=False).mean()

#create  a new columns {MACD,Signal, Decision)
dt['MACD']=exp1-exp2

dt['Signal']=dt['MACD'].ewm(span=9,adjust=False).mean()

dt['Decision']=dt['MACD']>dt['Signal']


#Plotting the data
fig,ax=plt.subplots()

dt[['MACD','Signal']].plot(ax=ax)
plt.xlabel('Date')
plt.ylabel('MACD & Signal')

dt['Close'].plot(ax=ax,secondary_y=True, alpha=0.4)
plt.ylabel('Close Price')
plt.grid()
plt.show()


