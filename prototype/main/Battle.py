from Pokemon import Pokemon
from Move import Move

class Battle: # Calculates efficacy data of two pokemon
    def __init__(self, poke_1: Pokemon, poke_2: Pokemon) -> None:
        self.pokemon_1 = poke_1
        self.pokemon_2 = poke_2
        self.effective_against_pokemon_1 = {} # Pokemon 2 moves that are effective against pokemon 2
        self.effective_against_pokemon_2 = {} # Pokemon 1 moves that are effective against pokemon 1
        # Use either a nested list or a nested map for the type matrix.
        self.type_chart = dict(dict()) # Format: [attacking_type] = ([defending_type] = efficacy_multiplier)
        # self.type_matrix = [[]] # Use nested or dict(list()) if dict(dict()) doesn't work.
        self.__load_type_chart("../resources/some_file_name")

    def eval_efficacy(poke_1: Pokemon, poke_2: Pokemon): # Evaluates the move efficacies of both pokemon 
        # Use super/not-very/not effective functions here.
        return {}
    
    def pokemon_1_efficacy(): # Returns moves from pokemon 2 that pokemon 1 is weak against
        # Calculates something based in the type chart, returns the dict.
        return {}
    
    def pokemon_2_efficacy(): # Returns moves from pokemon 1 that pokemon 2 is weak against 
        # Calculates something based in the type chart, returns the dict.
        return {}
    
    def __super_effective(self, move_name: Move): # Used in eval_efficacy
        return int(move_name.Move.power * 2) # Make sure it returns an int

    def __not_very_effective(self, move_name: Move):
        return int(move_name.Move.power / 2) # Make sure it returns an int
    
    def __not_effective(self, move_name: Move):
        return 0
    
    def __load_type_chart(self, file_name: str): #  Parses file_name and loads it into type_matrix
        return
