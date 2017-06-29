import json
import urllib2
import graphitesend
import datetime
import time

weatherData = json.load(urllib2.urlopen("http://api.wunderground.com/api/f00bf171bdb60225/conditions/q/pws:KIDMERID50.json"))

current_observation = weatherData['current_observation']

g = graphitesend.init(prefix="weather", system_name='')
g.send("temp", current_observation['temp_f'])
humidity = current_observation['relative_humidity']
humidity = humidity.replace("%", "")
g.send("humidity", humidity)
g.send("wind", current_observation['wind_mph'])
g.send("dewpoint", current_observation['dewpoint_f'])

print "[%s] Current weather is %s.  Temperature is %sF" % (datetime.datetime.now(), current_observation['weather'], current_observation['temp_f'])
