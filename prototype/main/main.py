# import time
import CustomPokeApiWrapper as PokeWrapper
from Load_Pokemon_Data import Load_Pokemon_Data
from Pokemon import Pokemon 
from Battle import Battle

def main():
    # Pokemon() is an custom imported class
    pokemon_1 = Pokemon()
    pokemon_2 = Pokemon()

    found = False
    while found == False:
        try:
            pokemon = input("Enter pokemon 1: ")
            pokemon = pokemon.lower()
            pokemon_1_data = PokeWrapper.get_pokemon(pokemon)
        except ValueError:
            print("Not a valid value.")
        else:
            found = True

    found = False
    while found == False:
        try:
            pokemon = input("Enter pokemon 2: ")
            pokemon = pokemon.lower()
            pokemon_2_data = PokeWrapper.get_pokemon(pokemon)
        except ValueError:
            print("Not a valid value.")
        else:
            found = True

    load_poke_data = Load_Pokemon_Data()
    load_poke_data.load_pokemon(pokemon_1, pokemon_1_data)
    load_poke_data.load_pokemon(pokemon_2, pokemon_2_data)

    pokemon_battle = Battle(pokemon_1, pokemon_2)
    pokemon_battle.eval_efficacy()
    pokemon_battle.dump_effective_moves()

    # print(pokemon_battle.get_effective_moves_against_pokemon_1().items())
    # print(pokemon_battle.get_effective_moves_against_pokemon_2().items())

if __name__ == "__main__":
    main()


