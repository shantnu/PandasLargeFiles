import pandas as pd


# Read the file
data = pd.read_csv("Accidents7904.csv", low_memory=False)
# Output the number of rows
print("Total rows: {0}".format(len(data)))
# See what headers are available
# print(list(data))

print("\n Accidents")
print("-----------")

# Accidents which killed > 10 people
ten_deaths = data[data.Number_of_Casualties > 10]
print("> 10 people died: {0}".format(
    len(ten_deaths)))

# Accidents which killed > 10 people, > 20 cars
ten_deaths_twenty_cars = data[
    (data.Number_of_Casualties > 10) & (data.Number_of_Vehicles > 20)]
print("> 10 people died involving > 20 cars: {0}".format(
    len(ten_deaths_twenty_cars)))

# Accidents which killed > 10 people, > 20 cars, in the rain
ten_deaths_twenty_cars_rain = data[
    (data.Number_of_Casualties > 10) & (data.Number_of_Vehicles > 20) &
    (data.Weather_Conditions == 2)]
print("> 10 people died involving > 20 cars in the rain: {0}".format(
    len(ten_deaths_twenty_cars_rain)))

# All the accidents in London from 1979-2004
london_accidents = data[data['Police_Force'] == 1]
london_accidents_date_casualties = london_accidents[[
    'Date', 'Number_of_Casualties']]
print("\nTotal accidents in London from 1979-2004: {0}\n".format(
    len(london_accidents_date_casualties)))
print(london_accidents_date_casualties.head(10))

# Save to Excel
writer = pd.ExcelWriter(
    'Accidents_London.xlsx', engine='xlsxwriter')
london_accidents_date_casualties.to_excel(writer, 'Sheet1')
writer.save()
