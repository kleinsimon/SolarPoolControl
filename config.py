#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

##Standardmodus nach dem Einschalten des Controllers:
modeNames = ["Auto","Timer","An", "Aus"]
stateNames = ["P0","P1"]
nightName = "Nacht"

defaultMode = 2
# Befehl zum Einschalten:
commandOn=["pilight-send","-S", "127.0.0.1","-P", "5000","-p", "quigg_gt9000", "-i", "656022", "-u", "1", "-t"]
# Befehl zum Ausschalten:
commandOff=["pilight-send","-S", "127.0.0.1","-P", "5000","-p", "quigg_gt9000", "-i", "656022", "-u", "1", "-f"]

## Allgemeine Variablen

#Begin der Ruhezeit (Abends). Format: HHMM also 1730 für 17:30
timerBeginSilence = 1700

#Ende der Ruhezeit (Morgens). Format: HHMM also 1000 für 10:00
timerEndSilence = 1000

#Mindestzeit zwischen Schaltvorgängen (Sekunden)
pumpMinTogglePause = 10

## Einstellungen für Intervallschaltung
# Pumpe alle N Minuten einschalten
intervallPause = 60

# Pumpe für N Minuten einschalten
intervallRuntime = 5

## Einstellungen für Auto (Temperaturdifferenzschaltung)
#Temperaturdifferenz zum Einschalten
#autoTempDiff=0.8

#Temperaturänderung zum Schalten
#autoTempChange=0.15

#Anzahl an stetigen Temperatuen zum Schalten
#autoTempsLength=13

#Differenz zum ein / aussschalten. 4°C an, 2°C Aus

autoTempOn = 4
autoTempOff = 2

#Mindestzeit zwischen den Schaltvorgängen (Sekunden)
#autoToggleWait=30

#Laufzeit interval (0.05 = 50ms)
runtimeSleep=0.05

#Sensor Path
sensorPath="/sys/bus/w1/devices/"

#Save Path
savePath="/mnt/mmcblk0p2/conf/"

#Dateiname
saveFile="pumpmode.txt"

#GPIO Pins für Display (Nach BCM)
#gpioPins=[0,1,3,4,5,10,11]
#gpioDotPin=6
gpioPins=[17,18,22,23,24,8,7]
gpioDotPin=25

#Control GPIOs 1 2 3 4
gpioBtnPins=[19,26,6,13]
