import requests
from pydantic import BaseModel

# class PokemonAbility(BaseModel):
#     name: str
#     url: str

# class PokemonAbilityDetails(BaseModel):
#     ability: PokemonAbility
#     is_hidden: bool
#     slot: int

class PokemonMove(BaseModel):
    name: str
    url: str

    def get_move_id(self):
        return self.url.rstrip("/").split("/")[-1]
    
    def get_move_name(self):
        return self.name
    
    def get_move_url(self):
        return self.url

class PokemonMoveDetails(BaseModel):
    move: PokemonMove

class Pokemon(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    moves: list[PokemonMoveDetails] 
    # abilities: list[PokemonAbilityDetails] # Commented out because I don't use it.

    def get_id(self):
        return self.id

    def get_move_ids(self):
        move_ids = list()
        for move in self.moves:
            move_ids.append(move.move.get_move_id())
        return move_ids

    def get_move_names(self):
        move_names = list()
        for move in self.moves:
            move_names.append(move.move.get_move_name())
        return move_names
    
    def get_moves(self):
        move_list = list(list())

        for move in self.moves:
            temp_list = list()
            temp_list.append(move.move.get_move_id())
            temp_list.append(move.move.get_move_name())
            move_list.append(temp_list)
        return move_list

class MoveType(BaseModel):
    move: str
    url: str

class MoveTypesDetails(BaseModel):
    typeList: MoveType

class Move(BaseModel):
    id: int
    name: str
    power: int
    type: list[MoveTypesDetails]


# ditto_url = "https://pokeapi.co/api/v2/pokemon/ditto"
# pikachu_url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# api_data = requests.get(ditto_url)
# data_ditto = api_data.json()

# pokemon_model = Pokemon(**data_ditto)

# print("Ditto")
# print(pokemon_model.model_dump_json(indent=2)) # Used for testing

# print(pokemon_model.get_move_ids())
# print(pokemon_model.get_move_names())
# print(pokemon_model.get_moves())

# api_data = requests.get(pikachu_url)
# data_pikachu = api_data.json()
# pokemon_model = Pokemon(**data_pikachu)

# print("Pikachu")
# print(pokemon_model.get_move_ids())
# print(pokemon_model.get_move_names())
# print(pokemon_model.get_moves())

# print(pokemon_model.model_dump_json())

pound_url = "https://pokeapi.co/api/v2/move/pound"
api_data = requests.get(pound_url)
data_pound = api_data.json()

move_model = Move(**data_pound)
print("Pound")
print(move_model.model_dump_json(indent=2))


