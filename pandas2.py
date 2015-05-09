import pandas as pd
import matplotlib.pylab as plt

raw_data = pd.ExcelFile('Accidents_London.xlsx')
data = raw_data.parse('Sheet1')

print data.head()

data['Date'] = pd.to_datetime(data['Date'])
print data['Date'][:5]

data.sort(['Date'], inplace=True)
print data.head()

data2 = data[(data['Date'] > pd.to_datetime('2000-08-01')) & (data['Date'] < pd.to_datetime('2000-08-30'))]

data2.set_index('Date', inplace=True)
print data2.head()

data2.plot()
plt.show()


