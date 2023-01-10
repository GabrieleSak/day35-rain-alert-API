import requests
from api_key import api_key

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"


parameters = {
    "lat": 54.687157,
    "lon": 25.279652,
    "appid": api_key,
    "units": "metric",
    "cnt": 17
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)