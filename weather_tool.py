import requests as req
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city):
    url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEATHER_API_KEY')}&units=metric"
    res_weather = req.get(url_weather)
    weather_data = res_weather.json()
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    return temp,description

temp,description = get_weather("mumbai")
print(temp,description)

weather_function = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current temperature and weather conditions for a given city..",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["city"],
    },
}