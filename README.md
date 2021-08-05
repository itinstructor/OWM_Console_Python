# OpenWeatherMap Class Project
OpenWeatherMap Python Console Program Final Class Project
### Overview
- Python console program using requests, OpenWeatherMap One Call API, OpenWeatherMap Air Pollution API, and Nominatim from geopy
- Includes current and forecast weather, UV index, and Air Quality Index
- Air Quality Index is a separate API call from OpenWeatherMap Air Pollution API
- The lat and long retrieved from OpenWeatherMap is reverse geocoded into the name of the location using Nominatim from geopy
    * The reverse geocoding from geopy confirms that we have the weather for the right city.
### API Key
- To run the program, go to weather_utils.py. Put in your OpenWeatherMap API key.
