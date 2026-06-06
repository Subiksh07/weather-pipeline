import requests
import psycopg2
from datetime import datetime

API_KEY = "b1756e4521b2746c1b0ecae96fc3b76d"
CITY = "Chennai"

# Step 1 - Fetch weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

weather_data = {
    "city": data["name"],
    "temperature": data["main"]["temp"],
    "feels_like": data["main"]["feels_like"],
    "humidity": data["main"]["humidity"],
    "description": data["weather"][0]["description"],
    "wind_speed": data["wind"]["speed"],
    "timestamp": datetime.now()
}

print("✅ Weather Data Fetched!")

# Step 2 - Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="weather_db",
    user="postgres",
    password="subi"
)
cursor = conn.cursor()

print("✅ Connected to PostgreSQL!")

# Step 3 - Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id SERIAL PRIMARY KEY,
        city VARCHAR(100),
        temperature FLOAT,
        feels_like FLOAT,
        humidity INT,
        description VARCHAR(200),
        wind_speed FLOAT,
        timestamp TIMESTAMP
    )
""")

print("✅ Table Ready!")

# Step 4 - Insert data
cursor.execute("""
    INSERT INTO weather (city, temperature, feels_like, humidity, description, wind_speed, timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", (
    weather_data["city"],
    weather_data["temperature"],
    weather_data["feels_like"],
    weather_data["humidity"],
    weather_data["description"],
    weather_data["wind_speed"],
    weather_data["timestamp"]
))

conn.commit()
cursor.close()
conn.close()

print("✅ Data Stored in PostgreSQL Successfully!")