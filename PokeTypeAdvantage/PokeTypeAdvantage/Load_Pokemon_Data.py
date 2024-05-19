import logging
import CustomPokeApiWrapper as PokeWrapper
from CustomPokeApiWrapper import PokemonApi
from Pokemon import Pokemon
from Move import Move

class Load_Pokemon_Data: # Loads all pokemon data. Pokemon type, name (pokemon & moves), and ids (pokemon & moves)

    def __load_pokemon_type_names(self, pokemon: Pokemon, pokemon_data: PokemonApi): # returns all the pokemon types that a pokemon is
        """Summary of __load_pokemon_type_names():
                Loads all type names of a pokemon from pokemon_data to pokemon.
            Args:
                pokemon: To load all type names into it.
                pokemon_data: To load all type names from it.
        """
        pokemon.types = pokemon_data.get_type_names()

    def __load_pokemon_moves(self, pokemon: Pokemon, pokemon_data: PokemonApi):
        """Summary of __load_pokemon_moves():
                Loads all move data from pokemon_data onto pokemon.
            Args:
                pokemon: To load all move data into it.
                pokemon_data: To load all move data from it.
        """
        move_ids = pokemon_data.get_move_ids()

        for move in move_ids:
            try:
                move_data = PokeWrapper.get_move(int(move))
                new_move =  Move() # Imported Move class to keep the PokeWrapper and the main application separated
                new_move.id = move_data.get_id()
                new_move.name = move_data.get_name()
                new_move.power = move_data.get_power()
                new_move.type = move_data.get_type()

            except TypeError:
                print("\tAn Error Occured with " + move)
                log = logging.getLogger()
                log.exception("An Error Occured with " + move)

            pokemon.moves[move_data.id] = new_move

    # def __api_delim(self, to_search: str, to_find, up_to):
    #     to_return = []
    #     # to_search = str(to_search)
    #     it = to_search.find(to_find)

    #     while it != -1:
    #         to_build = ""
    #         for i in range(it + len(to_find), len(to_search)):
    #             if to_search[i] == up_to:
    #                 break
    #             to_build = "".join([to_build, to_search[i]])
    #         to_return.append(to_build)
    #         to_search = to_search.replace(to_find, "", 1)

    #         it = to_search.find(to_find)
    #     return to_return

    def load_pokemon(self, pokemon: Pokemon, pokemon_data: PokemonApi): # loads basic pokemon data and its moves
        """Summary of load_pokemon()
                Loads pokemon data from pokemon_data and PokeWrapper onto pokemon.
            
            Args:
                pokemon: Input a non-api Pokemon class.
                pokemon_data: Input an api Pokemon class from PokeWrapper.
        """
        pokemon.name = pokemon_data.get_name()
        pokemon.sprites = pokemon_data.get_sprites()
        self.__load_pokemon_type_names(pokemon, pokemon_data)
        self.__load_pokemon_moves(pokemon, pokemon_data)
