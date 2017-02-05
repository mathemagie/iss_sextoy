import time
import urllib2
import urllib
import json
from  LatLongUTMconversion import * 

ip = "192.168.0.23"
port = "14127"

def get_iss_position():
	req = urllib2.Request("http://api.open-notify.org/iss-now.json")
	response = urllib2.urlopen(req)
	obj = json.loads(response.read())
	return obj['iss_position']['latitude'], obj['iss_position']['longitude']

def vibrate(level=10,duration=1):
	url = 'http://' + ip + ':' + str(port) + '/Vibrate?v=' + str(level)
	url_stop = 'http://' + ip + ':' + str(port) + '/Vibrate?v=0'
	#print (url)
	try:
		print "vibrate level " + str(level) + " during " + str(duration)
		response = urllib.urlopen(url)
		time.sleep(duration)
		response = urllib.urlopen(url_stop)
	except IOError:
		print ("connection refused, launch body chat please")

while 1:
	lat, lng = get_iss_position()
	lat = float(lat)
	lng = float(lng)
	print lat,lng
	(z, e, n) = LLtoUTM(23,lat, lng)
   	print z,e,n
   	if z == '18F':vibrate(20,0.5)
	time.sleep(4)