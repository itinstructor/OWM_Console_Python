"""
    Name: one_call_console.py
    Author:
    Created:
    Purpose: Main program
    Get one call weather data from OpenWeatherMap.org API with requests and json
    Get lat and lon from geocode
"""

import weather_utils
import one_call_class


def menu():
    print("-"*70)
    print(f"[1] Get current weather")
    print(f"[2] Get 12 hour forecast")
    print(f"[3] Get 48 hour forecast")
    print(f"[4] Get 7 day forecast")
    print(f"[5] Get new location")
    menu_choice = input(f"[Enter] to quit. Enter your choice: ")
    return menu_choice


#------------------------ MAIN PROGRAM -------------------------------------#
def main():
    # Create program object
    one_call = one_call_class.OneCall()

    # Get initial location
    one_call.get_location()

    # Menu loop
    while True:
        menu_choice = menu()
        if menu_choice == "":
            # Exit loop
            break
        elif menu_choice == "1":
            one_call.get_current_weather()
        elif menu_choice == "2":
            one_call.get_twelve_hour()
        elif menu_choice == "3":
            one_call.get_forty_eight_hour()
        elif menu_choice == "4":
            one_call.get_seven_day()
        elif menu_choice == "5":
            one_call.get_location()

    weather_utils.goodbye()


main()
