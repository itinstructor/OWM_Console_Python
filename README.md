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
### Changes
- 08/01/2021: Initial commit

### License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Copyright (c) 2021 William A Loring
