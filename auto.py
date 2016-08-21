#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import config, sensor, display

state=0

def run(stop_event):
	global state
	mindiff=config.autoTempDiff
	wait=config.autoToggleWait

	while not stop_event.wait(1):
		s = sensor.getValues()
		if len(s) >= 2:
			dt = abs(s[0]-s[1])
			print ("T1: {:.2f}, T2: {:.2f}, Diff: {:.2f}".format(s[0], s[1], dt))
			state = dt >= config.autoTempDiff
		else:
			print ("Sensors not working")
			display.show("e")
			sensor.initSensors()

