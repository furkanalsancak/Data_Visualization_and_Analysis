import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('fivethirtyeight')


data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']


plt.plot_date(price_date, price_close, linestyle='solid') #marker=None
plt.gcf().autofmt_xdate() #get current figure

#to format dates
# date_format = mpl_dates.DateFormatter('%b, %d, %Y')
# plt.gca().xaxis.set_major_formatter(date_format) #get current axis

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')


plt.tight_layout()

plt.show()

