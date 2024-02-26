import json
from geopy.geocoders import Nominatim
from tinydb import Query, TinyDB
db=TinyDB('locationdb.json')
countrydb=TinyDB('countrydb.json')

#check the cache db for the location, if not in db add it and return the location
def get_location(lat,lon, geolocator):
    q=Query()
    result=db.search((q.lat==lat) & (q.lon==lon))
    if len(result)==0:
        location = geolocator.reverse(f"{lat},{lon}",timeout=None)
        if (location):
            address = location.address
            country=location.raw['address'].get('country', '')
        else:
            address="None"
            country="None"
        db.insert({'lat':lat,'lon':lon,'country':country, 'address':address})
        return country, address
    else:
        return result[0]['country'], result[0]['address']

#open the input file and read it in
with open('slimmed.json') as f:
    data = json.load(f)


#initialize variables and also name the agent
geolocator = Nominatim(user_agent="Takeout-Location-History")
count=0
country=''
startdate='2012-08-20T19:53:45.117Z'

#for each location check the country through the geolocator revers geolocation
#if the country is different than previous, output it
for i in data:
    count+=1
    new_country, address = get_location(round(i['latitudeE7']/1e7,2),round(i['longitudeE7']/1e7,2), geolocator)
    if new_country != country:
        print(startdate[0:10]+"\t"+i['timestamp'][0:10]+"\t"+country+"\t"+address)
        country=new_country
        startdate=i['timestamp']
