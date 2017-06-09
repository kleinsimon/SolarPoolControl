#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import os, time, sys, subprocess, threading, pump, auto, interval, config, runvars, timer, display
import RPi.GPIO as GPIO

modechar=[0,"a","i","1","0"]

def getmode(pin):
	try:
		#r = subprocess.check_output(["gpio","read",str(pin)])
		r = GPIO.input(pin)
		return int(r)==0
	except subprocess.CalledProcessError as e:
		print ("Error getting status of gpio")

def initgpio(pins):
	for p in pins:
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		#subprocess.call(["gpio","mode",str(p),"in"])
		#subprocess.call(["gpio","mode",str(p),"up"])
		
def setmode(m):
	global modechar
	if m!=runvars.mode:
		print("Switch to mode "+str(m))
		runvars.mode = m
		display.show(modechar[m])
		saveMode(m)

def setstate():
	state=0
	oldstate=runvars.mode
	if runvars.mode==1:
		state = timer.state and (auto.state or interval.state)
	if runvars.mode==2:
		state = timer.state and interval.state
	if runvars.mode==3:
		state = 1
	if runvars.mode==4:
		state = 0
	pump.switch(state)
	
	if state and not oldstate:
		runvars.lastSwitchOnTime=time.time()
	elif not state and oldstate:
		runvars.runtime+=time.time()-runvars.lastSwitchOnTime
		runvars.lastSwitchOnTime=0

def saveMode(mode):
	with open(config.savePath + "/" + config.saveFile, "w") as f:
		f.write(str(mode))
	
def readSavedMode():
	m=config.defaultMode
	try:
		with open(config.savePath + "/" + config.saveFile, "r") as f:
			m=int(f.read())
	except:
		pass
	return m
	
def main():
	modes=[1,2,3,4]
	#pins=[24,25,22,23]
	pins = config.gpioBtnPins

	initgpio(pins)
	setmode(readSavedMode())

	while 1:
		for m in modes:
			if getmode(pins[m-1]):
				setmode(m)
		setstate()

		runvars.waittime+=config.runtimeSleep
		time.sleep(config.runtimeSleep)

if __name__ == "__main__":
	stopthread=threading.Event()
	thread = threading.Thread(target=auto.run, args=(stopthread,), name='pumpauto')
	thread.start()
	
	threadistop=threading.Event()
	threadi = threading.Thread(target=interval.run, args=(threadistop,), name='pumpinter')
	threadi.start()
	
	threadtstop=threading.Event()
	threadt = threading.Thread(target=timer.run, args=(threadtstop,), name='pumptimer')
	threadt.start()
	
	main()
