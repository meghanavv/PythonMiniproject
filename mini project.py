import requests

def get_weather(api_key, city):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city, "aqi": "no"}  # Setting "aqi" to "no" disables air quality data.

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if "error" in data:
            print("City not found.")
        else:
            weather_info = {
                "city": data["location"]["name"],
                "temperature": data["current"]["temp_c"],
                "description": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_kph"],
            }

            print("Weather forecast for", weather_info["city"])
            print("Temperature:", weather_info["temperature"], "°C")
            print("Description:", weather_info["description"])
            print("Humidity:", weather_info["humidity"], "%")
            print("Wind Speed:", weather_info["wind_speed"], "km/h")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual WeatherAPI.com API key.
    api_key = "57f12cd5a6fa439b82d83553232107"
    city = input("Enter the city name: ")
    get_weather(api_key, city)
