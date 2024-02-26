import json
from geopy.distance import geodesic

SENSITIVITY = 50 # miles
lat, lon = 0, 0
slimmed_data = []

#open the json file
with open('Records.json') as f:
    data = json.load(f)

#print the number of locations in the input file
print(len(data['locations']))

#go through the locations
#add the locations to the slimmed data array if they are over the sensitivity
#from the previous location added
#note that the locations have to be converted as Google records them in 1e7 format
for i in  data['locations']:
    if 'latitudeE7' not in i:
        continue
    if geodesic((lat, lon), (i['latitudeE7']/1e7, i['longitudeE7']/1e7)).miles > SENSITIVITY:
        slimmed_data.append(i)
        lat, lon = i['latitudeE7']/1e7, i['longitudeE7']/1e7

#print the number of locations in the output file
print(len(slimmed_data))                

#output to a slimmed down file
with open('slimmed.json', 'w') as f:
    json.dump(slimmed_data, f, indent=4)
