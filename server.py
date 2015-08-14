#!/usr/bin/python
import web
import random
from nanpy import Arduino
from nanpy import serial_manager
serial_manager.connect('/dev/ttyACM0')
from time import sleep
import time
analogPort = 0
powervoltage = 5.

urls = (
	'/','index'
)

class index:
	def GET(self):
	#   x = []
           while True:  
	                print "start to get the temperature info....."
			while True:
			   sensorValue = Arduino.analogRead(analogPort)
			   temperature = (sensorValue/1023.)*powervoltage*100
			   return temperature

if __name__=="__main__":
	app = web.application(urls,globals())
	app.run()


