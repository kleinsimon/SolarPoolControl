#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time, config, control, runvars

state=0

def run(stop_event):
	global state

	while not stop_event.wait(1):
		if runvars.waittime > config.intervallPause*60:
			if runvars.runtime<config.intervallRuntime*60:
				print("Zeit ist rum... einschalten")
				state=1
			else:
				print("Und wieder aus")
				runvars.runtime=0
				runvars.waittime=0
				state=0
