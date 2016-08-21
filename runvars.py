#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import config
#System wide variables
waittime=0
runtime=0
mode=0
lastSwitchOnTime=0
lastTemps=[0]

def addTemp(temp):
	global lastTemps
	lastTemps.append(temp)
	if len(lastTemps) > config.autoTempsLength:
		lastTemps.pop(0)


def tRising():
	global lastTemps
	if len(lastTemps) < config.autoTempsLength:
		return False
	s = sorted(lastTemps)
	return lastTemps == s

def tFalling():
	global lastTemps
	if len(lastTemps) < config.autoTempsLength:
		return False
	s = sorted(lastTemps, reverse=True)
	return lastTemps == s

def maxDiff():
	global lastTemps
	return max(lastTemps) - min(lastTemps)