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
    return {"city": city, "temp": temp, "description": description}



client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
def temp_convertor(temp, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return temp

    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (temp * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (temp - 32) * 5/9
    else:
        raise ValueError(f"Unsupported conversion: {from_unit} -> {to_unit}")


convertor = {
    "type": "function",
    "name": "temp_convertor",
    "description": "Converts a temperature value between Celsius and Fahrenheit.",
    "parameters": {
        "type": "object",
        "properties": {
            "temp": {
                "type": "number",
                "description": "The temperature value to convert.",
            },
            "from_unit": {
                "type": "string",
                "description": "Unit of the input temperature. Must be 'celsius' or 'fahrenheit'.",
            },
            "to_unit": {
                "type": "string",
                "description": "Target unit to convert to. Must be 'celsius' or 'fahrenheit'.",
            },
        },
        "required": ["temp", "from_unit", "to_unit"],
    },
}
available_functions = {
    "get_weather": get_weather,
    "temp_convertor" : temp_convertor,
}


user_input = input("Ask me anything: ")
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=user_input,
        tools=[weather_tool,convertor],
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