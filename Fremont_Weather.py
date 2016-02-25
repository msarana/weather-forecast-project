'''
Created on Feb 24, 2016

@author: User
'''
import urllib, json
import unittest

class YahooAPITest(unittest.TestCase):
    
    def testSunsetTime(self):
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select astronomy.sunset from weather.forecast where woeid=2407405"
        yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.urlopen(yql_url).read()
        data = json.loads(result)
        self.assertEqual(data['query']['results']['channel']['astronomy']['sunset'], "5:56 pm", "Invalid sunset time")

    def testSunriseTime(self):
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select astronomy.sunrise from weather.forecast where woeid=2407405"
        yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
        result = urllib.urlopen(yql_url).read()
        data = json.loads(result)
        self.assertEqual(data['query']['results']['channel']['astronomy']['sunrise'], "6:47 am", "Invalid sunrise time")

suite = unittest.TestLoader().loadTestsFromTestCase(YahooAPITest)
unittest.TextTestRunner(verbosity=2).run(suite)

