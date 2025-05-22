import requests
import os

def notify_discord(city, analysis, drive_link):
    webhook_url = os.getenv("DISCORD_WEBHOOK")
    if not webhook_url:
        print("DISCORD_WEBHOOK not set")
        return

    content = (
        f"📍 **{city} Weather Report**\n"
        f"🌡️ Max Temp: {analysis['max_temp']}°C\n"
        f"🌡️ Min Temp: {analysis['min_temp']}°C\n"
        f"💧 Avg Humidity: {analysis['avg_humidity']:.2f}%\n"
        f"☔ Rain Chance: {analysis['rain_chance']}%\n"
        f"📄 [Excel Report]({drive_link})"
    )

    payload = {"content": content}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        print(f"Failed to send Discord notification: {response.status_code}")