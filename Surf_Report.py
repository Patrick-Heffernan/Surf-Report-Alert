import json
import requests
import time
import datetime
import ezgmail


#Insert your own API Key Here
API_ID = '*'

#Feel free to include as many or as few fields of data as possible... I only took the ones that I was interested in knowing
url = "http://magicseaweed.com/api/%s/forecast/?spot_id=386&units=us&fields=timestamp,solidRating,fadedRating,swell.absMinBreakingHeight,swell.absMaxBreakingHeight,swell.absHeight,wind.compassDirection" % (API_ID)

#pulls data from the API
response = requests.get(url)
surfData = json.loads(response.text)

first = surfData[2] #index @ 2 for current conditions at 8AM, can change it to any 3hr window of the day

#parse data from the current conditions
timestamp = first["timestamp"]
date = datetime.datetime.fromtimestamp(timestamp)
date_readable = date.strftime("%I %p %A, %B %d")
stars = first["solidRating"]+(first["fadedRating"]/2)
wind = first["wind"]
windDir = wind["compassDirection"]
waves = first["swell"]
wavemin = waves["absMinBreakingHeight"]
wavemax = waves["absMaxBreakingHeight"]


#Email Content, including address, subject line, and body content... alternatively you can just print everything and have the result here in python
email_address = "Insert Email Address"
subject = 'Location Surf Conditions for ' + str(date_readable) #for the given day
wave_height = " Wave Height: " + str(wavemin) + "-" + str(wavemax) + "ft"
wind_info = "\n Wind Direction: " + str(windDir)
star_info = "\n MSW Stars: " + str(stars)

ezgmail.send(email_address, subject, wave_height + wind_info + star_info)
