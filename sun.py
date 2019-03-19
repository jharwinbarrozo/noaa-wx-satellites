#!/usr/bin/env python2
import ephem
import time
import sys

date = time.strftime('%Y-%m-%d %H:%M:%S')

obs=ephem.Observer()
obs.lat=''
obs.long=''
obs.date = date

sun = ephem.Sun(obs)
sun.compute(obs)
sun_angle = float(sun.alt) * 57.2957795 # Rad to deg
print int(sun_angle)
