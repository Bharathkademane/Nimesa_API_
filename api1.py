import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_hourly_weather_forecast():

    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    return data
    

def get_temp_on_date(data, date):
    for entry in data["list"]:
        if entry["dt_txt"].startswith(date):
            temperature = entry["main"].get("temp", "")
            return temperature
    return None

def get_wind_speed_on_date(data, date):
    for entry in data["list"]:
        if entry["dt_txt"].startswith(date):
            wind_speed = entry["wind"].get("speed", "")
            return wind_speed
    return None

def get_pressure_on_date(data, date):
    for entry in data["list"]:
        if entry["dt_txt"].startswith(date):
            pressure = entry["main"].get("pressure", "")
            return pressure
    return None

def print_temp():
    date = input("Enter the date (YYYY-MM-DD): ")
    weather_data = get_hourly_weather_forecast()
    if weather_data:
        temperature = get_temp_on_date(weather_data, date)
        if temperature:
            print(f"Temperature on {date}: {temperature}°C")
        else:
            print(f"No temperature data available for {date}.")
    else:
        print("Weather data not available. Please try again later.")

def print_wind_speed():
    date = input("Enter the date (YYYY-MM-DD): ")
    weather_data = get_hourly_weather_forecast()
    if weather_data:
        wind_speed = get_wind_speed_on_date(weather_data, date)
        if wind_speed:
            print(f"Wind Speed on {date}: {wind_speed} m/s")
        else:
            print(f"No wind speed data available for {date}.")
    else:
        print("Weather data not available. Please try again later.")

def print_pressure():
    date = input("Enter the date (YYYY-MM-DD): ")
    weather_data = get_hourly_weather_forecast()
    if weather_data:
        pressure = get_pressure_on_date(weather_data, date)
        if pressure:
            print(f"Pressure on {date}: {pressure} hPa")
        else:
            print(f"No pressure data available for {date}.")
    else:
        print("Weather data not available. Please try again later.")

if __name__ == "__main__":
    while True:
        print("1. Get temperature")
        print("2. Get wind speed")
        print("3. Get pressure")
        print("0. Exit")

        print("NOTE:Select any Date between 2019-03-27 to 2019-03-31")
        user_option = input("Enter your choice: ")

        if user_option == "1":
            print_temp()
        elif user_option == "2":
            print_wind_speed()
        elif user_option == "3":
            print_pressure()
        elif user_option == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
