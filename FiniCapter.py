import utime
from dht11 import *
from machine import Pin, I2C
import time
from phew import server, connect_to_wifi
import json

dht11 = DHT(16) #temperature and humidity sensor connect to D18 port
adcpin = 4
sensor = machine.ADC(adcpin)
ip = connect_to_wifi("Wifi-Test-Mathis","I_Love_Blondie")

print(ip)
    
@server.route("/", methods=["GET"])
def home(request):
    t,h = dht11.readTempHumid() # temp:  humid:
    x = {
        "Temperature ": t,
        "Humiditer ": h,
        }
    y = json.dumps(x)
    html= f""" <!doctype html>
	<html lang="en">
	    <body>
	        <main class="container">
            {y}
            </main>
	    </body>
	</html>
	"""
    return str(html)

@server.catchall()
def catchall(request):
    return "Page not found", 404

while True:

    server.run()

    
   
    
    print(y)

    
