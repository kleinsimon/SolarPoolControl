#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

##Standardmodus nach dem Einschalten des Controllers:
defaultMode = 2
# Befehl zum Einschalten:
commandOn=["pilight-send","-S", "127.0.0.1","-P", "5000","-p", "quigg_gt9000", "-i", "656022", "-u", "1", "-t"]
# Befehl zum Ausschalten:
commandOff=["pilight-send","-S", "127.0.0.1","-P", "5000","-p", "quigg_gt9000", "-i", "656022", "-u", "1", "-f"]

## Allgemeine Variablen

#Begin der Ruhezeit (Abends). Format: HHMM also 1730 für 17:30
timerBeginSilence = 1800

#Ende der Ruhezeit (Morgens). Format: HHMM also 1000 für 10:00
timerEndSilence = 1000

#Mindestzeit zwischen Schaltvorgängen (Sekunden)
pumpMinTogglePause = 5

## Einstellungen für Intervallschaltung
# Pumpe alle N Minuten einschalten
intervallPause = 10

# Pumpe für N Minuten einschalten
intervallRuntime = 1

## Einstellungen für Auto (Temperaturdifferenzschaltung)
#Temperaturdifferenz zum Einschalten
autoTempDiff=3

#Mindestzeit zwischen den Schaltvorgängen (Sekunden)
autoToggleWait=30

#Laufzeit interval (0.05 = 50ms)
runtimeSleep=0.05 

#Sensor Path
sensorPath="/sys/bus/w1/devices/"

#Save Path
savePath="/mnt/mmcblk0p2/conf/"

#Dateiname
saveFile="pumpmode.txt"

#GPIO Pins für Display (Nach wiringpi)
gpioPins=[0,1,3,4,5,10,11]
gpioDotPin=6