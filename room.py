class Rooms:
  """
  create a class for the rooms in th hospital
  """
  def __init__ (tile, description):
    tile.description = description
    
class Tile(Rooms):
  def __init__ (tile, description, passage):
    super(Tile, tile).__init__(description)
    tile.passage = passage