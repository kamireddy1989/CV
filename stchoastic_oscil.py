import pandas as pd
import matplotlib.pyplot as plt

#MACD days use either(12,21,9) or (8,17,9) 

#reading the file in the data frame)
dt=pd.read_csv('stock_data.csv',index_col=0,parse_dates=True)

#14 day High
day14_high=dt['High'].rolling(14).max()
#14 day Low
day14_low=dt['Low'].rolling(14).min()

#Calculating %K 
dt['%K']=(dt['Close']-day14_low)*100/(day14_high-day14_low)

#Calulating %D moving average 3
dt['%D']=dt['%K'].rolling(3).mean()

#Signal
dt['Decision']=dt['%K']>dt['%D']


#Plotting the data
fig,ax=plt.subplots()

dt[['%K','%D']].plot(ax=ax,alpha=0.8)
plt.xlabel('Date')
plt.ylabel('%K & %D')
dt['Close'].plot(ax=ax,secondary_y=True, alpha=0.7)
plt.ylabel('Close Price')
ax.axhline(80,c='r',alpha=0.8)
ax.axhline(20,c='r',alpha=0.8)
plt.grid()
plt.show()
