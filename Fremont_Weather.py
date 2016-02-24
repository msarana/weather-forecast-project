'''
Created on Feb 24, 2016

@author: User
'''
import urllib2, urllib, json
baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select astronomy.sunset from weather.forecast where woeid=2407405"
yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
result = urllib.urlopen(yql_url).read()
data = json.loads(result)
print "Today's sunset time is " + data['query']['results']['channel']['astronomy']['sunset']

