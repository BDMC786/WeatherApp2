def fixnyc(city):
    nycAlts = ["new york" , "new york, ny" , "new york city" "new york, new york" , "new york ny" , "new york new york"]
    if city.lower() in nycAlts:
        city = "manhattan"
    if city.lower() == "bayonne":
        city = "Bayonne, NJ"
    
    return city

def getlocation(city):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(timeout=300, user_agent="WeatherApp")
    location = geolocator.geocode(city)
    latitude = location.latitude
    longitude = location.longitude
    print(location)
    
    #Get location name from geopy
    city_mod = f"{location}".split(", ") 
    place = f'{city_mod[0]}, {city_mod[2]}'

    return(place, latitude, longitude)

def get_url(latitude, longitude):

    key = "5fc1f583fa2e15d8a27208e502ba5fb0"
    #Get URL for API call to DarkSky
    url = f'https://api.darksky.net/forecast/{key}/{latitude},{longitude}'
    print(url)

    return url



def getdata(url):
    import requests
    #Make API Call
    response = requests.get(url)
    response_json = response.json()

    #Get timezone offset
    x = response_json["offset"]
    time_adjust = (int(x)) * 3600

    return (response_json, time_adjust)

def getcurrent(current_weather, time_adjust):
    from datetime import datetime as dt
    #Pull data from current conditions
    current_dict = {}
    current_list_try = ["apparentTemperature",  "cloudCover", "humidity", "precipIntensity", "precipAccumulation", "precipProbability", "summary", "temperature", "time", "uvIndex", "windSpeed" , "windGust"]
    
    for elements in current_list_try:
        if elements in current_weather:
            current_dict[elements] = current_weather[elements]

    #Adjusts Time to local time
    current_dict["time"] = current_dict["time"] + time_adjust

    #Gets the Day of the week and the time in AM PM format
    current_dict["time"] = f"{dt.utcfromtimestamp(current_dict['time']).strftime('%A')} {dt.utcfromtimestamp(current_dict['time']).strftime('%r')}".lstrip("0").replace(" 0", " ")
    
    #Correct Formats Current
    current_dict["apparentTemperature"] = f'{round(current_dict["apparentTemperature"])} °F' #Round 
    current_dict["cloudCover"] = f'{round(current_dict["cloudCover"] * 100)}%' #Percentage
    current_dict["humidity"] = f'{round(current_dict["humidity"] * 100)}%'
    current_dict["precipProbability"] = f'{round(current_dict["precipProbability"] * 100)}%'
    current_dict["temperature"] = f'{round(current_dict["temperature"])} °F'
    if "precipAccumulation" in current_dict:
        current_dict["precipAccumulation"] = f'Snowfall Accumulation: {current_dict["precipAccumulation"]} Inches'
    current_dict["windSpeed"] = f'{round(current_dict["windSpeed"])} MPH'
    current_dict["windGust"] = f'{round(current_dict["windGust"])} MPH'

    return current_dict

def gethourly(hourly_weather, time_adjust):
    from datetime import datetime as dt
    #Pull data from Hourly Conditions
    hourly_list = []
    hourly_elements_try = ["apparentTemperature", "cloudCover", "humidity", "precipIntensity", "precipAccumulation", "precipProbability", 
                    "summary", "temperature", "time", "uvIndex", "windSpeed" , "windGust"]
    for hours in hourly_weather:
        hour_dict = {}
        for element in hourly_elements_try:
            if element in hours:
                hour_dict[element] = hours[element]

        try:
            hour_dict["time"] = dt.utcfromtimestamp(int(hours["time"]) + int(time_adjust)).strftime('%A %I:%M %p')
            hour_dict["time"] = hour_dict["time"].lstrip("0").replace(" 0", " ")
        except:
            print('hour_dict["time"] failed')
        try:
            hour_dict["apparentTemperature"] = f'{round(hour_dict["apparentTemperature"])} °F' #Round 
        except:
            print('hour_dict["apparentTemperature"] failed')
        try:
            hour_dict["cloudCover"] = f'{round(hour_dict["cloudCover"] * 100)}%' #Percentage
        except:
            print('hour_dict["cloudCover"] failed')
        try:
            hour_dict["humidity"] = f'{round(hour_dict["humidity"] * 100)}%'
        except:
            print('hour_dict["humidity"] failed')
        try:
            hour_dict["precipProbability"] = f'{round(hour_dict["precipProbability"] * 100)}%'
        except:
            print('hour_dict["precipProbability"] failed')
        try:
            hour_dict["temperature"] = f'{round(hour_dict["temperature"])} °F'
        except:
            print('hour_dict["temperature"] failed')
        try:
            hour_dict["windSpeed"] = f'{round(hour_dict["windSpeed"])} MPH'
        except:
            print('hour_dict["windSpeed"]')
        try:
            hour_dict["windGust"] = f'{round(hour_dict["windGust"])} MPH'
        except:
            print('hour_dict["windGust"]')
        
        hourly_list.append(hour_dict)

    return hourly_list

