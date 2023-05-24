import message
import sys
from randomResult import *
action = ["walk", "inventory", "search", "quit"]

Inventory = Objects()


class Action:
  """
  """
  def __init__ (action, message, description):
    """
    """
    action.message = message
    action.description = description

  
  def mainChoiceMessages(action): 
    """
    """
    print(action.description)
    print('\n')
    print(action.message)
    print('\n')

  
  def mainChoice():
    """
    
    """
    while True:
      print("Possible actions: ")
      for key in action:
        print(f"- {key}")
      actionChoice = (input(message.action))
      print('\n')
      if actionChoice == "walk":
        Walk.mainChoiceMessages()
        break
      elif actionChoice == "search":
        Search.mainChoiceMessages()
        Inventory.randomResult()
        print('\n')
        break
      elif actionChoice == "quit":
        Quit.mainChoiceMessages()
        sys.exit()
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
        break
      else:
        print("No Capital Letters! ")
        print('\n')


Walk = Action("Currently Walking Around!", "You will be able to walk around the room. ")
Search = Action("Searching for possible objects! ", "You will be able to search the room. ")
Inv = Action("These are your current inventories. ", "If you do not see anything in it, that is because you have not collected anything yet. ")
Quit = Action("Thank you for playing. Bye!! ", "The game will stop. ")