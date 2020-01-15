#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 03:00:20 2020

@author: liam
"""

#Don't have a native temp calculator, so let's make one at 3am
tempf = input("Enter Temp (F) Here: ")
resultC = float(tempf) - int(32)
resultC2 = float(resultC) * int(5)
resultC3 = float(resultC2) / int(9)
print("Celcius: " )
print(resultC3 )
#I'm adding Kelvin to try and find a niche with this
#Code might be messy, but its 3am

print("Kelvin: ")
print(resultC3 + float(273.15))