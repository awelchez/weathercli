# WeatherCLI
The WeatherCLI is a Command Line Interface (CLI) application that allows you to retrieve current weather information based on a given zip code. It utilizes the WeatherAPI to fetch real-time weather data and displays it in an easy-to-read format.

# Installation
Clone the repository or download the source code.

Navigate to the project directory.

## Prerequisites
Python 3.6+

pystyle

httpx

To install the pystyle and httpx libraries, do `pip install -r requirements.txt` in the repository folder.
You may individually install each of these libraries by doing:
```
pip install pystyle
pip install httpx
```

# Usage
Open a terminal or command prompt.

Navigate to the directory containing the main.py file.

Run the following command to execute the WeatherCLI:

`python main.py`

The application will prompt you to input your WeatherAPI key. This key is required to access the weather data. If you don't have an API key, you can obtain one from WeatherAPI.

After providing the API key, you will be prompted to enter a zip code for the location you want to check the weather for.

# Features
Retrieve weather data for a specific location based on its zip code.

Display current weather conditions including:

City, region, and country

Local time

Wind speed (in MPH and KPH)

Humidity percentage

Temperature (in Celsius and Fahrenheit)

Cloud conditions

Last update time of the information

# Error Handling
The WeatherCLI handles errors related to API key validation and zip code validation.

If an invalid API key is provided, the application will display an error message and shut down.
If an invalid zip code is entered, the application will display an error message and shut down.
# Example
Here's an example of how the WeatherCLI works:

```
Please input your API Key for WeatherAPI.
> your_api_key_here
What is your zip code?
> 12345

City: Example City
Region: Example Region
Country: Example Country
Current Local Time: 2023-08-27 12:34
Wind in MPH: 5.6
Wind in KPH: 9.0
Humidity: 78%
Temperature in Celsius: 22.5
Temperature in Fahrenheit: 72.5
Clouds: Partly cloudy
This info was last updated at 2023-08-27 12:30:00
```
Note:

This CLI application was created for educational and personal purposes. It may not include all features of a fully-fledged weather application and is subject to limitations of the WeatherAPI service.

# License
This project is licensed under the MIT License.
