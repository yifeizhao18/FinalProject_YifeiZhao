# Global Variables & Imports
import message
import sys
from randomResult import *

# created a list of the choices the player can do
action = ["walk", "inventory", "search", "quit"]

# created the object for the class
Inventory = Objects()


class Action:
  """
  a class for all of the actions
  """
  def __init__ (action, message, description):
    """
    the messages and the descriptions for each action
    """
    action.message = message
    action.description = description

  
  def mainChoiceMessages(action): 
    """
    prints the descriptions and the messages for each action
    """
    # prints the description for that action
    print(action.description)
    print('\n')
    # prints the message for the action
    print(action.message)
    print('\n')


class Alternative:
  """
  this class is for the possible actions the user can take in a room
  """
  def __init__ (choice):
    """
    choice
    """
    choice.choice = choice

  
  def mainChoice(choice):
    """
    it asks for the user's action
    """
    while True:
      # prints the options for action
      print("Possible actions: ")
      for key in action:
        print(f"- {key}")
      # asks for the action
      actionChoice = (input(message.action))
      print('\n')
      # if the user chose walk as their action, do this
      if actionChoice == "walk":
        Walk.mainChoiceMessages()
        print(message.actionFinish)
        break
      # if the user chose search as their action, do this
      elif actionChoice == "search":
        Search.mainChoiceMessages()
        Inventory.outcome()
        print('\n')
        print(message.actionFinish)
        break
      # if the user chose quit as their action, do this
      elif actionChoice == "quit":
        Quit.mainChoiceMessages()
        sys.exit()
      # if the user chose inventory as their action, do this
      elif actionChoice == "inventory":
        Inv.mainChoiceMessages()
        print("Inventories: ")
        for item in Inventory.inventory:
          print(f"- {item}")
          print('\n')
        print('\n')
        print("Medicines: ")
        for meds in Inventory.medicine:
          print(f"- {meds}")
          print('\n')
        print('\n')
        print("Foods: ")
        for food in Inventory.food:
          print(f"- {food}")
          print('\n')
        print('\n')
        print('\n')
        print(message.actionFinish)
        break
      # if the user chose none of the above, do the following
      else:
        print("No Capital Letters! ")
        print('\n')


# create action objects
Walk = Action("Currently Walking Around!", "You will be able to walk around the room. ")
Search = Action("Searching for possible objects! ", "You will be able to search the room. ")
Inv = Action("These are your current inventories. ", "If you do not see anything in it, that is because you have not collected anything yet. ")
Quit = Action("Thank you for playing. Bye!! ", "The game will stop. ")