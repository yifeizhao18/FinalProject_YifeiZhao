import random
import message
from choice import *


r1 = "There are zombies heading your way. Knives would be great for battleing with them. "
r2 = "There are Type A zombies coming. Knives might not be enough. Do you have a sword to fight with them? "


class Player:
  """
  """
  def __init__ (self, row, col):
    self.row = row
    self.col = col 


  def movements (self):
    """
    """
    while True:
      Inventory.mainChoice()
      # PUZZLES
      clue = input(message.hint)
      print('\n')
      if clue == "yes":
        print(message.clue1)
      elif clue == "no":
        print(message.answer)
      else:
        print(message.error)