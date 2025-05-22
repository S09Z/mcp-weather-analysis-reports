import pytest
from utils.analyze import analyze_weather

sample_data = {
    "list": [
        {
            "dt_txt": "2025-05-22 12:00:00",
            "main": {"temp": 30.5, "humidity": 60},
            "weather": [{"description": "clear sky"}]
        },
        {
            "dt_txt": "2025-05-22 15:00:00",
            "main": {"temp": 32.0, "humidity": 55},
            "weather": [{"description": "light rain"}],
            "rain": {"3h": 0.5}
        },
        {
            "dt_txt": "2025-05-22 18:00:00",
            "main": {"temp": 28.3, "humidity": 70},
            "weather": [{"description": "scattered clouds"}]
        }
    ]
}

def test_analyze_weather():
    result = analyze_weather(sample_data)
    assert result["max_temp"] == 32.0
    assert result["min_temp"] == 28.3
    assert round(result["avg_humidity"], 2) == 61.67
    assert result["rain_chance"] == pytest.approx(33.33, rel=1e-2)

def test_analyze_weather_empty():
    result = analyze_weather({})
    assert result["max_temp"] is None
