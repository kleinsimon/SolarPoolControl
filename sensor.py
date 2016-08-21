#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time, sys, config

sensors=None

def readSensor(path):
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
		print (time.strftime("%x %X"), "Error reading", path, ": ", e)
	return value

def getSensors():
	sensors=[]
	slist=os.listdir(config.sensorPath)
	for s in slist:
		p=config.sensorPath+ "/" + s + "/w1_slave"
		if os.path.exists(p):
			sensors.append(p)
	return sensors

def getValues():
	global sensors
	res=[]
	for s in sensors:
		res.append(readSensor(s))
	return res

def initSensors():
	global sensors
	sensors=getSensors()

initSensors()

if __name__ == "__main__":
	print (getValues())

  
