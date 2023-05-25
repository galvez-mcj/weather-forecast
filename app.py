import requests
import tkinter as tk
import tkinter.ttk as ttk
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
    -------------------------------------
    Totoong temperatura: {temperature}°C
    Pero it feels like: {feels_like}°C
    """
    weather_text.config(text=display_text)


root = tk.Tk()
root.iconbitmap('fire.ico')
root.title('Ang Ineeeeet!!!')
root.geometry('300x200')


input_label = tk.Label(root, text="\nTaga-saan ka?\n")
input_label.pack()

location_btn = tk.Button(root, text="Kunin ang lokasyon", command=get_location)
location_btn.pack()

# Result
weather_text = tk.Label(root, text="")
weather_text.pack()

root.mainloop()