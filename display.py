#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import sys, config, disp1602, time, runvars, pump, auto, timer, sensor
import RPi.GPIO as GPIO

doblink=False

def showData():
	global doblink
	if runvars.btnMode == 1:
		if runvars.setPos==0:
			t=">%02d:%02d" % (runvars.setH, runvars.setM)
		else:
			t="%02d>%02d" % (runvars.setH, runvars.setM)
	else:
		t = time.strftime("%H:%M")
	
	m = config.modeNames[runvars.mode-1]
	if runvars.mode == 1 and not(timer.state):
		m = config.nightName
	m = config.stateNames[pump.curState] + " " + m
	if len(sensor.sensors) >= 2:
		s1 = sensor.sensors[0].value
		s2 = sensor.sensors[1].value
	else:
		s1 = 0
		s2 = 0
	dt = "%.1f, %.1f > %.1f" % (s1, s2, abs(s2-s1))

	if doblink:
		dt += " -"
		doblink=False
	
	p1 = 16 - len(t) - len(m)
	
	disp1602.lcd_message(1, m.ljust(len(m)+p1) + t)
	disp1602.lcd_message(2, dt.ljust(16))


def blink():
	global doblink
	doblink=True
	
if __name__ == "__main__":
	disp1602.lcd_message(1, sys.argv[1])

