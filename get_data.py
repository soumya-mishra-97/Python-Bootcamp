import requests
from datetime import datetime, timedelta

latitude = 18.52
longitude = 73.85

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
print(f"Paris temperature: {paris_temp}°C")
print(f"Tokyo temperature: {tokyo_temp}°C")
