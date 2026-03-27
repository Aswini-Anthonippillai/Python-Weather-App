import requests

api_key = "76c0fa8b84e7305300e927fa88c91f71"

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != "404":
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print(f"\n📍 City: {city}")
    print(f"🌡 Temperature: {temp}°C")
    print(f"☁️ Condition: {weather}")
else:
    print("❌ City not found!")