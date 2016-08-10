#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time, sys, config
from subprocess import call, check_output

curState=0
call(config.commandOff)

def switch(on):
	global curState 
	if (on and not curState):
		#call(["gpio","write","0", "0"])
		#call(["gpio","write","1", "0"])
		call(config.commandOn)
		call(config.commandOn)
		print('Switch on')
		curState=1
		
	elif (not on and curState):
		#call(["gpio","write","0", "1"])
		#call(["gpio","write","1", "1"])
		call(config.commandOff)
		call(config.commandOff)
		print('Switch off')
		curState=0

if __name__ == "__main__":
	if len(sys.argv) == 1:
		command = ""
	else:
		command = sys.argv[1]

	if command == "on":
		switch(True)
	elif command == "off":
		switch(False)

  
