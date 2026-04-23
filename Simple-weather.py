import urllib.request
import json

api_key = "6cbe181d1f693c0c763b7c5d8272d7fc"

print("Simple-Weather")

while True:
    city = input("\nEnter city name (or 'exit'): ")

    if city.lower() == "exit":
        print("Goodbye!")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\n--- Weather Report ---")
        print("City:", city.title())
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather)

    except:
        print("Error: Invalid city or network issue")