def getdaily(daily_weather, time_adjust):
    from datetime import datetime as dt
    #Pull data from Daily Conditions
    daily_elements_try = ["cloudCover", "humidity", "precipIntensity", "precipIntensityMax", 
    "precipIntensityMaxTime", "precipProbability", "precipType", "precipAccumulation", "summary", "sunriseTime", "sunsetTime", "temperatureHigh", 
    "temperatureHighTime", "temperatureLow", "temperatureLowTime", "time", "uvIndex", "uvIndexTime", "windSpeed" , "windGust"] 
    daily_list = []

    # print("enter daily loop")

    for days in daily_weather:
        daily_dict = {}
        for elements in daily_elements_try:
            # print("elements")
            if elements in days:
                # print(elements)
                daily_dict[elements] = days[elements]
                # print(daily_dict[elements])
        #Format Fixing
        try:
            daily_dict["cloudCover"] = f'{round(daily_dict["cloudCover"] * 100)}%'
        except:
            print('daily_dict["cloudCover"] failed')
        try:
            daily_dict["humidity"] = f'{round(daily_dict["humidity"] * 100)}%'
        except:
            print('daily_dict["humidity"] failed')
        try:
            daily_dict["precipProbability"] = f'{round(daily_dict["precipProbability"] * 100)}%'
        except:
            print('daily_dict["precipProbability"] failed')
        try:
            daily_dict["temperatureHigh"] = f'{round(daily_dict["temperatureHigh"])} °F'
        except:
            print('daily_dict["temperatureHigh"] failed')
        try:
            daily_dict["temperatureLow"] = f'{round(daily_dict["temperatureLow"])} °F'
        except:
            print('daily_dict["temperatureLow"] failed')
        try:
            daily_dict["windSpeed"] = f'{round(daily_dict["windSpeed"])} MPH'
        except:
            print('daily_dict["windSpeed"] failed')
        try:
            daily_dict["windGust"] = f'{round(daily_dict["windGust"])} MPH'
        except:
            print('daily_dict["windGust"] failed')

        #TIMES
        try:
            daily_dict["precipIntensityMaxTime"] = f"{dt.utcfromtimestamp(daily_dict['precipIntensityMaxTime'] + time_adjust).strftime('%I:%M %p')}".lstrip("0").replace(" 0", " ")
        except:
            print('daily_dict["precipIntensityMaxTime"] failed')
        try:
            daily_dict["sunriseTime"] = f"{dt.utcfromtimestamp(daily_dict['sunriseTime'] + time_adjust).strftime('%I:%M %p')}".lstrip("0").replace(" 0", " ")
        except:
            print('daily_dict["sunriseTime"] failed')
        try:
            daily_dict["sunsetTime"] = f"{dt.utcfromtimestamp(daily_dict['sunsetTime'] + time_adjust).strftime('%I:%M %p')}".lstrip("0").replace(" 0", " ")
        except:
            print('daily_dict["sunsetTime"] failed')
        try:
            daily_dict["temperatureHighTime"] = f"{dt.utcfromtimestamp(daily_dict['temperatureHighTime'] + time_adjust).strftime('%I:%M %p')}".lstrip("0").replace(" 0", " ")
        except:
            print('daily_dict["temperatureHighTime"] failed')
        try:
            daily_dict["temperatureLowTime"] = f"{dt.utcfromtimestamp(daily_dict['temperatureLowTime'] + time_adjust).strftime('%I:%M %p')}".lstrip("0").replace(" 0", " ")
        except:
            print('daily_dict["temperatureLowTime"] failed')
        try:
            daily_dict["time"] = f"{dt.utcfromtimestamp(daily_dict['time'] + time_adjust).strftime('%A %B %d')}".lstrip("0").replace(" 0", " ")
        except:
            print('daily_dict["time"] failed')
        try:
            daily_dict["uvIndexTime"] = f"{dt.utcfromtimestamp(daily_dict['uvIndexTime'] + time_adjust).strftime('%I:%M %p')}".lstrip("0").replace(" 0", " ")
        except:
            print('daily_dict["uvIndexTime"] failed')
        
        
        daily_list.append(daily_dict)

    return daily_list


