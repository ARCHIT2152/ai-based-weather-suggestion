import requests as req

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
city = input("enter city: ")
url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('WEATHER_API_KEY')}&units=metric"
res_weather = req.get(url_weather)

weather_data = res_weather.json()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
temp = weather_data["main"]["temp"]
description = weather_data["weather"][0]["description"]
prompt = f"""You are a Weather Data Analyst. 
The current weather in {city} is {temp}°C with {description}.
Based on this data, give me:
1. Outfit suggestions (fabric, layers, etc.)
2. Hydration or dietary tips
3. Any precautions I should take today
"""

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
)

print(interaction.output_text)

