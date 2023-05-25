import requests
import tkinter as tk
from decouple import config

IPBASE_KEY = config('IPBASE_KEY')
OPENWEATHER_KEY = config('OPENWEATHER_KEY')

IPBASE_ENDPOINT = 'https://api.ipbase.com/v2/info'
OPENWEATHER_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'

def get_location():
    query_params = {
        'apiKey': IPBASE_KEY
    }

    response = requests.get(IPBASE_ENDPOINT, params=query_params)
    if response.status_code == 200:
        data = response.json()
        try:
            location_data = data['data']['location']
            city_name = location_data['city']['name']            
        except KeyError as e:
            print(f'Error: {e}')
    else:
        print(f'Error: {response.status_code} - {response.text}')

    weather_params = {
        'q': city_name,
        'appid': OPENWEATHER_KEY,
        'units': 'metric'
    }

    response = requests.get(OPENWEATHER_ENDPOINT, params=weather_params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
    else:
        print(f'Error: {response.status_code} - {response.text}')
    
    """
    Display the weather data to tkinter
    """
    display_text = f"""
    Grabe na talaga sa {city_name}!
    --------------------------------------------
    Totoong temperatura: {temperature}°C
    Pero it feels like: {feels_like}°C
    """
    weather_text.config(text=display_text)

root = tk.Tk()
root.title('Ang Ineeeeet!!!')
canvas1 = tk.Canvas(root, width = 300, height = 200)
canvas1.pack()

input_label = tk.Label(root, text="Taga-saan ka?", fg='brown', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 30, window=input_label)

location_btn = tk.Button(root, text="Kunin ang lokasyon", command=get_location, bg='brown', fg='white')
canvas1.create_window(150, 60, window=location_btn)

# Result
weather_text = tk.Label(root, text="", font=('helvetica', 12))
canvas1.create_window(150, 130, window=weather_text)

root.mainloop()
