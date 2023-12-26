import requests
from pydantic import BaseModel

"""Move Object Pydantic Models"""

def get_move(name_or_id: str | int):
    """Summary of get_move(name_or_id: str | int)
        Requests and returns a move from pokeapi and populates a Move object to return.    
    
        Args:
            name_or_id: str | int: Input a name or id of a move.
        Returns:
            A populated Move object that was populated from the name_or_id pokeapi request.
    """
    url = "https://pokeapi.co/api/v2/move/{endpoint}".format(endpoint=name_or_id)
    data = requests.get(url).json()
    return Move(**data)

class MoveType(BaseModel):
    name: str
    url: str

class Move(BaseModel):
    id: int
    name: str
    power: int
    type: MoveType


"""Pokemon Object Pydantic Models"""

def get_pokemon(name_or_id: str | int):
    """Summary of get_pokemon(name_or_id: str | int)
        Requests and returns a pokemon from pokeapi and populates a Pokemon object to return.    
    
        Args:
            name_or_id: str | int: Input a name or id of a pokemon.
        Returns:
            A populated Pokemon object that was populated from the name_or_id pokeapi request.
    """
    url = "https://pokeapi.co/api/v2/pokemon/{endpoint}".format(endpoint = name_or_id)
    data = requests.get(url).json()
    return Pokemon(**data)

class PokemonMove(BaseModel):
    name: str
    url: str

    def get_move_id(self):
        """Summary of get_move_id()

            Returns:
                str: The id of the current move.
        """
        return self.url.rstrip("/").split("/")[-1]
    
    def get_move_name(self):
        """Summary of get_move_name()

            Returns:
                str: The name of the current move.
        """
        return self.name
    
    def get_move_url(self):
        """Summary of get_move_url()
            Returns:
                str: The url of the current move.
        """
        return self.url

class PokemonMoveDetails(BaseModel):
    move: PokemonMove

class PokemonType(BaseModel):
    name: str
    url: str

    def get_type_name(self):
        """Summary of get_type_name()

            Returns:
                str: The name of the current type.
        """
        return self.name

    def get_type_url(self):
        """Summary of get_type_url()

            Returns:
                str: The url of the current type.
        """
        return self.url

    def get_type_id(self):
        """Summary of get_type_id()

            Returns:
                str: The id of the current type.
        """
        return self.url.rstrip("/").split("/")[-1]

class PokemonTypeDetails(BaseModel):
    type: PokemonType

class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    moves: list[PokemonMoveDetails]
    types: list[PokemonTypeDetails]

    """Move functions for the loaded pokemon."""

    def get_id(self):
        """Summary of get_id():

        Returns: 
            int: The id of the pokemon.
        """
        return self.id

    def get_move_ids(self):
        """Summary of get_move_ids():

        Returns:
            list: A list of move ids of a pokemon.
        """
        move_ids = list()
        for move in self.moves:
            move_ids.append(move.move.get_move_id())
        return move_ids
    
    def get_move_names(self):
        """Summary of get_move_names():

        Returns:
            list: A list of move names of a pokemon.
        """
        move_names = list()
        for move in self.moves:
            move_names.append(move.move.get_move_name())
        return move_names
        
    def get_moves(self):
        """Summary of get_move_names():

        Returns:
            list[list]: A nested list of move names and ids of a pokemon in this format: [['id', 'name'], . . .]
        """
        move_list = list(list())

        for move in self.moves:
            temp_list = list()
            temp_list.append(move.move.get_move_id())
            temp_list.append(move.move.get_move_name())
            move_list.append(temp_list)
        return move_list
    
    """Type functions for the loaded pokemon."""

    def get_type_names(self):
        """Summary of get_type_names():

        Returns:
            list: A list of type names of a pokemon.
        """
        type_names = list()
        for type in self.types:
            type_names.append(type.type.get_type_name())
        return type_names
    
    def get_type_ids(self):
        """Summary of get_type_ids():

        Returns:
            list: A list of type ids of a pokemon.
        """
        type_ids = list()
        for type in self.types:
            type_ids.append(type.type.get_type_id())
        return type_ids

