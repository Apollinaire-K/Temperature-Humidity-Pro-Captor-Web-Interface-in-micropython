# Code Made by Mathis.M
# For a Prototype for Stacks

import utime
from dht11 import *
from machine import Pin, I2C
import time
from phew import server, connect_to_wifi
import json # Import all library required for this code to work

dht11 = DHT(16) #temperature and humidity sensor connect to the 16th GPIO (Note that you need to change it to you're own GPIO)

ip = connect_to_wifi("YouWifiSSID","YouWifiPassword") # Connecting you to your chosen wifi

print(ip) #Print you raspberry PICO ip into the consol for you to acces the web page
    
@server.route("/", methods=["GET"])
def home(request):
    t,h = dht11.readTempHumid() # temp:  humid: capter getting the information
    x = {
        "Temperature ": t,
        "Humiditer ": h,
        } 			#Making the base for the json.
    y = json.dumps(x) 		# dumping it all into the json into a varuable
    html= f""" <!doctype html>
	<html lang="en">
	    <body>
	        <main class="container">
            {y}
            </main>
	    </body>
	</html>
	"""
    return str(html) # Making the HTML for the web page to display the data collecte by the captor

@server.catchall()
def catchall(request):
    return "Page not found", 404

while True:
	print(y) #Also printing the data into the consol
    	server.run() #Running the server
