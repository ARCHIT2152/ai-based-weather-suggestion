import requests as req
from google import genai
from dotenv import load_dotenv
import os
import json

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



client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather conditions for a given city.",
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

available_functions = {
    "get_weather": lambda city: {
        "city": city, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)