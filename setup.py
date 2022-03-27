#This packages will give you the weather forecast of today for a certain location.

#To use it use this command:
#pip install -i https://test.pypi.org/simple/ get-todays-weather
#and import the todays_weather function:
#from todays_weather_in import todays_weather

from setuptools import setup

setup(name='todays_weather_in',
      version='1.3',
      license='MIT',
      description='Showing todays weatherforecast for a locations chosen in the function',
      packages=['todays_weather_in'],
      zip_safe=False,
      author = 'Franziska Braun',
      author_email = 'franziska.braunschneider@googlemail.com',
      url = 'https://github.com/FiDataS/todays_weather_in.git',
      download_url = 'https://github.com/FiDataS/todays_weather_in/archive/refs/tags/v1.3.tar.gz',
      keywords = ['weather', 'weatherforecast']
      )

#making the package:

#cd package_directory (navigate to folder with setup.py)
#python setup.py sdist
#pip install twine

# commands to upload to the pypi test repository
#twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# command to upload to the pypi repository
#twine upload dist/*