import sys
import csv
from dateutil.parser import parse
from datetime import datetime

#Take a csv with datetime stamps and addresses split across remaing cells and output
#a fuzzed csv that contains two columns. A datetime stamp of the first day of the year
#in which the location occured, and the country.

#call it with python fuzz_addresses.py inputfile.csv outputfile.csv

#open the CSV output file
inputfile  = open((sys.argv[1]), "r")
reader = csv.reader(inputfile)

#open the CSV output file
outputfile  = open((sys.argv[2]), "wb")
writer = csv.writer(outputfile)

for row in reader:
 #for the date, which is the first column, strip it down to the year, 
 #and make everything January 1 if you don't care about fuzzing the date, 
 #change the line below to when=row[0]
 when=parse(str( parse(row[0]).year ) +'-1-1')

 #for the address, get rid of everything but the country which is the last column that has an entry
 country=''
 while country=='':
   country = row.pop(-1)
 where=country

 #write the new row
 writer.writerow([when, where])

#close the files
inputfile.close()
outputfile.close()
