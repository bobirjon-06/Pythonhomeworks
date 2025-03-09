import requests

def get_weather(city, api):
    url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {
        'q': city,
        'appid': api,
        'units' : 'metric'

    }
    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    city = "Tashkent"
    api_key = "b3f4bbfd3df40854df5d95d6a4556c93" 
    get_weather(city, api_key)