import sys
from datetime import datetime
from dateutil.parser import parse
import pytz
import csv

#Make a geochart
#https://developers.google.com/chart/interactive/docs/gallery/geochart
#from a csv file that has timestamps and addresses with the countries last
#takes one arg (the input file) and outputs the HTML to draw the chart

#To invoke: #python make_country_chart.py input_file.csv > Country_Chart.html 

#read in the csv (when is the first, country is the last)
csv_file = open (sys.argv[1], 'r')
reader = csv.reader(csv_file)
 

#use a hash to store the countries
countries={}
for items in reader:
  #the time is the first thing
  when = items[0]

  #figure out the number of years ago the vist was
  #at some point should fix this to actually use time zones when we have them
  years = int((datetime.now().replace(tzinfo=pytz.UTC) - parse(when).replace(tzinfo=pytz.UTC)).days / 365.25) 

  country=''
  #the country is the last field in the csv
  while country=='':
   country = items.pop(-1)
  #if we find a country but it is not yet in our hash or in it but a longer number of years ago, write it
  if country != 'NONE':
   if (not country in countries) or (countries[country]>years):
    countries[country]=years

csv_file.close()

#write the HTML
print '''
<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['geochart']});
      google.charts.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = google.visualization.arrayToDataTable([
          ['Country', 'Years Since Visit']
'''
for key in countries: 
  print ',[\''+key+'\', -'+str(countries[key])+']'
print '''
          ]);

        var options = {};

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="regions_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>'''
