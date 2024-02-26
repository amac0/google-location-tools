# google-location-tools

A set of scripts to process Google timeline files to produce useful extracts of the information. More info at: [https://www.bricoleur.org/2024/02/google-timeline-to-countries-and-dates.html]
and, if you have any issues, please @message me on Mastodon as [@amac@mastodon.social](https://mastodon.social/@amac) or Threads as [@amac0](https://www.threads.net/@amac0).

reduce_json.py -- takes Records.json from Google Takeout of Google Timeline and creates slimmed.json which contains only points at least 50 miles apart

find_countries.py -- takes slimmed.json and outputs a list of dates and countries for any changes in country from slimmed.json

Bother scripts use geopy. The second script maintains a cache of reverse geolocations as per the requirements in geopy.

This repository also contains some old files based on Google's old format of location history. See https://www.bricoleur.org/2017/09/google-location-history-to-country-chart.html
