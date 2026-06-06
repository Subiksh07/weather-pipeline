# 🌤️ Weather Data Pipeline

An end-to-end data engineering project that automatically collects, stores, and visualizes real-time weather data.

## 📌 Project Overview
This pipeline fetches live weather data from OpenWeatherMap API every hour, stores it in PostgreSQL database, and displays it on an interactive Streamlit dashboard.

## 🛠️ Tools & Technologies
| Tool | Purpose |
|---|---|
| Python | Data fetching & transformation |
| PostgreSQL | Data storage |
| Apache Airflow | Pipeline automation |
| Streamlit | Dashboard & visualization |
| Plotly | Interactive charts |
| Git/GitHub | Version control |

## 📊 Dashboard Features
- Live temperature display
- Feels like temperature
- Humidity percentage
- Wind speed
- Temperature trend chart
- Humidity trend chart
- Raw data table

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Subiksh07/weather-pipeline.git
cd weather-pipeline
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install requests psycopg2-binary pandas streamlit plotly python-dotenv
```

### 4. Set up environment variables
Create a `.env` file:
WEATHER_API_KEY=your_api_key_here
POSTGRES_PASSWORD=your_password_here

### 5. Run the dashboard
```bash
streamlit run dashboard.py
```

### 6. Start Airflow
```bash
source ~/airflow_env/bin/activate
airflow standalone
```

## 👨‍💻 Author
Subiksha - Data Engineering Project