import random 
import sys
from randomResult import *


class EnemyMessage: 
  """
  """
  def __init__ (self, description, message):
    """
    """
    self.description = description
    self.message = message


  def enemyDescription(self):
    """
    """
    print(self.description)
    print('\n')
    print(self.message)
    print('\n')


# create enemy objects
zombie = EnemyMessage("THE ZOMBIES ARE HEADING THIS WAY!! THEY ARE NOT THAT HARD TO FIGHT WITH. ", "USE YOUR KNIFE OR YOUR SWORD TO KILL THEM!! IF YOU HAVE A KNIFE, USE IT. SWORD IS MORE VALUABLE. ")
boss = EnemyMessage("THESE IS THE HARDEST TYPE OF ENEMY TO FIGHT WITH. THEY ARE THE BOSS. ", "YOU CAN ONLY USE YOUR SWORD TO KILL THEM. GOOD LUCKKKK!!!! ")

result1 = zombie.enemyDescription()
result2 = boss.enemyDescription()

Battle = Objects()

  
class Enemy: 
  """
  """
  def __init__ (choice):
    """
    """
    choice.choice = choice


  def enemyChoice(choice):
    """
    """
    result = random.randint(0, 2)
    if result == 0:
      print(result1)
      print('\n')
      print("Inventories: ")
      for item in Battle.inventory:
        print(f"a {item}")
        print('\n')
      fight = input(message.knife)
      if fight == "yes":
        if Battle.inventory == "knife":
          object.inventory.delete("knife")
        elif Battle.inventory ==? "knife":
          print("There is no knife in your inventory. Sorry!! You just got killed by the enemy. Bye!! ")
          sys.exit()