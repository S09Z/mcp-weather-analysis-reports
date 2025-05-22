import datetime
from utils.fetch_weather import fetch_weather_data
from utils.analyze import analyze_weather
from utils.export_excel import export_to_excel
from utils.upload_drive import upload_to_drive
from utils.notify_discord import notify_discord
from utils.plot_graph import create_weather_plot
from utils.send_email import send_email


def main():
    # 1. Get today's date
    today = datetime.date.today().isoformat()

    # 2. Fetch weather data
    city = "Bangkok"
    weather_data = fetch_weather_data(city)

    # 3. Analyze the data
    analysis = analyze_weather(weather_data)

    # 4. Export to Excel
    excel_file = f"reports/weather_{today}.xlsx"
    export_to_excel(weather_data, analysis, excel_file)

    # 5. Upload to Google Drive
    drive_link = upload_to_drive(excel_file)

    # 6. Create a weather plot image
    image_file = f"reports/weather_{today}.png"
    create_weather_plot(weather_data, image_file)

    # 7. Send Discord notification
    notify_discord(city, analysis, drive_link)

    # 8. Send Gmail with attachments
    send_email(
        subject=f"Daily Weather Report - {today}",
        body="See attached weather report and summary image.",
        attachment_path=excel_file
    )


if __name__ == "__main__":
    main()