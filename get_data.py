import requests
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

latitude = 18.520430
longitude = 73.856743

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()

print(data)
type(data)
data.keys()
temp = data["current"]["temperature_2m"]
print(f"Current temperature at latitude {latitude} and longitude {longitude} is: {temp}°C")

def get_temperature(lat, long):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m")
    data = response.json()
    temp = data["current"]["temperature_2m"]
    return temp
paris_temp = get_temperature(48.25, 2.35)
tokyo_temp = get_temperature(35.68, 169.69)
pune_temp = get_temperature(18.520430, 73.856743)
print(f"Paris temperature: {paris_temp}°C")
print(f"Tokyo temperature: {tokyo_temp}°C")
print(f"Pune temperature: {pune_temp}°C")

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Formats dates for API (YYYY-MM-DD)
str_date = week_ago.strftime("%Y-%m-%d")
lst_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=18.520430&longitude=73.856743&start_date={str_date}&end_date={lst_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

'''
Pandas is the library to use it for the data manipulating, analyze the data. It creates the Tabular format data 
like rows and colums so easily data is readable and uderstandable.
2 parts: Data frame and Series
'''
daily_data = data["daily"]
# Create the tabular data
df = pd.DataFrame({
    'date': daily_data["time"],
    'max_temp': daily_data["temperature_2m_max"],
    'min_temp': daily_data["temperature_2m_min"]
})
df['date'] = pd.to_datetime(df['date'])
print(df)

'''
matplotlib.pyplot is the framework to create the charts for generating the reports. 
like in here you have to create the temprature report for daily basis so in here you can use it as to create a chart show the 
required data in here. it's best for data visulasation.
'''
# Create the plot
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['max_temp'], marker = 'o', label = 'Max Temp')
plt.plot(df['date'], df['min_temp'], marker = 'o', label = 'Min Temp')

# Add label and title
plt.xlabel('Date')
plt.ylabel('Temp (°C)')
plt.title('Pune Weather - Past 7 days')
plt.legend()

# Rotate x-labels for readability
plt.xticks(rotation = 45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

# Create data folder if it's not exist
if  not os.path.exists('data'):
    os.mkdir('data')
    
# Save to csv
df.to_csv('data/pune_weather.csv', index = False)
print('Data saved')