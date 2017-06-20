#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
import os, time, sched, sys, config, control, subprocess, runvars
import RPi.GPIO as GPIO
from threading import Timer


def getmode(pin):
	try:
		r = GPIO.input(pin)
		return int(r)==0
	except subprocess.CalledProcessError as e:
		print ("Error getting status of gpio")

def getmodes():
	pins = config.gpioBtnPins
	res = [False] * len(pins)
	for i in range(len(pins)):
		res[i] = getmode(pins[i])
	return res

def initgpio():
	pins = config.gpioBtnPins
	for pin in pins:
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(pin, GPIO.BOTH, callback=buttonchanged, bouncetime=300)

def startSetTime():
	runvars.btnMode=1
	runvars.setPos=0
	t = time.localtime()
	runvars.setH=t[3]
	runvars.setM=t[4]

def changeH(rev=False):
	if rev:
		runvars.setH -= 1
		if runvars.setH == -1:
			runvars.setH = 23
	else:
		runvars.setH += 1
		if runvars.setH == 24:
			runvars.setH = 0

def changeM(rev=False):
	if rev:
		runvars.setM -= 1
		if runvars.setM == -1:
			runvars.setM = 59
	else:
		runvars.setM += 1
		if runvars.setM == 60:
			runvars.setM = 0

def confirmSet():
	subprocess.call(["date","+%T","-s", "%d:%d:00" % (runvars.setH,runvars.setM)])
	subprocess.call(["hwclock","-w"])
	endSet()
	pass

def endSet():
	runvars.btnMode=0
		
def buttonchanged(pin=-1):
	if runvars.btnLock:
		return
	runvars.btnLock = True
	pins = config.gpioBtnPins
	time.sleep(0.2)
	btns = getmodes()
	if runvars.btnMode == 0:
		if sum(btns) == 1:
			mode = btns.index(True) + 1
			control.setmode(mode)
		elif btns == config.timeMask:
			startSetTime()
			print("switch to Time Set Mode")
	elif runvars.btnMode == 1:
		if sum(btns) == 1:
			idx = btns.index(True)
			if idx == config.timeSetBtns[0]: #Hoch
				if runvars.setPos == 0:
					changeH()
				elif runvars.setPos == 1:
					changeM()
			elif idx == config.timeSetBtns[1]: #Runter
				if runvars.setPos == 0:
					changeH(True)
				elif runvars.setPos == 1:
					changeM(True)
			elif idx == config.timeSetBtns[2]: #Weiter
				if runvars.setPos<1:
					runvars.setPos+=1
				else:
					confirmSet()
			elif idx == config.timeSetBtns[3]: #Zurück
				endSet()
	runvars.btnLock = False
	if sum(btns) != 0:
		buttonchanged(pin)

initgpio()