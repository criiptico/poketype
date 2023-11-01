from Pokemon import Pokemon
import aiopoke
from Move import Move

class Load_Pokemon_Data: # Loads all pokemon data. Pokemon type, name (pokemon & moves), and ids (pokemon & moves)
    # move_ids = []
    def __get_move_ids(self, pokemon_data): # returns all the move ids, the moves, that a pokemon can do 
        move_string = str(pokemon_data.moves)
        return self.__api_delim(move_string, "move=MinimalResource(id=", ',')

    def __load_pokemon_types(self, pokemon, pokemon_data): # returns all the pokemon types that a pokemon is
        type_string = str(pokemon_data.types)
        pokemon.types = self.__api_delim(type_string, "name='", "'")

    async def __load_moves(self, pokemon: Pokemon, pokemon_data):
        async with aiopoke.AiopokeClient() as client:
            moves_id = self.__get_move_ids(pokemon_data) # get the move ids first (returns a list)
            print(moves_id)
            # Use client to load the pokemon with its corresponding move_name, move_id, and move_power | Load it in the Pokemon type data member: moves = {}
            for move in moves_id:
                move_data = await client.get_move(int(move)) # API Wrapper Error on line 23
                new_move =  Move() # Imported Move class
                new_move.id = move
                new_move.name = move_data.name
                new_move.power = move_data.power
                new_move.type = move_data.type
                
                pokemon.moves[move_data.name] = new_move

                print(move_data.name)
                
    def __api_delim(self, to_search: str, to_find, up_to):
        to_return = []
        # to_search = str(to_search)
        it = to_search.find(to_find)

        while it != -1:
            to_build = ""
            for i in range(it + len(to_find), len(to_search)):
                if to_search[i] == up_to:
                    break
                to_build = "".join([to_build, to_search[i]])
            to_return.append(to_build)
            to_search = to_search.replace(to_find, "", 1)

            it = to_search.find(to_find)
        return to_return

    async def load_pokemon(self, pokemon: Pokemon, pokemon_data): # loads basic pokemon data and its moves
        self.__load_pokemon_types(pokemon, pokemon_data)
        await self.__load_moves(pokemon, pokemon_data)
