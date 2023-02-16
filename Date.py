# datetime module
import datetime

# to get date time now
x = datetime.datetime.now() # this creates date objects.
print(x)
# to get the year
print(x.year)
# to get the name of the weekday
# strftime() # generates a format
print(x.strftime("%A") + " " + str(x.month) + " " + str(x.year))
print(x.strftime("%p"))

# to get more formats : https://www.w3schools.com/python/python_datetime.asp