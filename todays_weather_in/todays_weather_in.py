#Import of librarys:
import pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.request
import requests
import re


def get_weather_data(url):
    r = requests.get(url)
    soup = bs(r.content,"html5lib") 
    
    #Get the weather information from this website

    #rain:
    rain_raw=soup.find_all("span", class_="precipitation__value")
    #First line is the title, this value we do not need
    rain_raw=rain_raw[1:]
    #Use a regex on the array and convert it into string while getting rid of everything except from the number:
    clean_rain=[re.sub('<.*?>','',str(i)) for i in rain_raw]

    #temperature (max and min):
    temp_raw_max=soup.find_all("span", {'class':['temperature min-max-temperature__max temperature--warm', 'temperature min-max-temperature__max temperature--cold']})
    temp_raw_min=soup.find_all("span", {'class':['temperature min-max-temperature__min temperature--cold', 'temperature min-max-temperature__min temperature--warm']})
    #Use a regex on the array and convert it into string while getting rid of everything except from the number:
    clean_temp_max=[re.sub('<.*?>','',str(i)) for i in temp_raw_max]
    clean_temp_min=[re.sub('<.*?>','',str(i)) for i in temp_raw_min]

    #dates:
    date_raw = soup.find_all('h3', {'class' : "daily-weather-list-item__date-heading"})
    #clean dates:
    dates_clean = []
    for i in range(0,len(date_raw)):
        i = str(date_raw[i]) #convert element to str
        i = i.split('"')[3]
        dates_clean.append(i)

    #create a dataframe from that:
    df = pd.DataFrame({"date":dates_clean,
                        "temperature_max":clean_temp_max,
                        "temperature_min":clean_temp_min,
                        "precipitation, mm":clean_rain})
    
    #Only get todays data (first entry)
    date = df.date[0]
    temp_max = df.temperature_max[0]
    temp_min = df.temperature_min[0]
    rain = df['precipitation, mm'][0]
    return print("Today (", date, ") the max temperature is:", temp_max, "and the min temperature is:", temp_min, ". The precipitation in mm is:", rain, ".")


#Function for getting todays data
def todays_weather(city, country='', state=''):
    """
    This function needs the city you want todays weather for as an argument in 'city'
    Optionally you can also give the country and/or the state.
    Arguments:
    - city
    - country (optional)
    - state (optional)
    This function will return todays weather of the requested place.
    """
    
    q_str = city+' '+country+' '+state
    q_str_list = q_str.split()
    count_input_words=len(q_str_list)
    
    q_url_plain='https://www.yr.no/en/search?q='
    q_url=q_url_plain
    
    i=0
    for q in q_str_list:
        if i==0:
            q_url=q_url+q
            i=i+1
        if i>0:
            q_url=q_url+"%20"+q
    
    #now the search url with the inputed arguments is generated and stored in q_url           
    #now we have the search site and want to access the actual weather page
    q_reg=requests.get(q_url)#request on the search site
    q_soup=bs(q_reg.content,"html5lib")
    
    try: 
        weather_url='https://www.yr.no'+str(q_soup.find_all("a", class_="search-results-list__item-anchor")[0]).split('"')[3] #url of the weather webpage

        place=str(q_soup.find_all("a", class_="search-results-list__item-anchor")[0]).split('>')[10].split(', <')[0] #location of requested forcast


        #Get the weather information from this website with the following function:
        print("Weather forecast for today in", city, "-", place, ":\n"), get_weather_data(weather_url)
    except:
        print("We couldn't find any locations matching your inserted arguments. Please check if everything is written correctly and try again.")