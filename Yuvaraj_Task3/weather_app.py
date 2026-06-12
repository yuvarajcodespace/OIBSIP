# ============================================================
#   WEATHER APP
#   Oasis Infobyte Python Internship - Task 3
#   Author: Yuvaraj.T.K
# ============================================================

import requests
from datetime import datetime, timezone, timedelta

API_KEY  = "587b95823d03f922274ee5f500ea1a01"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    try:
        params   = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data     = response.json()

        if response.status_code == 200:
            return data
        elif response.status_code == 404:
            print(f"\n  ❌ City '{city}' not found! Please check the spelling.\n")
        elif response.status_code == 401:
            print("\n  ❌ Invalid API key! Please check your API key.\n")
        else:
            print(f"\n  ❌ Could not fetch data. (Error Code: {response.status_code})\n")

    except requests.exceptions.ConnectionError:
        print("\n  ❌ No internet connection! Please check your network.\n")
    except Exception as e:
        print(f"\n  ❌ Something went wrong: {e}\n")

    return None


def get_weather_emoji(condition):
    c = condition.lower()
    if "clear"   in c: return "☀️"
    if "cloud"   in c: return "☁️"
    if "drizzle" in c: return "🌦️"
    if "rain"    in c: return "🌧️"
    if "thunder" in c: return "⛈️"
    if "snow"    in c: return "❄️"
    if "mist"    in c or "fog" in c or "haze" in c: return "🌫️"
    return "🌤️"


def get_temp_desc(temp):
    if temp < 0:   return "🥶 Freezing"
    if temp < 10:  return "🧊 Very Cold"
    if temp < 18:  return "🌬️ Cold"
    if temp < 24:  return "😊 Comfortable"
    if temp < 30:  return "🌤️ Warm"
    if temp < 36:  return "🔥 Hot"
    return "🌋 Extremely Hot"


def get_humidity_desc(humidity):
    if humidity < 30:  return "🏜️ Very Dry"
    if humidity < 50:  return "✅ Comfortable"
    if humidity < 70:  return "💧 Moderate"
    if humidity < 85:  return "💦 Humid"
    return "🌊 Very Humid"


def get_wind_desc(speed):
    if speed < 0.5:  return "🪨 Calm"
    if speed < 3:    return "🍃 Light Breeze"
    if speed < 8:    return "💨 Moderate Wind"
    if speed < 14:   return "🌬️ Strong Wind"
    if speed < 20:   return "⚠️  Very Strong Wind"
    return "🌀 Storm!"


def get_local_time(offset):
    local = datetime.now(timezone.utc) + timedelta(seconds=offset)
    return local.strftime("%I:%M %p")


def get_city_name():
    while True:
        city = input("\n  🔍 Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            return None
        if not city:
            print("  ❌ City name cannot be empty! Please try again.")
        elif any(char.isdigit() for char in city):
            print("  ❌ City name should not contain numbers! Please try again.")
        else:
            return city


def ask_search_again():
    while True:
        choice = input("\n  🔄 Search another city? (yes / no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("  ❌ Invalid input! Please type 'yes' or 'no'.")


def display_weather(data):
    city       = data["name"]
    country    = data["sys"]["country"]
    temp       = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    temp_min   = data["main"]["temp_min"]
    temp_max   = data["main"]["temp_max"]
    humidity   = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    condition  = data["weather"][0]["description"].title()
    visibility = data.get("visibility", 0) // 1000
    local_time = get_local_time(data["timezone"])
    emoji      = get_weather_emoji(condition)

    print("\n" + "=" * 52)
    print(f"   {emoji}  WEATHER IN {city.upper()}, {country}  {emoji}")
    print("=" * 52)
    print(f"  🕐 Local Time   : {local_time}")
    print(f"  🌈 Condition    : {condition} {emoji}")
    print("─" * 52)
    print(f"  🌡️  Temperature  : {temp}°C    {get_temp_desc(temp)}")
    print(f"  🤔 Feels Like   : {feels_like}°C")
    print(f"  🔽 Min          : {temp_min}°C")
    print(f"  🔼 Max          : {temp_max}°C")
    print("─" * 52)
    print(f"  💧 Humidity     : {humidity}%      {get_humidity_desc(humidity)}")
    print(f"  💨 Wind Speed   : {wind_speed} m/s  {get_wind_desc(wind_speed)}")
    print(f"  👁️  Visibility   : {visibility} km")
    print("=" * 52)


def main():
    print("=" * 52)
    print("      🌤️   WELCOME TO WEATHER APP   🌤️")
    print("=" * 52)

    while True:
        city = get_city_name()

        if city is None:
            print("\n  👋 Thank you for using Weather App! Goodbye.\n")
            break

        data = get_weather(city)

        if data:
            display_weather(data)

        if not ask_search_again():
            print("\n  👋 Thank you for using Weather App! Goodbye.\n")
            break


if __name__ == "__main__":
    main()
