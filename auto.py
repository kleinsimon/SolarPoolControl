#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time, pump, config
from subprocess import call, check_output

state=0

# function: read and parse sensor data file
def read_sensor(path):
	value = 0
	try:
		f = open(path, "r")
		line = f.readline()
		if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
			line = f.readline()
			m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
			if m:
				value = (float(m.group(2)) / 1000.0)
		f.close()
	except IOError as e:
		pass
		#print (time.strftime("%x %X"), "Error reading", path, ": ", e)
	return value

def getmode():
	try:
		r = check_output(["gpio","read","0"])
		return int(r)!=1
	except subprocess.CalledProcessError as e:
		print ("Error getting status of gpio0")

def run(stop_event):
	global state
	mindiff=config.autoTempDiff
	wait=config.autoToggleWait

	interval=1		#Alle N Sekunden messen
	lastmode=getmode()	#Letzter Zustand: true: an, false: aus
	lastswitch=0		#Wartezeit seit dem letzten Schalten

	while not stop_event.wait(interval):
		t0 = time.time()
		t1 = read_sensor("/sys/bus/w1/devices/28-031643fad8ff/w1_slave")
		t2 = read_sensor("/sys/bus/w1/devices/28-03164402efff/w1_slave")
		dt = abs(t2-t1)

		waited = (time.time()-lastswitch)
		#print ('T1: {:.2f}, T2: {:.2f}, Diff: {:.2f}, Waited: {:.2f}, Ontime: {:.2f}'.format(t1, t2, dt, waited, ontime))
		if (waited >= wait):	#Wartezeit abgelaufen
			mode = dt >= mindiff	#Wenn Temperaturdifferenz größer als erfordert
			if (mode!=lastmode):
				lastmode=mode
				state=mode
				lastswitch=time.time()


