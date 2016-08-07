#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

##Standardmodus nach dem Einschalten des Controllers:
defaultMode = 1
# Befehlt zum einschalten:
commandOn=["pilight-send","-p", "quigg_gt9000", "-i", "656022", "-u", "1", "-t"]
commandOff=["pilight-send","-p", "quigg_gt9000", "-i", "656022", "-u", "1", "-f"]

## Einstellungen für Intervallschaltung
# Pumpe alle N Minuten einschalten
intervallPause = 60
# Pumpe für N Minuten einschalten
intervallRuntime = 10

## Einstellungen für Auto (Temperaturdifferenzschaltung)
#Temperaturdifferenz zum Einschalten
autoTempDiff=3
#Mindestzeit zwischen den Schaltvorgängen (Sekunden)
autoToggleWait=30

