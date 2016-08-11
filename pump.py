#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import time, sys, config
from subprocess import call

curState=0
call(config.commandOff)
lastToggle=0

def switch(on):
	global curState, lastToggle
	if (time.time()-lastToggle) < config.pumpMinTogglePause and lastToggle!=0:
		return

	if (on and not curState):
		#call(["gpio","write","0", "0"])
		#call(["gpio","write","1", "0"])
		call(config.commandOn)
		call(config.commandOn)
		print('Switch on')
		curState=1
		lastToggle=time.time()
		
	elif (not on and curState):
		#call(["gpio","write","0", "1"])
		#call(["gpio","write","1", "1"])
		call(config.commandOff)
		call(config.commandOff)
		print('Switch off')
		curState=0
		lastToggle=time.time()

if __name__ == "__main__":
	if len(sys.argv) == 1:
		command = ""
	else:
		command = sys.argv[1]

	if command == "on":
		switch(True)
	elif command == "off":
		switch(False)

  
