import time
import datetime
#trims the time to eliminate all time elements but the hour
#trims all chars but from 11 to 13(11:13)
def timeTrim(tt):
	newTimeTrim = tt[11:13]
	return newTimeTrim

#trims time string to find only the hour, then converts to int type for use with comparison operators
def getHour():
    trimToHour = timeTrim(str(datetime.datetime.now()))
    time_hour = int(trimToHour)
    return time_hour

#determines whether to use the word "day" or "night" based on the hour
#times from 18:00 (6p) to 5:00 (5a) are considered night -- between is considered day
def timeDN(hour):
	termDN = "day"
	if hour >= 18:
		termDN = "night"
	if hour < 6:
		termDN = "night"
	return termDN
