import re
from geopy.geocoders import GoogleV3
import sys
import csv

#Take in a Google kml location file and export a csv with date and addresses
#should start with PYTHONIOENCODING=utf-8 and give it the inputfile as the argument
#would love to be pointed to the more appropriate way to do this in python.

#To invoke: #PYTHONIOENCODING=utf-8 python get_addresses.py input_file.kml
#will produce input_file.kml.csv 

#note that this script does not make any attempt to do the rate limiting google expects
#you should break your location data up into chunks that require less than 2500 calls
#for example, by using the split utility

#use your own key
import location_config as cfg
geolocator = GoogleV3(api_key=cfg.my_Google_api_key)

#read the KML file
kml_file = open (sys.argv[1], 'r')
kml_text = kml_file.read()
kml_file.close()

#open the CSV output file
outputfile  = open((sys.argv[1]+'.csv'), "wb")
writer = csv.writer(outputfile)

count = 0
for when,where in re.findall(r'\<when\>(.+?)\<\/when\>\s+\<gx\:coord\>(.+?)\<\/gx\:coord\>',kml_text):
 #kml does longitude before latitude
 (longitude, latitude, altitude) = where.split(' ')
 location = geolocator.reverse((latitude + ', '+ longitude), exactly_one=True)
 if location:
  #eventually it would be good to fix this to do real csv
  writer.writerow([when] + location.address.split(","))
 else: 
  print "Couldn't find: "+when+','+latitude+','+longitude+',NONE'

outputfile.close()
