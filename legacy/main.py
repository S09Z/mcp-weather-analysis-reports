import datetime
import os
import uuid
from utils.fetch_weather import fetch_weather_data
from utils.analyze import analyze_weather
from utils.export_excel import export_to_excel
# from utils.upload_drive import upload_to_drive
from utils.notify_discord import notify_discord
from utils.plot_graph import create_weather_plot
from utils.send_email import send_email

base_dir = os.path.dirname(__file__)

def main():
    # 1. Get today's date
    today = datetime.date.today().isoformat()
    unique_id = str(uuid.uuid4())

    # 2. Fetch weather data
    city = "Bangkok"
    weather_data = fetch_weather_data(city)

    # 3. Analyze the data
    analysis = analyze_weather(weather_data)

    # 4. Export to Excel
    excel_name = f"weather_{unique_id}_{today}.xlsx"
    excel_file = os.path.abspath(os.path.join(base_dir, "reports", "data", excel_name))
    export_to_excel(weather_data, analysis, excel_file)
    # 5. Upload to Google Drive
    # drive_link = upload_to_drive(excel_file)

    # 6. Create a weather plot image
    
    image_name = f"weather_{unique_id}_{today}.png"
    image_file = os.path.abspath(os.path.join(base_dir, "reports", "visualize", image_name))
    create_weather_plot(weather_data, image_file)

    # 7. Send Discord notification
    notify_discord(city, analysis, "")

    # 8. Send Gmail with attachments
    send_email(
        subject=f"Daily Weather Report - {today}",
        body="See attached weather report and summary image.",
        attachment_path=image_file
    )


if __name__ == "__main__":
    main()