def getweather_input(city):
    city = fixnyc(city)

    location_response = getlocation(city)
    place = location_response[0]
    print(place)

    url = get_url(location_response[1], location_response[2])

    data_response = getdata(url)
    response_json = data_response[0]
    time_adjust = data_response[1]

    current_dict = getcurrent(response_json["currently"], time_adjust)

    hourly_list = gethourly(response_json["hourly"]["data"], time_adjust)

    daily_list = getdaily(response_json["daily"]["data"], time_adjust)


    #Get Next Hour Summary
    try:
        next_hour = response_json["minutely"]["summary"]
    except:
        print("next hour failed")
        next_hour = "Unavailable"

    #Get Alerts
    if "alerts" in response_json:
        all_alerts = response_json["alerts"]
        alerts = []
        for messages in all_alerts:
            alerts.append(messages["description"])
    else:
        alerts = []
        alerts.append("CLEAR")

    data = [place, current_dict, hourly_list, daily_list, next_hour, alerts]

    return data


def getweather_link(city):
    city_urls = {"Bayonne, NJ" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.6687141,-74.1143091" ,
    "Atlanta, GA" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/33.7490987,-84.3901849",
    "Cranston, RI" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/41.7809588,-71.4371257", 
    "Culver, IN" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/41.2189311,-86.4230626" ,
    "Magic Kingdom, Disney World, Florida" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/28.4190753,-81.58171584246976" ,
    "Easton, PA" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.6916081,-75.2099866" , 
    "Hightstown, NJ" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.2695538,-74.5232089" , 
    "Montclair, NJ" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.8164458,-74.2210643" , 
    "New York, NY" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.7896239,-73.9598939" ,
    "Warren Township, NJ" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.63065715,-74.52266308479568" , 
    "West New York, NJ" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.7856117,-74.0093129",
    "Lincoln Park, NJ" : "https://api.darksky.net/forecast/5fc1f583fa2e15d8a27208e502ba5fb0/40.9242652,-74.3020933"

    }

    url = city_urls[city]

    place = city

    data_response = getdata(url)
    response_json = data_response[0]
    time_adjust = data_response[1]

    current_dict = getcurrent(response_json["currently"], time_adjust)

    hourly_list = gethourly(response_json["hourly"]["data"], time_adjust)

    daily_list = getdaily(response_json["daily"]["data"], time_adjust)


    #Get Next Hour Summary
    try:
        next_hour = response_json["minutely"]["summary"]
    except:
        print("next hour failed")
        next_hour = "Unavailable"

    #Get Alerts
    if "alerts" in response_json:
        all_alerts = response_json["alerts"]
        alerts = []
        for messages in all_alerts:
            alerts.append(messages["description"])
    else:
        alerts = []
        alerts.append("CLEAR")

    data = [place, current_dict, hourly_list, daily_list, next_hour, alerts]

    return data



# 100, 60th Street, West New York, Hudson County, New Jersey, 07093, United States
# Bayonne, Hudson County, New Jersey, 07002, United States
# Manhattan, New York County, New York, United States
# Empire State Building, 350, 5th Avenue, Koreatown, Midtown South, Manhattan, New York County, New York, 10018, United States
# Brooklyn, Kings County, New York, United States
# state names don't work, index issue 
# Walt Disney World Resort, Bay Lake, Reedy Creek Improvement District, Orange County, Florida, 32830, United States
# Splash Mountain, Frontierland North, Bay Lake, Reedy Creek Improvement District, Orange County, Florida, United States
# 29, Avenue B, Bayonne, Hudson County, New Jersey, 07002, United States
# Bayonne High School, West 30th Street, Bayonne, Hudson County, New Jersey, 07002, United States
# JFK + 58th Street, John F. Kennedy Boulevard, Bayonne, Hudson County, New Jersey, 07305, United States
# Albany, Albany County, New York, 12207, United States
# Yankee Stadium, 1, East 161st Street, The Bronx, Bronx County, New York, 10451, United States
# Los Angeles, California, United States
# Paris, Île-de-France, France métropolitaine, France
# Washington, District of Columbia, United States
# 
# 
# 