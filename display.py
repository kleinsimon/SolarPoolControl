#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import sys, config
from subprocess import call

#translatePin=[11,12,13,15,16,18,22,7,3,5,24,26,19,21,23,8,10]
sets={}
# sets["0"] = [1,0,1,1,1,1,1]
# sets["1"] = [0,0,0,0,1,0,1]
# sets["2"] = [0,1,1,1,0,1,1]
# sets["3"] = [0,1,0,1,1,1,1]
# sets["4"] = [1,1,0,0,1,0,1]
# sets["5"] = [1,1,0,1,1,1,0]
# sets["6"] = [1,1,1,1,1,1,0]
# sets["7"] = [0,0,0,0,1,1,1]
# sets["8"] = [1,1,1,1,1,1,1]
# sets["9"] = [1,1,0,0,1,1,1]
# sets["a"] = [1,1,1,0,1,1,1]
# sets["b"] = [1,1,1,1,1,0,0]
# sets["c"] = [0,1,1,1,0,0,0]
# sets["d"] = [0,1,1,1,1,0,1]
# sets["e"] = [1,1,1,1,0,1,0]
# sets["f"] = [1,1,1,0,0,1,0]
# sets["g"] = [1,0,1,1,1,1,0]
# sets["h"] = [1,1,1,0,1,0,1]
# sets["i"] = [0,0,1,0,0,1,0]
# sets["j"] = [0,0,1,1,1,0,1]
sets["0"] = [1,0,1,1,1,1,1]
sets["1"] = [1,0,1,0,0,0,0]
sets["2"] = [0,1,1,1,0,1,1]
sets["3"] = [1,1,1,1,0,1,0]
sets["4"] = [1,1,1,0,1,0,0]
sets["5"] = [1,1,0,1,1,1,0]
sets["6"] = [1,1,0,1,1,1,1]
sets["7"] = [1,0,1,1,0,0,0]
sets["8"] = [1,1,1,1,1,1,1]
sets["9"] = [1,1,1,1,1,0,0]
sets["a"] = [1,1,1,1,1,0,1]
sets["b"] = [1,1,0,0,1,1,1]
sets["c"] = [0,1,0,0,0,1,1]
sets["d"] = [1,1,1,0,0,1,1]
sets["e"] = [0,1,0,1,1,1,1]
sets["f"] = [0,1,0,1,1,0,1]
sets["g"] = [1,0,0,1,1,1,1]
sets["h"] = [1,1,1,0,1,0,1]
sets["i"] = [0,0,0,1,0,0,1]
sets["j"] = [1,0,1,0,0,1,1]
sets["t"] = [0,1,0,0,1,1,1]


def init():
	call(["gpio","mode",str(config.gpioDotPin),"out"])
	call(["gpio","write",str(config.gpioDotPin),"0"])

	for pin in config.gpioPins:
		call(["gpio","mode",str(pin),"out"])
		call(["gpio","write",str(pin),"0"])
		
def set(vars):
	for i in range(0,len(vars)):
		call(["gpio","write",str(config.gpioPins[i]),str(vars[i])])
		
def show(char):
	global sets
	if not char in sets:
		print ("Not defined: " + str(char))
		return
	set(sets[char])
	
def blink():
	call(["gpio","write",str(config.gpioDotPin),"1"])
	call(["gpio","write",str(config.gpioDotPin),"0"])
	
init()
if __name__ == "__main__":
	show(sys.argv[1])

  

  
