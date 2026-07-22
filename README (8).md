# 🌤️ Weather AI Suggestion App

A Python command-line application that combines real-time weather data with generative AI to deliver personalized, context-aware daily recommendations — covering clothing, hydration, and safety precautions.

This project demonstrates **API chaining**: using the structured output of one API (weather data) as the input to another (an LLM), enabling the model to reason over real-world data rather than generate generic responses.

---

## ✨ Features

- Fetches live weather conditions for any city worldwide via the OpenWeatherMap API
- Uses Google's Gemini API to generate tailored, human-readable advice based on that data
- Assigns the LLM a "Weather Data Analyst" persona for more structured, higher-quality responses
- Secure credential handling — no API keys are ever hardcoded in source

---

## 🛠️ Tech Stack

| Component        | Technology                                   |
|-------------------|-----------------------------------------------|
| Language          | Python 3                                     |
| Weather Data      | [OpenWeatherMap API](https://openweathermap.org/api) |
| AI Reasoning      | [Google Gemini API](https://ai.google.dev/) (`google-genai`) |
| Config Management | `python-dotenv`                              |
| HTTP Requests     | `requests`                                   |

---

## ⚙️ How It Works

1. **Input** — User enters a city name
2. **Fetch** — App sends a `GET` request to OpenWeatherMap and retrieves current temperature and conditions
3. **Parse** — Relevant fields (temperature, weather description) are extracted from the JSON response
4. **Prompt Construction** — These values are embedded into a structured prompt instructing Gemini to act as a Weather Data Analyst
5. **Generate** — The prompt is sent to Gemini's API, which returns tailored suggestions
6. **Output** — The AI-generated recommendations are printed to the console

```
City Name → OpenWeatherMap API → Extracted Weather Data → Gemini Prompt → AI-Generated Suggestions
```

---

## 📦 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/ARCHIT2152/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment
```bash
python -m venv myenv
myenv\Scripts\activate      # Windows
source myenv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install requests google-genai python-dotenv
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```env
WEATHER_API_KEY=your_openweathermap_api_key
GEMINI_API_KEY=your_gemini_api_key
```
- Get a free OpenWeatherMap key: https://openweathermap.org/api
- Get a free Gemini API key: https://ai.google.dev/

### 5. Run the application
```bash
python index.py
```

---

## 💡 Example Usage

```
enter city: Delhi

As a Weather Data Analyst, here's what today's conditions mean for you:

At 34.6°C with overcast clouds, high humidity is the key factor —
expect it to feel warmer than the actual temperature suggests.

1. Outfit Suggestions: Opt for breathable cotton or linen, loose-fitting
   clothing, and avoid synthetic fabrics that trap moisture.
2. Hydration & Diet: Drink at least 3L of water; include electrolyte-rich
   options like coconut water or buttermilk.
3. Precautions: Apply SPF even under cloud cover, and carry a compact
   umbrella — overcast heat can trigger sudden showers.
```

---

## 🔒 Security

All credentials are loaded from a local `.env` file, which is explicitly excluded via `.gitignore`. No API keys are ever committed to version control or hardcoded in source files.

---

## 🚀 Future Improvements

- [ ] Add error handling for invalid city names or failed API requests
- [ ] Support concurrent lookups for multiple cities using `asyncio`
- [ ] Deploy as a simple web app or Telegram bot
- [ ] Cache recent responses to reduce redundant API calls

---

## 📄 License

This project is open-source and available for personal or educational use.
