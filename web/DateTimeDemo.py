#Import datetime Library
from datetime import datetime,timedelta

#This module serves the date-time conversion functionalities
#and helps users serving intenational client bases
import pytz

#Create a datetime with the specified year, month, day
d = datetime(2011,9,12)
#Format of the return string
print(d.strftime("%B,%d,%A,%x,\n%c"))
print(f"Timestamp for Sep 1, 2011: {d.timestamp()}")

#Creaete a dateime for the current time
d = datetime.now()
print(f"Year: {d.year} | Month: {d.month} | Day: {d.day} | \
Hour: {d.hour} | Minute: {d.minute} | Second: {d.second}")

#Create a datetime with a future date
fd1 = d + timedelta(days = 730)
fd2 = d + timedelta(days = 2)

print(f"The date for 2 years in the future is {fd1}")
print(f"The date for 2 days in the future is {fd2}")

#FInd the time difference
print(f"The time difference between fd1 and fd2 is {fd1 - fd2}")

#Create a datetime with the specified timestamp
d = datetime.fromtimestamp(1315803600.0)
print(f"Year: {d.year} | Month: {d.month} | Day: {d.day} | \
Hour: {d.hour} | Minute: {d.minute} | Second: {d.second}")

#Timezones in Datetime can be used in the case where you might
#want to display time according to the timezone

#Display the all timezones
#for tz in pytz.all_timezones:
    #print(tz)

format = "%Y-%m-%d %H:%M:%S %Z%z"

#Current Time
now_cdt = datetime.now(pytz.timezone('America/Chicago'))
print(now_cdt.strftime(format))







































