#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time, sys, config, threading

sensors=None

def getSensors():
	sensors=[]
	slist=os.listdir(config.sensorPath)
	for id in slist:
		path = config.sensorPath+ "/" + id + "/w1_slave"
		if os.path.exists(path):
			sensors.append(Sensor(id, path))
	return sensors

def getValues():
	global sensors
	res=[]
	for s in sensors:
		res.append(s.value)
	return res

def initSensors():
	global sensors
	time.sleep(1)
	try:
		sensors=getSensors()
	except:
		sensors=None
	if len(sensors)<2:
		initSensors()


def startScans():
	global sensors
	for s in sensors:
		s.startScan()

class Sensor:
	id = 0
	path = ""
	value = -1
	stopthread=threading.Event()
	thread = None
	
	def __init__(obj, id, path):
		obj.path = path
		obj.id = id
	
	def readSensor(obj):
		try:
			with open(obj.path, "r") as f:
				line = f.readline()
				if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
					line = f.readline()
					m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
					if m:
						obj.value = (float(m.group(2)) / 1000.0)
		except IOError as e:
			print (time.strftime("%x %X"), "Error reading", obj.path, ": ", e)
	
	def scan(obj, stopevent):
		while not stopevent.wait(1):
			obj.readSensor()
	
	def startScan(obj):
		obj.thread = threading.Thread(target=obj.scan, args=(obj.stopthread,), name='sensorscan'+obj.id)
		obj.thread.start()
		
	def stopScan(obj):
		obj.stopthread.set()
	
initSensors()
startScans()

if __name__ == "__main__":
	print (getValues())

  
