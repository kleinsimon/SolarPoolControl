#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import os, time, sys, subprocess, threading, pump, auto, interval, config, runvars, timer, display, buttons

modechar=[0,"a","i","1","0"]
		
def setmode(m):
	global modechar
	if m!=runvars.mode:
		print("Switch to mode "+str(m))
		runvars.mode = m
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
	setmode(readSavedMode())


	while True:
		setstate()
		display.showData()
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
	
	try:
		main()
		
	except KeyboardInterrupt:
		GPIO.cleanup()
