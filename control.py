#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time, sys, subprocess, threading, pump, auto, interval, config

#System wide variables
waittime=config.intervallPause * 60
runtime=0

def getmode(pin):
	try:
		r = subprocess.check_output(["gpio","read",str(pin)])
		return int(r)==0
	except subprocess.CalledProcessError as e:
		print ("Error getting status of gpio")


def initgpio(pins):
	for p in pins:
		subprocess.call(["gpio","mode",str(p),"in"])
		subprocess.call(["gpio","mode",str(p),"up"])
		
def setmode(m):
	global mode, runtime
	state=0
	if m==mode:
		return
	print("Mode "+str(m))
	if m==1:
		state = auto.state and interval.state
	if m==2:
		state = interval.state
	if m==3:
		state = 1
	if m==4:
		state = 0
	mode = m
	pump.switch(state)
	if state:
		runtime+=1

def main():
	global mode
	mode=0
	modes=[1,2,3,4]
	pins=[24,25,22,23]
	interval=0.05
	initgpio(pins)
	setmode(config.defaultMode)

	while 1:
		for m in modes:
			if getmode(pins[m-1]):
				setmode(m)
		
		time.sleep(interval)

if __name__ == "__main__":
	stopthread=threading.Event()
	thread = threading.Thread(target=auto.run, args=(stopthread,), name='pumpauto')
	thread.start()
	threadistop=threading.Event()
	threadi = threading.Thread(target=interval.run, args=(threadistop,), name='pumpinter')
	threadi.start()
	main()