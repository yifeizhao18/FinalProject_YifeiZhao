##############################################################################
# Title: Final Project

# Class: Computer Science 30 P1 S2

# Date: May 15, 2023

# Coder's Name: Yifei Zhao

# Version: 001
##############################################################################
"""
description...
"""
##############################################################################
# Global Variables & Imports
from room import * 
import sys

# create room objects
entrance = Tile("You are currently at the entrance of the hospital. There are lots of patients and doctors running around. SEEMS NORMAL... ", "Welcome to the central hospital!! It is a very stormy night. You are here because this hospital got shut done because something abnormal was going on. As a private investigator, you immediately stepped in to investigate. GOOD LUCK!! You will have to escape all of the rooms and be careful to not get killed. ")
emergency = Rooms("You are currently at the EMERGENCY ROOM. It used to be a very busy space, but right now, all you can hear is the deadly silence. ")
icu = Rooms("You are currently at the ICU. All you can hear is the machines beeping. This is also the FIRST room to report the abnormalities in this hospital. BE CAREFUL...")
radiology = Rooms("You are currently at the radiology toom. There are monstrous imaging machines that makes every corner of the room a great space to hide... ")
OR = Rooms("You are currently at the operating room. There are potential weapons everywhere. BE CAREFUL!! ")
psych = Rooms("This is the psychiatry room. This was the department that got shut done first. I wonder why... ")
exit = Tile("You are one step away from escaping the hospital!! Solve the last puzzle and you can get out of here!! FAST! TIME IS RUNNING OUT.. ", "Congratulations!! You have successfully escaped! Bye!! ")


Playing = True
print(entrance.passage)
while Playing:
  print(entrance.description)
  print(emergency.description)
  print(radiology.description)
  print(icu.description)
  print(OR.description)
  print(psych.description)
  print(exit.description)
  print(exit.passage)
  sys.exit()