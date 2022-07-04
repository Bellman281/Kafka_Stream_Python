import random
import datetime
import math

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

# https://gis.stackexchange.com/questions/69328/generate-random-location-within-specified-distance-of-a-given-point

def randomGeo(center,radius):
    y0 = center['latitude']
    x0 = center['longitude']
    rd = radius/111300 
    u = random.uniform(0,1)
    v = random.uniform(0,1)
    w = rd * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    dic1 = { 'latitude': y + y0 ,'longitude': x + x0}
    return dic1

def distance(lat1,lon1,lat2,lon2):
    R = 6371000
    a = 0.5 - math.cos( (lat2-lat1)*math.pi /180)/2 + math.cos(lat1+math.pi/180)
    return R * math.asin(math.sin(a))
