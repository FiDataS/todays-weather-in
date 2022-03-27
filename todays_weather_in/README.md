# Show_Todays_Weather_Pypi_Package
With this package one can get the weather forcast of today on a certain location

With this package you will be able to get the weather forecast of today for an inserted location.
This is a private project and was developed (among other things) as an application of web scraping with beautiful soap.

Installation with pip:
pip install -i https://test.pypi.org/simple/ show-todays-weather

To use it, import the function in the following way:
from todays_weather_in import todays_weather

How to use:
You can get the forecast by simply using the function 'todays_weather' and putting the location you wish the forecast for as arguments.

  In Details:
  todays_weather(city, country, state) - whereas country and state are optional arguments. 
  But be aware that if you only input the mandatory city name, the search might give you a city with the same name but in another country/state.