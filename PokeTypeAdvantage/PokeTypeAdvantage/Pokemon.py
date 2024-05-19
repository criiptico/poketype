from Move import Move

class Pokemon: # Data structur for the standard info of a pokemon. Includes the name, id, type(s), and moves (move name & move id) a pokemon has
    def __init__(self):
        self.name = ""
        self.id = 0
        self.moves = dict() # Map of moves. [id] = move_object
        self.types = list() # The type(s) the pokemon is
        self.sprites = dict() # URL of sprites