# 🌍 Global Weather Assistant with Forecast & Voice

A Python desktop application that fetches and speaks out the current weather and weekly forecast for any global city, using a user-friendly **Tkinter GUI**.

---

## 📌 Project Purpose

> This project was built by **Adonis Jeswin** and **Krishal Haria** to showcase our solid understanding of **Python fundamentals** — including GUI, API integration, file handling, and voice interaction.

We also enhanced the GUI experience using ideas and guidance from AI (ChatGPT), to demonstrate how modern tools can support rapid development.

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

weather_assistant/
├── main.py # Main GUI + logic
├── config.py # API keys
├── location_data.json # Country → State → City mapping
└── README.md

---

## 🔧 Installation & Usage

1. **Install dependencies**:
```bash
pip install requests pyttsx3

