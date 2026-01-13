# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(fn: str)->dict:
    res={}

    with open(fn) as new_file:
        for word in new_file:
            ls = word.split(";")
            if ls[0]=='Longitude':
                continue
            else:
                res[ls[3]]=(float(ls[0]),float(ls[1]))
            #print(word)

    return res

def distance(d :dict, st1: str, st2: str)->float:
    res=0.0

    lo1,la1=d[st1]
    lo2,la2=d[st2]
    x_km = (lo1 - lo2) * 55.26
    y_km = (la1 - la2) * 111.2
    res = math.sqrt(x_km**2 + y_km**2)

    return res

def greatest_distance(d: dict)->tuple:
    max_dist=0
    max_1=""
    max_2=""

    stations=d.keys()
    for st1 in stations:
        for st2 in stations:
            dis = distance(d,st1,st2)
            if dis>max_dist:
                max_dist=dis
                max_1=st1
                max_2=st2


    return (max_1,max_2,max_dist)

if __name__ == '__main__':
#    stations = get_station_data('stations1.csv')
#    d = distance(stations, "Designmuseo", "Hietalahdentori")
#    print(d)
#    d = distance(stations, "Viiskulma", "Kaivopuisto")
#    print(d)

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)