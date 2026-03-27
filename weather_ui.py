from tkinter import *
import requests

# Function
def get_weather():
    city = city_entry.get()

    if city == "":
        result_label.config(text="⚠️ Enter a city name")
        return

    api_key = "76c0fa8b84e7305300e927fa88c91f71"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]

            result_label.config(
                text=f"📍 {city}\n🌡 {temp}°C\n☁️ {weather}"
            )
        else:
            result_label.config(text="❌ City not found!")

    except:
        result_label.config(text="⚠️ Error fetching data")

# Window
root = Tk()
root.title("Weather App")
root.geometry("350x300")
root.config(bg="#1e1e1e")
root.resizable(False, False)

# Title
Label(root, text="🌦 Weather App", bg="#1e1e1e", fg="white",
      font=("Arial", 18, "bold")).pack(pady=10)

# Entry
city_entry = Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Colombo")

# Button
Button(root, text="Get Weather", command=get_weather,
       bg="orange", fg="white", font=("Arial", 12)).pack(pady=10)

# Result
result_label = Label(root, text="", bg="#1e1e1e", fg="white",
                     font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()