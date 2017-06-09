#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import config, sensor, display, runvars

state=0
dt=0

def run(stop_event):
	global state, dt

	while not stop_event.wait(1):
		s = sensor.getValues()
		if len(s) >= 2:
			dt = abs(s[0]-s[1])
			print ("T1: {:.2f}, T2: {:.2f}, Diff: {:.2f}".format(s[0], s[1], dt))

			#if (runvars.tFalling() and runvars.maxDiff() >= config.autoTempChange) or dt < config.autoTempDiff:
			#	state = False
			#elif runvars.tRising() and dt >= config.autoTempDiff:
			#	state = True
			#runvars.addTemp(dt)
			if dt >= config.autoTempOn:
				state = True
			elif dt <= config.autoTempOff:
				state = False

		else:
			print ("Sensors not working")
			display.show("e")
			sensor.initSensors()

