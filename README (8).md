# 🌦️ AI Weather Assistant using Google Gemini Function Calling

An AI-powered weather assistant built with **Python**, **Google Gemini**, and the **OpenWeatherMap API** that demonstrates **Function Calling (Tool Calling)**.

Instead of directly asking an LLM to answer weather questions, the application provides Gemini with a custom tool (`get_weather`). Whenever the model determines that external weather information is required, it automatically invokes the tool, retrieves live weather data, and uses the returned information to generate a natural language response.

This project demonstrates how Large Language Models interact with external APIs through developer-defined functions.

---

# 🚀 Features

- 🌍 Live weather information for any city
- 🤖 Google Gemini Function Calling
- 🔧 Dynamic tool execution
- ☁️ OpenWeatherMap API integration
- 🔐 Secure API key management using `.env`
- 📦 Clean modular architecture
- 🔄 Multi-turn conversation support
- 📋 Structured JSON communication between Python and Gemini

---

# 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python 3 |
| AI Model | Google Gemini |
| Weather API | OpenWeatherMap |
| HTTP Requests | requests |
| Environment Variables | python-dotenv |
| Data Format | JSON |

---

# 📂 Project Structure

```
weather-api-project/
│
├── weather_tool.py        # Main application
├── .env                   # API Keys
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
        Python Application
                  │
                  ▼
           Google Gemini
                  │
      Decides Function Call
                  │
                  ▼
      available_functions
                  │
                  ▼
       get_weather(city)
                  │
                  ▼
      OpenWeatherMap API
                  │
          JSON Weather Data
                  │
                  ▼
        Function Result
                  │
                  ▼
           Google Gemini
                  │
                  ▼
      Natural Language Response
                  │
                  ▼
                 User
```

---

# ⚙️ Workflow

### Step 1

User asks a question.

```
What is the temperature in London?
```

↓

### Step 2

Python sends the following to Gemini:

- User Query
- Tool Definition (`get_weather`)
- Previous Conversation ID

↓

### Step 3

Gemini analyzes the request.

If weather information is required, it generates a **Function Call**.

```
get_weather(city="London")
```

↓

### Step 4

Python receives the function call.

↓

### Step 5

Python looks up the requested function inside

```
available_functions
```

↓

### Step 6

`get_weather()` executes.

It:

- Builds the OpenWeatherMap URL
- Sends an HTTP request
- Receives JSON
- Extracts temperature and weather description

↓

### Step 7

Python packages the result into a Function Result.

↓

### Step 8

Gemini receives the function output.

↓

### Step 9

Gemini generates a natural language answer.

↓

### Step 10

The answer is displayed to the user.

---

# 🔄 Sequence Flow

```
User
 │
 │ Ask Weather
 ▼
Python Application
 │
 │ Prompt + Tool Definition
 ▼
Gemini API
 │
 │ Function Call
 ▼
available_functions
 │
 │
 ▼
get_weather()
 │
 │ HTTP GET
 ▼
OpenWeatherMap API
 │
 │ JSON
 ▲
 │
get_weather()
 │
 │ Function Result
 ▼
Gemini API
 │
 │ Natural Language Response
 ▼
Python Application
 │
 ▼
User
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
WEATHER_API_KEY=your_openweathermap_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/ARCHIT2152/weather-api-project.git
```

Move into the project

```bash
cd weather-api-project
```

Create a virtual environment

```bash
python -m venv myenv
```

Activate it

Windows

```bash
myenv\Scripts\activate
```

Linux / macOS

```bash
source myenv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run

```bash
python weather_tool.py
```

Example

```
Ask me anything:
What is the weather in Mumbai?
```

Output

```
Called get_weather({'city': 'Mumbai'})
```

Gemini

```
The current temperature in Mumbai is 29°C with scattered clouds.
```

---

# 📖 Concepts Demonstrated

- Google Gemini Function Calling
- AI Tool Calling
- Function Registry Pattern
- Dynamic Function Dispatch
- REST API Integration
- HTTP Requests
- Environment Variables
- JSON Serialization
- Multi-turn AI Conversations

---

# 📚 APIs Used

## Google Gemini API

Responsible for:

- Understanding user queries
- Deciding when tools should be called
- Generating natural language responses

---

## OpenWeatherMap API

Provides:

- Current Temperature
- Weather Description
- City Information

---

# 🚀 Future Improvements

- [ ] 5-Day Weather Forecast
- [ ] Humidity & Wind Speed
- [ ] Air Quality Index
- [ ] Weather Alerts
- [ ] Multiple AI Tools (News, Time, Currency)
- [ ] Streamlit Dashboard
- [ ] Voice Assistant
- [ ] Location Detection
- [ ] Unit Conversion (°C ↔ °F)
- [ ] Error handling for invalid cities

---

# 👨‍💻 Author

**Archit Bankey**

B.Tech Computer Science Engineering

Interested in Artificial Intelligence, Machine Learning, LLMs, AI Agents, and Backend Development.

---

## ⭐ Star this repository if you found it useful!