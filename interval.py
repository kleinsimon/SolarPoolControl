#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time, config, control

state=0

def run(stop_event):
	global state

	while not stop_event.wait(1):
		if control.waittime>config.intervallPause*60:
			if control.runtime<config.intervallRuntime*60:
				state=1
		if control.waittime >= (config.intervallPause+config.intervallRuntime)*60:
			control.waittime=0