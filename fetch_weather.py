print("Script started")
import requests

API_KEY = "257a2ffa385800ac839f92a79f693ef8"
CITY = "Chennai"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)