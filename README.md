# google-location-tools
A set of scripts to process Google location kml files to produce useful extracts of the information.

reduce_kml.py -- takes a large Google location kml archive and reduces it to only points that are at least some amount of distance from the last one

get_countries.py -- goes through a Google location kml archive (or reduced one) and makes a CSV with the timedate stamp and text version of that location

make_country_chart.py -- takes the csv output of get_countries.py and outputs an HTML file containing a Google country chart annotated with the number of years since each country that has been visited was visited.

Note that get_countries.py expects to access your Google Location API key in a file called location_config.py.
That file should have one variable declared like so:
my_Google_api_key = "YOUR-GOOGLE-LOCATION-API-KEY" 
