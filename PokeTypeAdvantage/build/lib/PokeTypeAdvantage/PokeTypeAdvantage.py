import main.CustomPokeApiWrapper as PokeWrapper
from main.Load_Pokemon_Data import Load_Pokemon_Data
from main.Pokemon import Pokemon 
from main.Battle import Battle

def get_pokemon(pokemon: str):
    try:
        pokemon = pokemon.lower()
        pokemon_data = PokeWrapper.get_pokemon(pokemon)
        # print("The address to this pokemon's front-default image is", {pokemon_data.sprites["front_default"]})
    except ValueError:
        raise ValueError
    return pokemon_data

def eval_pokemon(pokemon1: str, pokemon2: str):
    # Pokemon() is an custom imported class
    pokemon_1 = Pokemon()
    pokemon_2 = Pokemon()

    found = False
    while found == False:
        try:
            pokemon = pokemon1
            pokemon = pokemon.lower()
            pokemon_1_data = PokeWrapper.get_pokemon(pokemon)
        except ValueError:
            print("Not a valid value.") # Need to deal with this error in the front end.
            raise ValueError
        else:
            found = True

    found = False
    while found == False:
        try:
            pokemon = pokemon2
            pokemon = pokemon.lower()
            pokemon_2_data = PokeWrapper.get_pokemon(pokemon)
        except ValueError:
            print("Not a valid value.") # Need to deal with this error in the front end.
            raise ValueError
        else:
            found = True

    load_poke_data = Load_Pokemon_Data()
    load_poke_data.load_pokemon(pokemon_1, pokemon_1_data)
    load_poke_data.load_pokemon(pokemon_2, pokemon_2_data)

    pokemon_battle = Battle(pokemon_1, pokemon_2)
    pokemon_battle.eval_efficacy()

    to_return = list()
    # Need to send pokemon1 data [0]
    to_return.append(pokemon_battle.get_effective_moves_against_pokemon_1())
    # Need to send pokemon2 data [1]
    to_return.append(pokemon_battle.get_effective_moves_against_pokemon_2())

    return to_return # Returning list(dict(list()), dict(list()))


# def main():
#     # Pokemon() is an custom imported class
#     pokemon_1 = Pokemon()
#     pokemon_2 = Pokemon()

#     found = False
#     while found == False:
#         try:
#             pokemon = input("Enter pokemon 1: ")
#             pokemon = pokemon.lower()
#             pokemon_1_data = PokeWrapper.get_pokemon(pokemon)
#         except ValueError:
#             print("Not a valid value.")
#         else:
#             found = True

#     found = False
#     while found == False:
#         try:
#             pokemon = input("Enter pokemon 2: ")
#             pokemon = pokemon.lower()
#             pokemon_2_data = PokeWrapper.get_pokemon(pokemon)
#         except ValueError:
#             print("Not a valid value.")
#         else:
#             found = True

#     load_poke_data = Load_Pokemon_Data()
#     load_poke_data.load_pokemon(pokemon_1, pokemon_1_data)
#     load_poke_data.load_pokemon(pokemon_2, pokemon_2_data)

#     pokemon_battle = Battle(pokemon_1, pokemon_2)
#     pokemon_battle.eval_efficacy()
#     pokemon_battle.dump_effective_moves()

#     # print(pokemon_battle.get_effective_moves_against_pokemon_1().items())
#     # print(pokemon_battle.get_effective_moves_against_pokemon_2().items())

# if __name__ == "__main__":
#     main()


