import tkinter as tk
from tkinter import ttk, messagebox
import requests
import pyttsx3
import json
from config import API_KEY, BASE_URL

# Load location data
with open("location_data.json", "r", encoding="utf-8") as f:
    location_data = json.load(f)

engine = pyttsx3.init()

# Theme Colors
LIGHT_BG, DARK_BG = "#f2f2f2", "#2b2b2b"
LIGHT_FG, DARK_FG = "#000000", "#ffffff"
current_theme = "dark"

# App Window
root = tk.Tk()
root.title("🌍 Global Weather Assistant")
root.geometry("600x600")
root.configure(bg=DARK_BG)

# Theme Toggle
def toggle_theme():
    global current_theme
    if current_theme == "dark":
        root.configure(bg=LIGHT_BG)
        for widget in root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.configure(bg=LIGHT_BG, fg=LIGHT_FG)
        current_theme = "light"
    else:
        root.configure(bg=DARK_BG)
        for widget in root.winfo_children():
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.configure(bg=DARK_BG, fg=DARK_FG)
        current_theme = "dark"

# Dropdown Update
def update_states(*_):
    states = list(location_data.get(country_var.get(), {}).keys())
    state_menu['values'] = states
    state_var.set(''); city_var.set(''); city_menu['values'] = []

def update_cities(*_):
    cities = location_data.get(country_var.get(), {}).get(state_var.get(), [])
    city_menu['values'] = cities
    city_var.set('')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def fetch_weather(city):
    return requests.get(f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric").json()

def fetch_forecast(city):
    return requests.get(f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric").json()

def display_weather(data, forecast):
    try:
        city = data["name"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        result = f"📍 {city}\n🌡 {temp}°C\n💧 Humidity: {humidity}%\n☁ {desc.capitalize()}\n\n📅 Forecast:\n"
        for i in range(0, len(forecast["list"]), 8):
            entry = forecast["list"][i]
            dt_txt = entry["dt_txt"].split()[0]
            temp_day = entry["main"]["temp"]
            desc_day = entry["weather"][0]["description"].capitalize()
            result += f"{dt_txt}: {temp_day}°C, {desc_day}\n"

        output_label.config(text=result)
        speak(f"The weather in {city} is {desc} with {temp} degrees Celsius.")
    except Exception as e:
        print("[ERROR] Display:", str(e))
        messagebox.showerror("Error", "Failed to display weather.")

def get_selected_weather():
    city = city_var.get()
    if not city:
        messagebox.showerror("Missing", "Please select a valid city.")
        return
    data = fetch_weather(city)
    if data.get("cod") != 200:
        messagebox.showerror("Error", "City not found or weather data unavailable.")
        return
    forecast = fetch_forecast(city)
    display_weather(data, forecast)

# Variables
country_var, state_var, city_var = tk.StringVar(), tk.StringVar(), tk.StringVar()

# Dropdowns
tk.Label(root, text="Country:", bg=DARK_BG, fg=DARK_FG).pack()
country_menu = ttk.Combobox(root, textvariable=country_var, values=list(location_data.keys()), state="readonly")
country_menu.pack()

tk.Label(root, text="State:", bg=DARK_BG, fg=DARK_FG).pack()
state_menu = ttk.Combobox(root, textvariable=state_var, state="readonly")
state_menu.pack()

tk.Label(root, text="City:", bg=DARK_BG, fg=DARK_FG).pack()
city_menu = ttk.Combobox(root, textvariable=city_var, state="readonly")
city_menu.pack()

# Events
country_var.trace("w", update_states)
state_var.trace("w", update_cities)

# Buttons
tk.Button(root, text="Get Weather 🌦", command=get_selected_weather).pack(pady=10)
tk.Button(root, text="Toggle Theme 🌓", command=toggle_theme).pack(pady=(10, 0))

# Output
output_label = tk.Label(root, text="", wraplength=500, justify="left", bg=DARK_BG, fg=DARK_FG)
output_label.pack(pady=20)

root.mainloop()
