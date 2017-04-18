from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""Timezones functions"""

import arrow
from tzwhere import tzwhere
from datetime import datetime

def parse_string(input_str):
    input_list = input_str.split(',')
    return input_list

def get_time(_):
    """Returns the current time in the server' timezone
    
    :return: 
    """
    return HttpResponse(arrow.now())


def get_timezone_fromLatLong(_, latitudelongitude):
    """  returns the timezone at a given latitude and longitude as a short description string (e.g. America/Los_Angeles)
    . If there is no timezone at that location, return a 404. 
    
    :param latitude: 
    :param longitude: 
    :return: 
    """
    latlong_str = parse_string(latitudelongitude)
    latitude = float(latlong_str[0])
    longitude = float(latlong_str[1])
    tz =tzwhere.tzwhere()
    error_msg = 'Error 404'
    location = tz.tzNameAt(latitude, longitude)
    if tz.tzNameAt(latitude, longitude) is None:
        return HttpResponse(error_msg)
    else: return HttpResponse(tz.tzNameAt(latitude,longitude))


def get_time_in_timezone(_, latitudelongitude):
    """returns the current time in the timezone at a given latitude and longitude.
     If there is no timezone at that location, return a 400.
    
    :param latitude: 
    :param longitude: 
    :return: 
    """
    latlong_str = parse_string(latitudelongitude)
    latitude = float(latlong_str[0])
    longitude = float(latlong_str[1])
    tz = tzwhere.tzwhere()
    tz_name = tz.tzNameAt(latitude,longitude)
    local_time = arrow.now(tz_name)
    error_msg = 'Error 400'
    if local_time is None:
        return HttpResponse(error_msg)
    else: return HttpResponse(local_time)


def get_time_based_on_other_timezone(_,time, latitudelongitude):
    """
    
    :param latitudelongitude: 
    :param time: 
    :return: 
    """
    error_msg = 'Error 400'
    latlong_str = parse_string(latitudelongitude)
    latitude = float(latlong_str[0])
    longitude = float(latlong_str[1])
    tz = tzwhere.tzwhere()
    tz_name = tz.tzNameAt(latitude, longitude)
    clean_time = arrow.get(time)
    other_time = clean_time.to(tz_name)
    if other_time is None:
        return HttpResponse(error_msg)
    else: return HttpResponse(other_time)


def main():
    lat = 35.29
    long = -89.66
    time = '2016-08-25T10:40:15-07:00'
    current_time = get_time()
    timezone = get_timezone_fromLatLong(_, latlong)
    tz_time = get_time_in_timezone(latlong)
    diff_tz_time = get_time_based_on_other_timezone(latlong, time)
    return diff_tz_time

if __name__ == '__main__':
    main()