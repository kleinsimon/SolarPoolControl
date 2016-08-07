#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
import re, os, time
from subprocess import call, check_output

mindiff=3		#Mindestens 3 C Differenz
interval=1		#Alle N Sekunden messen
wait=30			#Sekunden zwischen dem Schalten
checktime=10	#Alle N Minuten Pumpe anschalten wenn mindestlaufzeit nicht erreicht
minontime=1		#Mindestlaufzeit pro Chektime in Minuten

# function: read and parse sensor data file
def read_sensor(path):
  value = 0
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = (float(m.group(2)) / 1000.0)
    f.close()
  except IOError as e:
    print (time.strftime("%x %X"), "Error reading", path, ": ", e)
  return value

def switch(on):
  if (on):
    call(["gpio","write","0", "0"])
    #call(["gpio","write","1", "0"])
  else:
    call(["gpio","write","0", "1"])
    #call(["gpio","write","1", "1"])

def getmode():
  try:
    r = check_output(["gpio","read","0"])
    return int(r)!=1
  except subprocess.CalledProcessError as e:
    print ("Error getting status of gpio0")

lastmode=getmode()	#Letzter Zustand: true: an, false: aus
ontime=0			#Laufzeit seit der letzten Kontrolle
lastcheck=time.time()	#letzte Laufzeitkontrolle
lastswitch=0		#Wartezeit seit dem letzten Schalten

while 1:
  t0 = time.time()
  t1 = read_sensor("/sys/bus/w1/devices/28-031643fad8ff/w1_slave")
  t2 = read_sensor("/sys/bus/w1/devices/28-03164402efff/w1_slave")
  dt = abs(t2-t1)
  
  if ((time.time()-lastcheck) >= (checktime * 60)):
    print("Checking if Pump was running enough")
    if (ontime < (minontime * 60)):
      cur = lastmode;
      if (not(cur)):
        lastmode = True
        switch(True)
        lastswitch=time.time()
        print("Pump time was not enough, switching on")
        time.sleep(minontime * 60)
      else:
        print("Pump time was enough")
    lastcheck = time.time()
    ontime = 0

  waited = (time.time()-lastswitch)
  print ('T1: {:.2f}, T2: {:.2f}, Diff: {:.2f}, Waited: {:.2f}, Ontime: {:.2f}'.format(t1, t2, dt, waited, ontime))
  if (waited >= wait):	#Wartezeit abgelaufen
    mode = dt >= mindiff	#Wenn Temperaturdifferenz größer als erfordert
    if (mode!=lastmode):	
      lastmode=mode
      switch(mode)
      print("toggle")
      repr(mode)
      lastswitch=time.time()
    
  time.sleep(interval)
  if (lastmode):
    ontime += time.time()-t0

