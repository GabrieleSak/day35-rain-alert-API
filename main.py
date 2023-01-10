import requests
from api_key import api_key

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 54.687157,
    "lon": 25.279652,
    "appid": api_key,
    "units": "metric",
    "cnt": 5
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_conditions = []

for weather_hourly in weather_data["list"]:
    for item in weather_hourly["weather"]:
        weather_conditions.append(item["id"])

for item in weather_conditions:
    if item < 700:
        print("Bring an Umbrella")
        break

