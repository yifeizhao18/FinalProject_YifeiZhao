# Global Variables & Imports 
import random
import message
import puzzle
from choice import *

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
    
    
  def puzzleOrder(self):
    """
    it gives the order puzzle.
    once it is completed, the user can move on to the next room
    """
    # do the actions first and then show the puzzle to the user
    option.mainChoice()
    print('\n')
    print(message.lock)
    print('\n')
    print(puzzle.puzzle1)
    print('\n')
    while True:
      # asks if the user wants a clue
      clue = input(message.hint)
      print('\n')
      # if they want a clue, do the following
      if clue == "yes":
        print(message.clueOrder1)
        print('\n')
        break
      # if they don't, do the following
      elif clue == "no":
        print(message.answer)
        print('\n')
        break
      # otherwise, do this and repeat the message again
      else:
        print(message.errorclue)
        print('\n')
    while True:
      # asks for the answer
      answer = input(message.puzzle)
      print('\n')
      # if the user answered correctly, do the following
      if answer == "cabde":
        print(message.congrats)
        print('\n')
        break
      # if they did not, do the following
      else:
        print(message.answerpuzzle)
        print('\n')
        while True:
          clue2 = input(message.hint)
          print('\n')
          # if they want a clue, do the follwoing
          if clue2 == "yes":
            print(message.clueOrder2)
            print('\n')
            break
          # if not, do the following 
          elif clue2 == "no":
            print(message.answer)
            print('\n')
            break
          # else, do the following and repeat the question
          else:
            print(message.error)
            print('\n')


  def puzzleDay(self):
    """
    it gives the order puzzle.
    once it is completed, the user can move on to the next room
    """
    # do the action first and then show the user the puzzle
    option.mainChoice()
    print(message.lock)
    print('\n')
    print(puzzle.puzzle2)
    print('\n')
    # asks if the user wants a clue
    while True:
      clue = input(message.hint)
      print('\n')
      # if they want a hint, do the following
      if clue == "yes":
        print(message.clueDay1)
        print('\n')
        break
      # if they do not, do the following
      elif clue == "no":
        print(message.answer)
        print('\n')
        break 
      # else do the following and repeat the question
      else:
        print(message.errorclue)
        print('\n')
    while True:
      # asks for the answer
      answer = input(message.puzzle)
      print('\n')
      # if the user answered correctly, do the following
      if answer == "friday":
        print(message.congrats)
        print('\n')
        break
      # if they did not, ask them if they want a hint
      else:
        print(message.answerpuzzle)
        print('\n')
        while True: 
          clue2 = input(message.hint)
          print('\n')
          # if they do want a hint, do the following
          if clue2 == "yes":
            print(message.clueDay2)
            print('\n')
            break
          # if they do not, do the following
          elif clue2 == "no":
            print(message.answer)
            print('\n')
            break
          # else do the following and repeat the question
          else: 
            print(message.error)
            print('\n')


  def puzzleHeight(self):
    """
    it gives the order puzzle.
    once it is completed, the user can move on to the next room
    """
    # do the action first and then show the puzzle
    option.mainChoice()
    print(message.lock)
    print('\n')
    print(puzzle.puzzle3)
    print('\n')
    while True:
      # asks if the user wants a hint
      clue = input(message.hint)
      print('\n')
      # if they want a hint, do the following
      if clue == "yes":
        print(message.clueHeight1)
        print('\n')
        break
      # if they do not, do the following
      elif clue == "no":
        print(message.answer)
        print('\n')
        break
      # else do the following and repeat the question
      else:
        print(message.errorclue)
        print('\n')
    while True:
      # asks for the answer
      answer = input(message.puzzle)
      print('\n')
      # if the answer is correct, do the following
      if answer == "r":
        print(message.congrats)
        print('\n')
        break
      # if not, do the following
      else:
        print(message.answerpuzzle)
        print('\n')
        while True: 
          clue2 = input(message.hint)
          print('\n')
          # if the user wants a hint, do the following
          if clue2 == "yes":
            print(message.clueHeight2)
            print('\n')
            break
          # if not, do the following
          elif clue2 == "no":
            print(message.answer)
            print('\n')
            break
          # else, do the following and repeat the question
          else: 
            print(message.error)
            print('\n')


  def puzzleAlphabet(self):
    """
    it gives the order puzzle.
    once it is completed, the user can move on to the next room
    """
    # do the action first and then show the puzzle
    option.mainChoice()
    print(message.lock)
    print('\n')
    print(puzzle.puzzle4)
    print('\n')
    while True:
      # asks if the user wants a hint
      clue = input(message.hint)
      print('\n')
      # if they want a hint, do the following
      if clue == "yes":
        print(message.clueAlpha1)
        print('\n')
        break
      # if they do not want a hint, do the following
      elif clue == "no":
        print(message.answer)
        print('\n')
        break
      # else, do the following and repeat the question
      else:
        print(message.errorclue)
        print('\n')
    while True:
      # asks for the answer
      answer = input(message.puzzle)
      print('\n')
      # if the answer is correct, do the following
      if answer == "n":
        print(message.congrats)
        print('\n')
        break
      # if not, do the following
      else:
        print(message.answerpuzzle)
        print('\n')
        while True: 
          clue2 = input(message.hint)
          print('\n')
          # if they want a hint, do the following
          if clue2 == "yes":
            print(message.clueAlpha2)
            print('\n')
            break
          # if not, do the following
          elif clue2 == "no":
            print(message.answer)
            print('\n')
            break
          # else, do the following and repeat the question
          else: 
            print(message.error)
            print('\n') 


  def puzzleDaughter(self):
    """
    it gives the order puzzle.
    once it is completed, the user can move on to the next room
    """
    # do the action first and then show the puzzle
    option.mainChoice()
    print(message.lock)
    print('\n')
    print(puzzle.puzzle5)
    print('\n')
    while True: 
      # asks if the user wants a hint
      clue = input(message.hint)
      print('\n')
      # if they want a hint, do the following
      if clue == "yes":
        print(message.clueDau1)
        print('\n')
        break
      # if not, do the following
      elif clue == "no":
        print(message.answer)
        print('\n')
        break
      # else, do the following and repeat the question
      else:
        print(message.errorclue)
        print('\n')
    while True:
      # asks for the answer
      answer = input(message.puzzle)
      print('\n')
      # if the answer is correct, do the following
      if answer == "m":
        print(message.congrats)
        print('\n')
        break
      # if not, do the following
      else:
        print(message.answerpuzzle)
        print('\n')
        while True: 
          clue2 = input(message.hint)
          print('\n')
          # if they want a hint, do the following
          if clue2 == "yes":
            print(message.clueDau2)
            print('\n')
            break
          # if not, do the following
          elif clue2 == "no":
            print(message.answer)
            print('\n')
            break
          # else, do the following and repeat the question
          else: 
            print(message.error)
            print('\n') 


  def puzzleRelate(self):
    """
    it gives the order puzzle.
    once it is completed, the user can move on to the next room
    """
    # do the action first and then show the puzzle
    option.mainChoice()
    print(message.lock)
    print('\n')
    print(puzzle.puzzle6)
    print('\n')
    while True:
      # asks if the user wants a hint
      clue = input(message.hint)
      print('\n')
      # if they want a hint, do the following
      if clue == "yes":
        print(message.clueRel1)
        print('\n')
        break
      # if they do not, do the following
      elif clue == "no":
        print(message.answer)
        print('\n')
        break
      # else, do the following and repeat the question 
      else:
        print(message.errorclue)
        print('\n')
    while True:
      # asks for the answer
      answer = input(message.puzzle)
      print('\n')
      # if the answer is correct, do the following
      if answer == "sisters":
        print(message.congrats)
        print('\n')
        break
      # if not, do the following
      else:
        print(message.answerpuzzle)
        print('\n')
        while True: 
          # asks if the user wants a hint
          clue2 = input(message.hint)
          print('\n')
          # if the user wants a hint, do the following
          if clue2 == "yes":
            print(message.clueRel2)
            print('\n')
            break
          # if not, do the following
          elif clue2 == "no":
            print(message.answer)
            print('\n')
            break
          # else, do the following and repeat the question
          else: 
            print(message.error)
            print('\n') 

  
  def puzzleMonth(self):
    """
    it gives the order puzzle.
    once it is completed, the user can move on to the next room
    """
    # do the action first and then show the puzzle
    option.mainChoice()
    print(message.lock)
    print('\n')
    print(puzzle.puzzle7)
    print('\n')
    while True: 
      # asks if the user wants a hint
      clue = input(message.hint)
      print('\n')
      # if the user wants a hint, do the following
      if clue == "yes":
        print(message.clueMon1)
        print('\n')
        break
      # if they do not, do the following
      elif clue == "no":
        print(message.answer)
        print('\n')
        break
      # else, do the following and repeat the question
      else:
        print(message.errorclue)
        print('\n')
    while True:
      # asks for the answer
      answer = input(message.puzzle)
      print('\n')
      # if they answered correctly, do the following
      if answer == "m":
        print(message.congrats)
        print('\n')
        break
      # if they did not, do the following
      else:
        print(message.answerpuzzle)
        print('\n')
        while True: 
          clue2 = input(message.hint)
          print('\n')
          # if they want a hint, do the following
          if clue2 == "yes":
            print(message.clueMon2)
            print('\n')
            break
          # if they do not want a hint, do the following
          elif clue2 == "no":
            print(message.answer)
            print('\n')
            break
          # else, do the following and repeat the question
          else: 
            print(message.error)
            print('\n') 