import Pokemon
import Move

class Battle: # Calculates efficacy data of two pokemon
    def __init__(self, poke_1: Pokemon, poke_2: Pokemon) -> None:
        self.pokemon_1 = poke_1
        self.pokemon_2 = poke_2
        self.against_pokemon_1 = {}
        self.against_pokemon_2 = {}
        self.type_matrix = [[]]

    def eval_efficacy(poke_1: Pokemon, poke_2: Pokemon): # Evaluates the move efficacies of both pokemon 
        return {}
    
    def pokemon_1_efficacy(): # Returns moves from pokemon 2 that pokemon 1 is weak against
        return {}
    
    def pokemon_2_efficacy(): # Returns moves from pokemon 1 that pokemon 2 is weak against 
        return {}
    
    def __superEffective(self, move_name: Move): # Used in eval_efficacy
        return int(move_name.Move.power * 2) # Make sure it returns an int

    def __notVeryEffective(self, move_name: Move):
        return int(move_name.Move.power/ 2) # Make sure it returns an int
    
    def __notEffective(self, move_name: Move):
        return 0
    
    def load_type_chart(self, file_name: str): #  Parses file_name and loads it into type_matrix
        return
