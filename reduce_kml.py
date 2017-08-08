import sys
import re
from geopy.distance import vincenty
 
#Takes a Google location kml export file and filters out points that are closer to the last output
#point than the sensitivity threshhold
#To invoke, use #python reduce_kml.py Google_Location.kml > outfile.kml

#For example, if the threshhold is 10 miles and the kml has three points, the first two are within 10 miles
#of each other, then the output will contain only the first and third points.

#miles of sensitivity
SENSITIVITY = 10

#read the KML file
kml_file = open (sys.argv[1], 'r')
kml_text = kml_file.read()
kml_file.close()

last_long=0;
last_lat=0;
count=0

for when,where in re.findall(r'\<when\>(.+?)\<\/when\>\s+\<gx\:coord\>(.+?)\<\/gx\:coord\>',kml_text):
 #kml does longitude before latitude
 (longitude, latitude, altitude) = where.split(' ')
 if vincenty((latitude, longitude), (last_lat, last_long)).miles >= SENSITIVITY:
  print '<when>'+when+'</when>'
  print '<gx:coord>'+longitude + ' ' + latitude + ' 0</gx:coord>'
  count=count+1
  (last_lat, last_long) = (latitude, longitude) 
