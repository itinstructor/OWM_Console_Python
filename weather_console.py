"""
    Name: weather_console.py
    Author:
    Created:
    Purpose: OOP console app
    Get current weather data from OpenWeatherMap.org API with requests and json
"""

# Openweather map url, api key, and other weather utilities
import weather_utils
import weather_console_class


#-------------------------- MAIN PROGRAM ----------------------------#
# Create program object
def main():
    weather = weather_console_class.WeatherClass()
    weather.get_location()
    while True:
        # Call weather methods
        weather.get_dictionaries()
        weather.get_weather()
        weather.display_weather()
        # Ask user to continue or end program
        answer = input(
            "Get weather from another location? (y), (Enter) to quit: ")
        if answer == "":
            break
        weather.get_location()

    weather_utils.goodbye()


# Call the main method
main()
