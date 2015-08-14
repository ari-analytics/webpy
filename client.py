import matplotlib.pyplot as plt
import urllib
import time
from drawnow import *

link = "http://192.168.0.104:8080"
f = urllib.urlopen(link)
tempC = []
def makeFig():
	plt.ylim(20,80)
	plt.title('Temperature Streaming')
	plt.grid(True)
	plt.plot(tempC, 'ro-',label='Degree C')
	plt.legend(loc='upper left')
cnt = 0
while True:
	f = urllib.urlopen(link)
	temperature = f.read()
	tempC.append(temperature)
	drawnow(makeFig)
	plt.pause(.0001)
	cnt = cnt+1
	if (cnt>50):
		tempC.pop(0)
	print "temperature= " , temperature
 


