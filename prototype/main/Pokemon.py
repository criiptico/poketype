class Pokemon: # Data structur for the standard info of a pokemon. Includes the name, id, type(s), and moves (move name & move id) a pokemon has
    name = ""
    id = 0
    moves = dict() # Map of moves. [id] = move_object
    types = [] # The type(s) the pokemon is