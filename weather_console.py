"""
    Name: weather_console.py
    Author:
    Created:
    Purpose: OOP console app
    Get current weather data from OpenWeatherMap.org API with requests and json
"""

# Openweather map url, api key, and other weather utilities
import weather_utils
# Make api request
import requests
# To convert GMT Unix time to local Python datetime object
import datetime
# For reverse geocode name of location from lat/lon
import geocode_geopy


class Weather:
    def __init__(self):
        """ Initialize program object """
        print(weather_utils.WEATHER_BANNER)
        print(weather_utils.title("Welcome to Bill's Weather App!"))

#-------------------------- GET LOCATION ----------------------------#
    def get_location(self):
        """
            Get weather location and weather information
        """
        try:
            # Get location input from user
            city = input("Enter city: ")
            state = input("Enter state: ")
            country = input("Enter country: ")

            # Build the weather query
            self.__location = f"{city},{state},{country}"

            # Build the openweathermap api url
            url = weather_utils.URL + self.__location

            # Get the weather information out as a weather object
            response = requests.get(url)
            # print(response.text)

            # If the status_code is 200, successful connection and data
            if(response.status_code == 200):
                # Load json response into __weather dictionary
                self.__weather_data = response.json()
                # For testing
                # print(self.__weather)
                # Let user know the connection was successful
                print("\n[+] The connection to OpenWeatherMap was successful.")
            else:
                print(f"The response status code was: {response.status_code}")
                print("You may have typed an invalid location.")
                print("Please try again.")
                self.get_location()
        except:
            print("[-] Sorry, there was a problem connecting.")

#-------------------------- GET DICTIONARIES ----------------------------#
    def get_dictionaries(self):
        """
            get individual weather information dictionaries
            from main self.__weather dictionary
        """
        # temp, feels_like, temp_min, temp_max, pressure, humidity
        self.__main_dict = self.__weather_data.get("main")
        # id, main, description, icon
        self.__weather_dict = self.__weather_data.get("weather")[0]
        # Wind speed and direction
        self.__wind_dict = self.__weather_data.get("wind")
        # Cloud information
        self.__clouds_dict = self.__weather_data.get("clouds")
        # Sunrise and Sunset time
        self.__sys_dict = self.__weather_data.get("sys")
        # Latitude and Longitude
        self.__coord_dict = self.__weather_data.get("coord")

#-------------------------- GET WEATHER ----------------------------#
    def get_weather(self):
        """
            Get individual weather items from dictionaries
        """
        # Get City name and time of data calculation
        self.__name = self.__weather_data.get("name")
        self.__time = self.convert_time(self.__weather_data.get("dt"))

        # Get description of current weather. Ex: Clear Skies
        self.__description = self.__weather_dict.get("description").title()
        # Get fahrenheit temperature
        self.__temperature = self.__main_dict.get("temp")
        # Get feels like temperature
        self.__feels_like = self.__main_dict.get("feels_like")
        # Get humidity
        self.__humidity = self.__main_dict.get("humidity")
        # Get pascals and convert to inches of mercury
        self.__pressure = round(self.__main_dict.get('pressure') / 33.86, 2)

        # Get wind speed and direction
        self.__wind_speed = self.__wind_dict.get("speed")
        self.__wind_direction = self.__wind_dict.get("deg")
        self.__cardinal_direction = weather_utils.degrees_to_cardinal(self.__wind_dict.get("deg"))

        # Get cloud cover percentage
        self.__clouds = self.__clouds_dict.get("all")

        # Get sunrise and sunset time
        self.__sunrise_time = self.convert_time(self.__sys_dict.get("sunrise"))
        self.__sunset_time = self.convert_time(self.__sys_dict.get("sunset"))

        # Get latitude and longitude
        self.__latitude = self.__coord_dict.get("lat")
        self.__longitude = self.__coord_dict.get("lon")

        # Reverse gecode the address
        self.__address = geocode_geopy.reverse_geocode(
            self.__latitude, self.__longitude)

#-------------------------- DISPLAY WEATHER ----------------------------#
    def display_weather(self):
        """
            Display weather information
        """
        # Field width constant for printing in columns
        WIDTH = 15
        # Print weather information
        print(f'\nCurrent weather at {self.__time} ☀')
        print(f"{self.__address}")
        print(self.__description)
        print(f'{"Temperature:":{WIDTH}} {self.__temperature}°F 🌡')
        print(f'{"Feels Like:":{WIDTH}} {self.__feels_like}°F')
        print(f'{"Humidity:":{WIDTH}} {self.__humidity}%')
        print(f'{"Wind Speed:":{WIDTH}} {self.__wind_speed} mph 💨')
        print(f'{"Wind Direction:":{WIDTH}} {self.__wind_direction}° {self.__cardinal_direction}')
        print(f'{"Pressure:":{WIDTH}} {self.__pressure} in')
        print(f'{"Cloud Coverage:":{WIDTH}} {self.__clouds}% ☁️')
        print(f'{"Sunrise:":{WIDTH}} {self.__sunrise_time}')
        print(f'{"Sunset:":{WIDTH}} {self.__sunset_time}')
        print(f'{"Longitude:":{WIDTH}} {self.__longitude}')
        print(f'{"Latitude:":{WIDTH}} {self.__latitude}\n')

#-------------------------- GET TIME ----------------------------#
    def convert_time(self, time):
        """
            Convert GMT Unix time to local time
        """
        # Convert Unix timestamp to local Python datetime
        time = datetime.datetime.fromtimestamp(time)
        # Format the date to hours, minutes, seconds, AM PM
        time = f"{time:%I:%M:%S %p}"
        # Strip out the leading 0's: 01 becomes 1
        time = time.lstrip("0")
        # Return GMT Unix as local Python time object
        return time

#-------------------------- GOODBYE ----------------------------#
    def goodbye(self):
        """
            Print goodbye to user
        """
        print(weather_utils.title("Good bye from Bill's Weather App!"))


#-------------------------- MAIN PROGRAM ----------------------------#
"""
    Create weather object, get weather
    while loop allows more than one location
"""

# Create weather object
weather = Weather()

while True:
    # Call weather methods
    weather.get_location()
    weather.get_dictionaries()
    weather.get_weather()
    weather.display_weather()
    # Ask user to continue or end program
    answer = input(
        "Get weather from another location? (y for yes, Enter to quit)? ")
    if answer == "":
        break

weather.goodbye()
