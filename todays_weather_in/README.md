# todays_weather_in - PyPI package
With this package one can get the weather forcast of today on a certain location

With this package you will be able to get the weather forecast of today for an inserted location.
This is a private project and was developed (among other things) as an application of web scraping with beautiful soap.

### Installation with pip:
!pip install todays-weather-in

### How to use:
To use it, import the function in the following way:
from todays_weather_in import todays_weather

You can get the forecast by simply using the function 'todays_weather' and putting the location you wish the forecast for as arguments.

  In Details:
  todays_weather(city, country, state) - whereas country and state are optional arguments. 
  But be aware that if you only input the mandatory city name, the search might give you a city with the same name but in another country/state.


### How to make a PyPI package:
You can find the detailed article on how to make a PyPI package here: https://medium.com/@franziska.braunschneider/dear-pypi-whats-todays-weather-in-rome-c7722d0037e9 

For uploading to Test-PyPI (test.pypy.org) and normal PyPI (pypi.org ):

cd PACKAGE_PATH 
python setup.py sdist
pip install twine

#### TestPyPI:
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

#### Normal PyPI:
twine upload dist/*