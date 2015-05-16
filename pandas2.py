import pandas as pd
import matplotlib.pylab as plt


# Read the file
raw_data = pd.ExcelFile('Accidents_London.xlsx')
data = raw_data.parse('Sheet1')

print(data.head())

# Convert date to Pandas date/time
data['Date'] = pd.to_datetime(data['Date'])
print(data['Date'][:5])

# Sort by Date
data.sort(['Date'], inplace=True)
print(data.head())

# Create new dataframe meeting the specified criteria
data2 = data[
    (data['Date'] > pd.to_datetime('2000-08-01')) &
    (data['Date'] < pd.to_datetime('2000-08-30'))
]

# Set the Date as the index
data2.set_index('Date', inplace=True)

# Plot the data
data2.plot()
plt.show()
