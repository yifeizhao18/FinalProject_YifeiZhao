class Rooms:
  """
  create a class for the rooms in th hospital
  """
  def __init__ (tile, description):
    """
    descriptions
    """
    tile.description = description
    
class Tile(Rooms):
  """
  created a child class under the class Rooms
  """
  def __init__ (tile, description, passage):
    """
    passage
    """
    super(Tile, tile).__init__(description)
    tile.passage = passage