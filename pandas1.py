import pandas as pd
import pdb

data = pd.read_csv("Accidents7904.csv")
print len(data)

# See what headers are available
list(data)

# Accidents which killed more than 10 people
data1 = data[data.Number_of_Casualties > 10]
print data1.head()
print len(data1)

# Accidents which killed at leat 10 people and had 20 cars
data2 = data[(data.Number_of_Casualties > 10) & (data.Number_of_Vehicles > 20)]
print len(data2)

# Same as above, but when it was raining
data3 = data[(data.Number_of_Casualties > 10) & (data.Number_of_Vehicles > 20) & (data.Weather_Conditions  == 2)]

print len(data3)
#Out[29]: 6

# Incidents when more than 4 people died due to snow in London
data6 = data[(data.Weather_Conditions == 3) & (data.Number_of_Casualties > 5) & (data.Police_Force == 1)]
print len(data6)
#data6.head()

# Only police force in London
data_london = data[data['Police_Force'] == 1]
print data_london[:5]

# Extract only the fields we need
data_london_new2 = data_london[['Date', 'Number_of_Casualties']]
print data_london_new2.head()

writer = pd.ExcelWriter('Accidents_London.xlsx')
data_london_new2.to_excel(writer,'Sheet1')
writer.save()
