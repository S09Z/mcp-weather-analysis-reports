import matplotlib.pyplot as plt
import os

def create_weather_plot(data, output_file):
    if data is None:
        print("No data to plot")
        return

    forecasts = data["list"]
    times = [entry["dt_txt"] for entry in forecasts]
    temps = [entry["main"]["temp"] for entry in forecasts]
    humidity = [entry["main"]["humidity"] for entry in forecasts]

    plt.figure(figsize=(12, 6))
    plt.plot(times, temps, label="Temperature (°C)", marker='o')
    plt.plot(times, humidity, label="Humidity (%)", marker='x')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.title("Weather Forecast")
    plt.legend()
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file)
    plt.close()