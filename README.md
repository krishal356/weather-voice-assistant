# 🌍 Global Weather Assistant with Forecast & Voice

A Python desktop application that fetches and speaks out the current weather and weekly forecast for any global city, using a user-friendly **Tkinter GUI**.

---

## 📌 Project Purpose

> This project was built by ***Adonis Jeswin*** and ***Krishal Haria*** to showcase our solid understanding of **Python fundamentals** — including GUI, API integration, file handling, and voice interaction.

We also enhanced the GUI experience using ideas and guidance from AI, to demonstrate how modern tools can support rapid development.

---

## 🎯 Features

- 🌎 Country → State → City dropdown selection (from `location_data.json`)
- 📡 Live current weather and 5-day forecast (via OpenWeatherMap API)
- 🎤 Voice assistant to read the weather aloud (using `pyttsx3`)
- 🌓 Dark Mode / Light Mode toggle
- 💻 Clean, responsive Tkinter GUI

---

## 🛠 Tech Stack

- Python 3
- Tkinter + ttk (GUI)
- OpenWeatherMap API
- `pyttsx3` (Text-to-Speech)
- JSON data handling

---

## 📂 File Structure

```bash
weather_assistant/
├── main.py # Main GUI + logic
├── config.py # API keys
├── location_data.json # Country → State → City mapping
└── README.md
```

---

## 🔧 Installation & Usage

1. **Install dependencies**:
```bash
pip install requests pyttsx3
```

2. **Get your OpenWeatherMap API key from**:
```bash
https://openweathermap.org/api
```

3. **Add your OpenWeatherMap API key to config.py**:
```bash
API_KEY = "your_openweathermap_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5"
```

4. **Run the app**:
```bash
python main.py
```

---

## 🧠 Developers
- ***Adonis Jeswin*** 
- ***Krishal Haria*** 

---

## 📝 License
- This project is licensed under the MIT License — feel free to use, modify, and share it.
- Just don’t forget to give us credit!

---

## ❤️ Built with AI Support
- This project was enhanced using AI-assisted development (ChatGPT) to help design the GUI and integrate modern usability features —proving that learning and building with AI is efficient and productive.

---
