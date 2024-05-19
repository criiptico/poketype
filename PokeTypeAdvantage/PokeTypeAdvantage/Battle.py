from Pokemon import Pokemon
import os
# from main.Move import Move

class Battle: # Calculates efficacy data of two pokemon
    def __init__(self, pokemon_1: Pokemon, pokemon_2: Pokemon) -> None:
        """Summary of __init__()
                Houskeeping procedures with pokemon_1 and pokemon_2 initializations and parsing of the type_chart.
            Args:
                pokemon_1: Pokemon to evaluate against pokemon_2.
                pokemon_2: Pokemon to evaluate against pokemon_1.
        """
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.effective_against_pokemon_1 = dict(list())  # Format: dict(list()) -> [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]]
        self.effective_against_pokemon_2 = dict(list())  # Format: dict(list()) -> [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]]
        self.type_chart = dict() # Format: [attacking_type] = ([defending_type] = efficacy_multiplier)
        
        base_dir = os.path.dirname(os.path.abspath(__file__)) # Sets the path of the current file
        file_path = os.path.join(base_dir, 'resources/single_type_chart.txt') # Sets file_path in addition to base_dir
        self.__parse_type_chart(file_path)
        # self.__parse_type_chart("../resources/single_type_chart.txt") # In the original code.

    def get_effective_moves_against_pokemon_1(self):
        """Summary of get_efffective_moves_against_pokemon_1():
                Note: Must execute after eval_efficacy()
            Returns:
                The effective moves from pokemon_2 that are effective against pokemon_1.
                In the format: dict(list()): [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]] 
        """
        return self.effective_against_pokemon_1
    
    def get_effective_moves_against_pokemon_2(self):
        """Summary of get_efffective_moves_against_pokemon_2():
                Note: Must execute after eval_efficacy()
            Returns:
                The effective moves from pokemon_1 that are effective against pokemon 2.
                In the format: dict(list()): [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]] 
        """        
        return self.effective_against_pokemon_2

    def eval_efficacy(self):
        """Summary of eval_efficacy():
                Evaluates the move efficacy of each pokemon and populates effective_against_pokemon_1 and
                effective_against_pokemon_2 in the format:
                dict(list()): [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]]
                Note: Must run before respective get functions.        
        """
        self.effective_against_pokemon_1 = self.__calc_efficacy(self.pokemon_2, self.pokemon_1)
        self.effective_against_pokemon_2 = self.__calc_efficacy(self.pokemon_1, self.pokemon_2)

    def dump_effective_moves(self):
        """Summary of dump_effective_moves():
                Prints the populated lists effective_against_pokemon_1 and effective_against_pokemon_2
                in a visually digestible manner. 
        """
        print("\n", self.pokemon_1.name, " is weak against. . .")
        for key in self.effective_against_pokemon_1.keys():
            print("Efficacy:", key)
            for move in self.effective_against_pokemon_1[key]:
                print(move.name, move.type, move.power)

        print("\n", self.pokemon_2.name, " is weak against. . .")
        for key in self.effective_against_pokemon_2.keys():
            print("Efficacy:", key)
            for move in self.effective_against_pokemon_2[key]:
                print(move.name, move.type, move.power)

    def __calc_efficacy(self, attacking_pokemon: Pokemon, defending_pokemon: Pokemon):
        """Summary of __calc_efficacy():
                Calculates a pair of pokemon's move efficacy depending if it's a single or double type pokemon.

            Args:
                attacking_pokemon: The pokemon who's attacking and whose moves should be evaluated
                against the defending_pokemon
                
                defending_pokemon: The pokemon who's defending against the attacking_pokemon's moves.
            
            Returns:
                A dict in the format: dict(list()): [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]]
        """
        # Pokemon of a single type
        if len(defending_pokemon.types) == 1:
            return self.__single_type(attacking_pokemon, defending_pokemon)
        # Pokemon of two types
        elif len(defending_pokemon.types) == 2:
            return self.__double_type(attacking_pokemon, defending_pokemon)
        else:
            raise ValueError("Error: Cannot calculate more than 2 types.")

    def __single_type(self, attacking_pokemon: Pokemon, defending_pokemon: Pokemon):
        """Summary of __single_type():
                Evaluates the effectiveness of the attacking_pokemon's moves against the defending_pokemon,
                then stores and returns them in the following format: 
                dict(list()): [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]]
            
            Args:
                attacking_pokemon: The pokemon who's attacking and whose moves should be evaluated
                against the defending_pokemon
                
                defending_pokemon: The pokemon who's defending against the attacking_pokemon's moves.

            Returns:
                A dict in the format: dict(list()): [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]]
        """

        efficacy_list = dict()
        efficacy_list[0] = list() # No effect
        efficacy_list[0.5] = list() # Note very effective
        efficacy_list[1] = list() # Normal effectiveness
        efficacy_list[2] = list() # Very effective

        for move in attacking_pokemon.moves.values():
            if move.power == 0 or move.power == None:
                efficacy_list[0].append(move)
                continue
            multiplier = self.type_chart[move.type][defending_pokemon.types[0]]
            efficacy_list[float(multiplier)].append(move)

        return efficacy_list

    def __double_type(self, attacking_pokemon: Pokemon, defending_pokemon: Pokemon):
        """Summary of __double_type():
                Evaluates the effectiveness of the attacking_pokemon's moves against the defending_pokemon, if 
                the defending pokemon is a double type pokemon. Then stores and returns them in the following format: 
                dict(list()): [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]]
            
            Args:
                attacking_pokemon: The pokemon who's attacking and whose moves should be evaluated
                against the defending_pokemon
                
                defending_pokemon: The pokemon who's defending against the attacking_pokemon's moves. This pokemon
                is a double type pokemon.

            Returns:
                A dict in the format: dict(list()): [[0] = [move_1, move_2, . . .], [0.5] = [. . .], [1] = [. . .], [2] = [. . .]]
        """
        efficacy_list = dict()
        efficacy_list[0] = list() # No effect
        efficacy_list[0.5] = list() # Not very effective
        efficacy_list[1] = list() # Normal effectiveness
        efficacy_list[2] = list() # Very effective

        for move in attacking_pokemon.moves.values():
            if move.power == 0 or move.power == None:
                efficacy_list[0].append(move)
                continue
            multiplier_1 = self.type_chart[move.type][defending_pokemon.types[0]]
            multiplier_2 = self.type_chart[move.type][defending_pokemon.types[1]]

            multiplier = multiplier_1 * multiplier_2
            if multiplier > 0.5 and multiplier <= 1:
                multiplier = 1
            elif multiplier > 0 and multiplier <= 0.5:
                multiplier = 0.5
            elif multiplier == 0:
                if multiplier_1 != 0 or multiplier_2 != 0:
                    if multiplier_1 != 0:
                        multiplier = multiplier_1
                    elif multiplier_2 != 0:
                        multiplier = multiplier_2
                else:
                    multiplier = 0
            elif multiplier > 1:
                multiplier = 2
                
            efficacy_list[float(multiplier)].append(move)

        return efficacy_list

    def __parse_type_chart(self, file_name: str): #  Parses file_name and loads it into type_matrix
        """Summary of __parse_type_chart():
                Parses single_type_chart.txt in ../resources/sinle_type_chart.txt and loads it onto a 
                matrix in the following format as a dict:
                type_chart[attacking_type][defending_type] = efficacy_multiplier
        """
        inFile = open(file_name, "r")

        next(inFile)
        for line in inFile:
            attacking_type = ""
            defending_type = ""
            efficacy_multiplier = 0.0
            
            temp = ""
            temp_int = 0
            for letter in line:
                if letter == ' ':
                    temp_int = temp_int + 1
                    if temp_int == 1:
                        attacking_type = temp.lower()
                        temp = ""
                    elif temp_int == 2:
                        defending_type = temp.lower()
                        temp = ""
                    continue
                elif letter == '\n':
                    efficacy_multiplier = float(temp)
                    break
                temp = "".join([temp, letter])
            
            # Load the data into the type chart
            if attacking_type not in self.type_chart:
                temp = dict()
                temp[defending_type] = efficacy_multiplier
                self.type_chart[attacking_type] = temp
            else:
                self.type_chart[attacking_type][defending_type] = efficacy_multiplier

        inFile.close()
