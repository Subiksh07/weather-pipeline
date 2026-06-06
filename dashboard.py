import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="wide")
st.title("🌤️ Chennai Weather Pipeline Dashboard")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="weather_db",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD")
)

# Fetch data
df = pd.read_sql("SELECT * FROM weather ORDER BY timestamp DESC", conn)
conn.close()

# Latest reading
latest = df.iloc[0]

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("🌡️ Temperature", f"{latest['temperature']}°C")
col2.metric("🤔 Feels Like", f"{latest['feels_like']}°C")
col3.metric("💧 Humidity", f"{latest['humidity']}%")
col4.metric("💨 Wind Speed", f"{latest['wind_speed']} m/s")

st.subheader("📊 Temperature Over Time")
fig = px.line(df, x="timestamp", y="temperature", title="Temperature Trend")
st.plotly_chart(fig, use_container_width=True)

st.subheader("💧 Humidity Over Time")
fig2 = px.bar(df, x="timestamp", y="humidity", title="Humidity Trend")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📋 Raw Data")
st.dataframe(df)