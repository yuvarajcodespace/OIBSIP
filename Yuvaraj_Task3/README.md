# 🌤️ Weather App

![Python](https://img.shields.io/badge/Python-3.x-3776AB)
![Level](https://img.shields.io/badge/Level-Beginner-8E44AD)
![Status](https://img.shields.io/badge/Status-Completed-2ECC71)
![API](https://img.shields.io/badge/API-OpenWeatherMap-E67E22)

## Description

A command-line **Weather App** built in Python. This project fetches live weather data from the **OpenWeatherMap API** and displays current weather conditions like temperature, humidity, wind speed and visibility in a clean and informative format. It supports any city worldwide and shows descriptions based on weather values.

## Features

- Search weather for any city worldwide 🌍
- Displays current weather conditions with emojis
- Shows local time of the searched city 🕐
- Temperature feel description (Comfortable / Hot / Cold...)
- Humidity level description (Dry / Humid / Very Humid...)
- Wind speed description (Calm / Light Breeze / Storm...)
- Handles invalid city names and network errors gracefully
- Search multiple cities in one session

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming language |
| `requests` library | Fetching data from OpenWeatherMap API |
| `datetime` module | Calculating local time of the city |
| OpenWeatherMap API | Live weather data source |
| JSON | Parsing API response data |

## How to Run

**Step 1** — Install the required library:
```bash
pip install requests
```

**Step 2** — Add your API key in the code:
```python
API_KEY = "your_api_key_here"
```
Get your free API key from [openweathermap.org](https://openweathermap.org)

**Step 3** — Run the program:
```bash
python weather_app.py
```

## Sample Output

```
====================================================
   🌧️  WEATHER IN KOCHI, IN  🌧️
====================================================
  🕐 Local Time   : 08:33 AM
  🌈 Condition    : Light Rain 🌧️
────────────────────────────────────────────────────
  🌡️  Temperature  : 28.34°C    🔥 Hot
  🤔 Feels Like   : 31.34°C
  🔽 Min          : 28.34°C
  🔼 Max          : 28.34°C
────────────────────────────────────────────────────
  💧 Humidity     : 70%      💦 Humid
  💨 Wind Speed   : 2.16 m/s  🍃 Light Breeze
  👁️  Visibility   : 10 km
====================================================
```

## Author

**Yuvaraj.T.K** — Python Intern @ Oasis Infobyte

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/YOUR_USERNAME)

#oasisinfobyte #oasisinfobytefamily #internship #python
