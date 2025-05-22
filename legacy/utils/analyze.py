import pandas as pd
from datetime import datetime

def analyze_weather(data):
    if not data or "list" not in data:
        return {"max_temp": None}
        
    temps = [item["main"]["temp"] for item in data["list"]]
    humidities = [item["main"]["humidity"] for item in data["list"]]
    rain_count = sum(1 for item in data["list"] if "rain" in item)
    
    return {
        "max_temp": max(temps),
        "min_temp": min(temps),
        "avg_humidity": sum(humidities) / len(humidities),
        "rain_chance": (rain_count / len(data["list"])) * 100
    }
