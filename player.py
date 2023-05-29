# Global Variables & Imports 
import random
import message
import puzzle
from choice import *

# each result variable represents a result
r1 = "There are zombies heading your way. Knives would be great for battleing with them. "
r2 = "There are Type A zombies coming. Knives might not be enough. Do you have a sword to fight with them? "

# created object for the class
option = Alternative()


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
    option.mainChoice()
    print('\n')
    print(message.lock)
    print('\n')
    print(puzzle.puzzle1)
    print('\n')
    clue = input(message.hint)
    print('\n')
    if clue == "yes":
      print(message.clueOrder1)
      print('\n')
    elif clue == "no":
      print(message.answer)
      print('\n')
    else:
      print(message.errorclue)
      print('\n')
    while True:
      answer = input(message.puzzle)
      print('\n')
      if answer == "cabde":
        print(message.congrats)
        print('\n')
        break
      else:
        print(message.answerpuzzle)
        print('\n')
        clue2 = input(message.hint)
        print('\n')
        if clue2 == "yes":
          print(message.clueOrder2)
          print('\n')
        elif clue2 == "no":
          print(message.answer)
          print('\n')
        else:
          print(message.error)
          print('\n')
    print(message.lock)
    print('\n')
    print(puzzle.puzzle2)
    print('\n')
    clue = input(message.hint)
    print('\n')
    if clue == "yes":
      print(message.clueDay1)
      print('\n')
    elif clue == "no":
      print(message.answer)
      print('\n')
    else:
      print(message.errorclue)
      print('\n')
    while True:
      answer = input(message.puzzle)
      print('\n')
      if answer == "friday":
        print(message.congrats)
        print('\n')
        break
      else:
        print(message.answerpuzzle)
        print('\n')
        clue2 = input(message.hint)
        print('\n')
        if clue2 == "yes":
          print(message.clueDay2)
          print('\n')
        elif clue2 == "no":
          print(message.answer)
          print('\n')
        else: 
          print(message.error)
          print('\n')