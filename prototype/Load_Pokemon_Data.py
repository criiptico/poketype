import Pokemon
import aiopoke

class Load_Pokemon_Data: # Loads all pokemon data. Pokemon type, name (pokemon & moves), and ids (pokemon & moves)
    # move_ids = []
    def __get_move_ids(self, pokemon, pokemon_data): # returns all the move ids, the moves, that a pokemon can do 
        move_id = [] # Get the move ids
        # Find PokemonMove, then name=', then get data, repeat
        move_string = pokemon_data.types
        while move_string.find("PokemonMove") != -1:
            it = move_string.find("PokemonMove")
            # self.del
        # PARSE pokemon data
        return move_id 

    def __load_pokemon_types(self, pokemon, pokemon_data): # returns all the pokemon types that a pokemon is
        # get pokemon types by PARSING pokemon data.
        type_string = pokemon_data.types
        types = self.__delim_2(type_string, "name='", "'", "PokemonMove")

    async def __load_moves(self, pokemon: Pokemon, pokemon_data): # retuns nothing
        async with aiopoke.AiopokeClient() as client:
            moves_id = self.get_move_ids(pokemon, pokemon_data) # get the move ids first
            # USE client to load the pokemon with its corresponding move_name, move_id, and move_power | Load it in the Pokemon type data member: moves = {}
        return
    
    def __delim_2(self, to_search: str, to_find, end_char, start_sub_string): # Need to finish this delim
        to_return = []
        n = 0
        end = len(to_search)

        while to_search.find(start_sub_string, n) != -1:
            n = n + to_search.find(start_sub_string, n)
            p = 
            temp_string = ""
            i = n + 1
            



        return
    
    def __delim_1(self, to_search: str, to_find, to_index, end_char): # to_index is the value it takes to get to the desired information
        to_return = []
        n = 0
        end = len(to_search)
        
        # Find some value
        while to_search.find(to_find, n) != -1:
            n = to_search.find(to_find, n) + to_index
            temp_string = ""
            i = n + 1
            # Concactenate from i to end_char
            for i in range(end):
                if to_search[i] == end_char:
                    break
                temp_string = temp_string + to_search[i]
            to_return.append(temp_string)    
        return to_return

    def load_pokemon(self, pokemon: Pokemon, pokemon_data): # loads basic pokemon data and its moves
        self.__load_pokemon_types(pokemon, pokemon_data)
        # self.__get_move_ids(pokemon)
        self.__load_moves(pokemon, pokemon_data)

        return # loads pokemon data and pokemon names