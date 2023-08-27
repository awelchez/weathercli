import httpx
import time
from pystyle import Add, Colorate, Colors, Box, Write

Write.Print("Please input your API Key for WeatherAPI.\n", Colors.blue_to_cyan, interval=0.05)
key = Write.Input("> ", Colors.blue)
Write.Print("What is your zip code?\n", Colors.blue_to_cyan, interval=0.05)
zipcode = Write.Input("> ", Colors.blue)

def apikeyerror():
    Write.Print("Enter a valid API Key.\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("The program will now shutdown. If you would like to try again, do 'python main.py'", Colors.blue_to_cyan, interval=0.05)
    quit()

def zipcodeerror():
    Write.Print("Enter a valid zip code.\n", Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    Write.Print("The program will now shutdown. If you would like to try again, do 'python main.py'", Colors.blue_to_cyan, interval=0.05)
    quit()

if len(zipcode) == 5:
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={zipcode}&aqi=no"
    response = httpx.get(url)
    if response.status_code == 200:
      data = response.json()
    
      if data.get('error', {}).get('code') == 1006:
            Write.Print("Please enter a valid zip code.")
      else:
            Write.Print(f"City: {data['location']['name']}\n"
            f"Region: {data['location']['region']}\n"
            f"Country: {data['location']['country']}\n"
            f"Current Local Time: {data['location']['localtime']}\n"
            f"Wind in MPH: {data['current']['wind_mph']}\n"
            f"Wind in KPH: {data['current']['wind_kph']}\n"
            f"Humidity: {data['current']['humidity']}%\n"
            f"Temperature in Celsius: {data['current']['temp_c']}\n"
            f"Temperature in Fahrenheit: {data['current']['temp_f']}\n"
            f"Clouds: {data['current']['condition']['text']}\n"
            f"This info was last updated at {data['current']['last_updated']}",
            Colors.purple_to_blue,
            interval=0.03)
    if response.status_code == 400:
      zipcodeerror()
    if response.status_code == 403:
      apikeyerror()
else:
      zipcodeerror()
