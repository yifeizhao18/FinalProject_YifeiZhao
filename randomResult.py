# Global Variables & Imports
import random
import message

# each result variable represents a result that the user might get
result1 = "You did not find anything here. "
result2 = "You found some energy drink. "
result3 = "You found a treasure chest with some bandages. "
result4 = "You found some apples. "
result5 = "You found a treasure chest with a flashlight in it. "
result6 = "You found a treasure chest with a knife in it. "
result7 = "You found a treasure chest with a sword in it. "
result8 = "You found a bottle of water. "


class Objects:
  """
  created a class for the inventory, food, medicine
  """
  def __init__ (objects):
    """
    empty inventories for the inventory, food, medicine
    """
    object.inventory = []
    object.food = []
    object.medicine = []


  def outcome(object):
    """
    it randomizes the result that the user might get
    """
    result = random.randint(0,15)
    # if it randomized a 0, do the following
    if result == 0:
      print(result1)
      print('\n')
    # if it randomized a 1, do the following
    elif result == 1:
      print(result4)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.food.append("apples")
          print(object.food)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 2, do the following
    elif result == 2:
      print(result6)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.inventory.append("knife")
          print(object.inventory)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 3, do the following
    elif result == 3:
      print(result1)
      print('\n')
    # if it randomized a 4, do the following
    elif result == 4:
      print(result5)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.inventory.append("flashlight")
          print(object.inventory)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 5, do the following
    elif result == 5:
      print(result3)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.medicine.append("bandages")
          print(object.medicine)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 6, do the following
    elif result == 6:
      print(result7)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.inventory.append("sword")
          print(object.inventory)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 7, do the following
    elif result == 7:
      print(result1)
      print('\n')
    # if it randomized a 8, do the following
    elif result == 8:
      print(result2)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.food.append("energy drink")
          print(object.food)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 9, do the following
    elif result == 9:
      print(result5)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.inventory.append("flashlight")
          print(object.inventory)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 10, do the following
    elif result == 10:
      print(result8)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.food.append("water")
          print(object.food)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 11, do the following
    elif result == 11:
      print(result1)
      print('\n')
    # if it randomized a 12, do the following
    elif result == 12:
      print(result8)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.food.append("water")
          print(object.food)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    #if it randomized a 13, do the following
    elif result == 13:
      print(result6)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.inventory.append("knife")
          print(object.inventory)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 14, do the following
    elif result == 14:
      print(result4)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.food.append("apples")
          print(object.food)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')
    # if it randomized a 15, do th following
    elif result == 15:
      print(result3)
      print('\n')
      print(message.congrats)
      print('\n')
      while True:
        # asks if the user wants to collect it or not
        collect = input(message.coll)
        print('\n')
        if collect == "yes":
          object.medicine.append("bandages")
          print(object.medicine)
          print('\n')
          break
        elif collect == "no":
          print(message.answer)
          print('\n')
          break
        else:
          print(message.error)
          print('\n')