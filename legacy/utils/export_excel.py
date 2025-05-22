import pandas as pd
import os

def export_to_excel(weather_data, analysis, filename):
    if weather_data is None:
        print("No data to export")
        return

    forecasts = weather_data["list"]

    # เตรียมข้อมูลรายชั่วโมง
    rows = []
    for entry in forecasts:
        rows.append({
            "datetime": entry["dt_txt"],
            "temp": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "weather": entry["weather"][0]["description"],
            "rain_mm": entry.get("rain", {}).get("3h", 0)
        })

    df = pd.DataFrame(rows)

    # เขียนลง Excel
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Forecast")

        # เขียนผลวิเคราะห์
        analysis_df = pd.DataFrame([analysis])
        analysis_df.to_excel(writer, index=False, sheet_name="Summary")