# Global Variables & Imports 
import random
import message
import puzzle
from choice import *

# each result variable represents a result
r1 = "There are zombies heading your way. Knives would be great for battleing with them. "
r2 = "There are Type A zombies coming. Knives might not be enough. Do you have a sword to fight with them? "

# created object for the class
Inventory = Objects()


class Player:
  """
  creates a player class and gives a location
  """
  def __init__ (self):
    """
    self
    """
    self.self = self
    
    
  def movements (self):
    """
    it gives the puzzles that the user has to solve in order to go to the next room
    """
    Inventory.mainChoice()
    print(message.lock)
    print(puzzle.puzzle1)
    clue = input(message.hint)
    print('\n')
    if clue == "yes":
      print(message.clueOrder1)
    elif clue == "no":
      print(message.answerpuzzle)
    else:
      print(message.errorclue)
    while True:
      answer = input(message.puzzle)
      if answer == "cabde":
        print(message.congrats)
        break
      else:
        clue = input(message.hint)
        print('\n')
        if clue == "yes":
          print(message.clueOrder2)
        elif clue == "no":
          print(message.answer)
        else:
          print(message.error)
    print(message.lock)
    print(puzzle.puzzle2)
    clue2 = input(message.hint)
    print('\n')
    if clue2 == "yes":
      print(message.clueDay1)
    elif clue2 == "no":
      print(message.answerpuzzle)
    else:
      print(message.errorclue)
    while True: 