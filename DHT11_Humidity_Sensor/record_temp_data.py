#!/user/bin/python
import sys
import Adafruit_DHT
import datetime
import datetime
import time
import csv
import os

FILENAME = 'temperature_data.csv'
TIMER =  60 * 15  # Get time in seconds only change second number
startlog = time.time()

temp_headers = ['Date','Year', 'Month', 'Day', 'Time', 'Temperature', 'Humidity']

# Check if file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(temp_headers)
print('press Ctrl + C to end program')
while True:
    # Only run after set time
    if time.time() - TIMER > startlog: 
	print('It is time, saving data')
	temp_data = []

   	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
   	full_datetime = datetime.datetime.now()
   	year = full_datetime.year
   	month = full_datetime.month
   	day = full_datetime.day
	curr_time = time.strftime("%H:%M:%S", time.localtime())

    	temp_data.append([full_datetime,
                      year,
                      month,
                      day,
                      curr_time,
		      temperature,
                      humidity])

    	with open(FILENAME, 'a') as csvfile:
        	# creating a csv writer object
        	csvwriter = csv.writer(csvfile)
       		# writing the data rows
        	csvwriter.writerows(temp_data)
        startlog = time.time()
