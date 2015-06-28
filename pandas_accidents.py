import pandas as pd


# Read the file
data = pd.read_csv("Accidents7904.csv", low_memory=False)
# Output the number of rows
print("Total rows: {0}".format(len(data)))
# See which headers are available
# print(list(data))

print("\nAccidents")
print("-----------")

# Accidents which happened on a Sunday
accidents_sunday = data[data.Day_of_Week == 1]
print("Accidents which happened on a Sunday: {0}".format(
    len(accidents_sunday)))

# Accidents which happened on a Sunday, > 20 cars
accidents_sunday_twenty_cars = data[
    (data.Day_of_Week == 1) & (data.Number_of_Vehicles > 20)]
print("Accidents which happened on a Sunday involving > 20 cars: {0}".format(
    len(accidents_sunday_twenty_cars)))

# Accidents which happened on a Sunday, > 20 cars, in the rain
accidents_sunday_twenty_cars_rain = data[
    (data.Day_of_Week == 1) & (data.Number_of_Vehicles > 20) &
    (data.Weather_Conditions == 2)]
print("Accidents which happened on a Sunday involving > 20 cars in the rain: {0}".format(
    len(accidents_sunday_twenty_cars_rain)))

# Accidents in London on a Sunday
london_data = data[data['Police_Force'] == 1 & (data.Day_of_Week == 1)]
print("\nAccidents in London from 1979-2004 on a Sunday: {0}".format(
    len(london_data)))

# Convert date to Pandas date/time
london_data_2000 = london_data[
    (pd.to_datetime(london_data['Date'], coerce=True) >
        pd.to_datetime('2000-01-01', coerce=True)) &
    (pd.to_datetime(london_data['Date'], coerce=True) <
        pd.to_datetime('2000-12-31', coerce=True))
]
print("Accidents in London in the year 2000 on a Sunday: {0}".format(
    len(london_data_2000)))

# Update header
london_data_2000.rename(
    columns={'\xef\xbb\xbfAccident_Index': 'Accident_Index'}, inplace=True)

# Save to Excel
writer = pd.ExcelWriter(
    'London_Sundays_2000.xlsx', engine='xlsxwriter')
london_data_2000.to_excel(writer, 'Sheet1')
writer.save()
