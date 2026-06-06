import requests

API_KEY = "b1756e4521b2746c1b0ecae96fc3b76d"
CITY = "Chennai"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Extract only what we need
weather_data = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "feels_like": data["main"]["feels_like"],
    "humidity": data["main"]["humidity"],
    "description": data["weather"][0]["description"],
    "wind_speed": data["wind"]["speed"]
}

print("✅ Weather Data Fetched!")
print(weather_data)