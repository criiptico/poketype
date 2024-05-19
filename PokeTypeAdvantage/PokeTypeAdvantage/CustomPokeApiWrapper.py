from functools import lru_cache
import requests
from typing import Optional
from pydantic import BaseModel

"""Move Object Pydantic Models"""

@lru_cache(maxsize=100)
def get_move(name_or_id: str | int):
    """Summary of get_move(name_or_id: str | int)
            Requests and returns a move from pokeapi to populate a Move object to return.    
    
        Args:
            name_or_id: Input a name or id of a move.
        Returns:
            A populated Move object that was populated from the name_or_id pokeapi request.
    """
    url = "https://pokeapi.co/api/v2/move/{endpoint}".format(endpoint = name_or_id)
    fetched_data = requests.get(url)

    if fetched_data.status_code == 200:
        data = fetched_data.json()
        return MoveApi(**data)
    raise ValueError("Invalid Move Endpoint.", url, name_or_id)

class _MoveType(BaseModel):
    name: str
    url: str

class MoveApi(BaseModel):
    id: int
    name: str
    power: Optional[int] # Move can be a status effect.
    type: _MoveType

    def get_name(self):
        """Summary of get_name()
        
            Returns:
                The name of the loaded move.
        """
        return self.name

    def get_id(self):
        """Summary of get_id()
        
            Returns:
                The id of the loaded move.
        """
        return self.id

    def get_power(self):
        """Summary of get_power()
        
            Returns:
                The power of the loaded move.
        """
        return self.power

    def get_type(self):
        """Summary of get_type()
        
            Returns:
                The name of the type of the loaded move.
        """
        return self.type.name
    


"""Pokemon Object Pydantic Models"""

@lru_cache(maxsize=50)
def get_pokemon(name_or_id: str | int):
    """Summary of get_pokemon(name_or_id: str | int)
            Requests and returns a pokemon from pokeapi to populate a Pokemon object to return.    
    
        Args:
            name_or_id: Input a name or id of a pokemon.
        Returns:
            A populated Pokemon object that was populated from the name_or_id pokeapi request.
    """
    url = "https://pokeapi.co/api/v2/pokemon/{endpoint}".format(endpoint = name_or_id)
    fetched_data = requests.get(url)
    
    if fetched_data.status_code == 200:
        data = fetched_data.json()
        return PokemonApi(**data)
    raise ValueError("Invalid Pokemon Endpoint.", url, name_or_id)


class _PokemonMove(BaseModel):
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

class _PokemonMoveDetails(BaseModel):
    move: _PokemonMove

class _PokemonType(BaseModel):
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

class _PokemonTypeDetails(BaseModel):
    type: _PokemonType

class PokemonApi(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    moves: list[_PokemonMoveDetails]
    types: list[_PokemonTypeDetails]
    sprites: dict

    def get_sprites(self):
        """Summary of get_sprites():
        
        Returns:
            dict[str]: The url of this pokemon's sprite on the PokeAPI
        """
        return self.sprites

    def get_name(self):
        """Summary of get_name():

        Returns: 
            str: The name of the loaded pokemon.
        """
        return self.name

    def get_id(self):
        """Summary of get_id():

        Returns: 
            int: The id of the loaded pokemon.
        """
        return self.id

    """Move functions for the loaded pokemon."""

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
        """Summary of get_moves():

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
    
    def get_types(self):
        """Summary of get_types():

        Returns:
            list[list]: A nested list of type names and ids of a pokemon in this format: [['id', 'name'], . . .]
        """
        type_list = list(list())

        for type in self.types:
            temp_list = list()
            temp_list.append(type.type.get_type_id())
            temp_list.append(type.type.get_type_name())
            type_list.append(temp_list)
        return type_list


## Testing

# pokemon = get_pokemon("pikachu")

# print(pokemon.get_name())
# print(pokemon.get_id())
# print(pokemon.get_moves())
# print(pokemon.get_move_ids())
# print(pokemon.get_move_names())
# print(pokemon.get_type_names())
# print(pokemon.get_type_ids())
# print(pokemon.get_types())
# print(pokemon.model_dump_json())

# pokemon_move = get_move(pokemon.get_move_ids()[0])
# print(pokemon_move.get_name())
# print(pokemon_move.get_id())
# print(pokemon_move.get_type())
# print(pokemon_move.get_power())
# print(pokemon_move.model_dump_json())

