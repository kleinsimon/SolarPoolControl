#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time, sys
from subprocess import call, check_output

curState=0

def switch(on):
	global curState 
	if (on and not curState):
		call(["gpio","write","0", "0"])
		call(["gpio","write","1", "0"])
		print('Switch on')
		curState=1
		
	elif (not on and curState):
		call(["gpio","write","0", "1"])
		call(["gpio","write","1", "1"])
		print('Switch off')
		curState=0

def getmode(pin):
	try:
		r = check_output(["gpio","read",str(pin)])
		return int(r)==0
	except subprocess.CalledProcessError as e:
		print ("Error getting status of gpio")

if len(sys.argv) == 1:
	command = ""
else:
	command = sys.argv[1]

if command == "on":
	switch(True)
elif command == "off":
	switch(False)

  
