#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import time, sys, config, display
from subprocess import call

curState=2
call(config.commandOff)
lastToggle=0

def switch(on):
	global curState, lastToggle
	if (time.time()-lastToggle) < config.pumpMinTogglePause:
		return
	doSwitch(on)

def doSwitch(on):
	global curState, lastToggle

	if (on):
		call(config.commandOn)
		call(config.commandOn)
		print('Switch on')
		curState=1
		lastToggle=time.time()
		
	elif (not on):
		call(config.commandOff)
		call(config.commandOff)
		print('Switch off')
		curState=0
		lastToggle=time.time()
	display.blink()

if __name__ == "__main__":
	if len(sys.argv) == 1:
		command = ""
	else:
		command = sys.argv[1]

	if command == "on":
		switch(True)
	elif command == "off":
		switch(False)

  
