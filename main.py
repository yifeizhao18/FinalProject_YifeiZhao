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
from player import *
import sys

# create room objects
entrance = Tile("You are currently at the entrance of the hospital. There are lots of patients and doctors running around. SEEMS NORMAL... ", "Welcome to the central hospital!! It is a very stormy night. You are here because this hospital got shut done due to something abnormal. As a private investigator, you immediately stepped in to investigate. GOOD LUCK!! You will have to escape all of the rooms and be careful to not get killed. ")
emergency = Rooms("You are currently at the EMERGENCY ROOM. It used to be a very busy space, but right now, all you can hear is the deadly silence. ")
icu = Rooms("You are currently at the ICU. All you can hear is the machines beeping. This is also the FIRST room to report the abnormalities in this hospital. BE CAREFUL...")
radiology = Rooms("You are currently at the radiology toom. There are monstrous imaging machines that makes every corner of the room a great space to hide... ")
OR = Rooms("You are currently at the operating room. There are potential weapons everywhere. BE CAREFUL!! ")
psych = Rooms("This is the psychiatry room. This was the department that got shut done first. I wonder why... ")
exit = Tile("You are one step away from escaping the hospital!! Solve the last puzzle and you can get out of here!! FAST! TIME IS RUNNING OUT.. ", "Congratulations!! You have successfully escaped! Bye!! ")

# create objects for the classes
User = Player()

# Main
# prints the welcome message
try:
  with open ("external.txt", "w") as file:
    file.write(f"Welcome! {entrance.passage}")
except:
  print("File Exception")
else:
  pass
print(entrance.passage)
print('\n')
# when the user gets to the entrance, print this
print(entrance.description)
print('\n')
User.puzzleOrder()
# when the user gets to the emergency, print this
print(emergency.description)
print('\n')
User.puzzleDay()
# when the user gets to the radiology, print this
print(radiology.description)
print('\n')
User.puzzleHeight()
# when the user gets to the icu, print this
print(icu.description)
print('\n')
User.puzzleAlphabet()
# when the user gets to the OR, print this
print(OR.description)
print('\n')
User.puzzleDaughter()
# when the user gets to the psych, print this
print(psych.description)
print('\n')
User.puzzleRelate()
# when the user is at the exit, print this
print(exit.description)
print('\n')
User.puzzleMonth()
# prints the ending message
print(exit.passage)
sys.exit()