#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import sys, config, disp1602, time, runvars, pump, auto, timer
import RPi.GPIO as GPIO

def showData():
	t = time.strftime("%H:%M")
	m = config.modeNames[runvars.mode-1]
	if runvars.mode == 1 and not(timer.state):
		m = "Auto-Nacht"
	s = config.stateNames[pump.curState]
	dt = "%.3g" % (auto.dt)
	
	p1 = 16 - len(t) - len(m)
	p2 = 16 - len(s) - len(dt)
	
	disp1602.lcd_message(1, m.ljust(len(m)+p1) + t)
	disp1602.lcd_message(2, s.ljust(len(s)+p2) + dt)
	
def blink():
	pass
	
if __name__ == "__main__":
	disp1602.lcd_message(1, sys.argv[1])

  

  
