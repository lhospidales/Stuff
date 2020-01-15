#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 03:25:45 2020

@author: liam
"""

#Gonna try and make an E-Zoltar
#First ask for a name
fort =input("What is your name?: ")

#get a random variable
from random import seed
from random import randint
seed(1)
for _ in range(1):
	x = randint(0, 7)
#now to assign values to a corresponding fate
if x <= 1:
    print("You will find much luck")
elif x <= 2:
    print("Your future is hazy")
elif x <= 3:
    print("You will do many great things")
elif x <= 4:
    print("You will lose your home to Chinese investors")
elif x <= 5:
    print("Your favorite show will come to Netflix")
elif x <= 6:
    print("Yikes, hope you have a backup plan")
elif x >= 7:
    print("I'm too tired, come back later")

#I think this works, its 3:43 though.I'll check later