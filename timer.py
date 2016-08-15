#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import time, config, vars, control

state=2

def run(stop_event):
	global state

	while not stop_event.wait(2):
		now = int(time.strftime("%H%M"))
		os = state
		state = now >= config.timerEndSilence and now < config.timerBeginSilence
		if state != os:
			if state:
				print("Daytime")
			else:
				print("Nighttime")
				if vars.mode == 3:
					vars.mode == 4
					control.setstate()