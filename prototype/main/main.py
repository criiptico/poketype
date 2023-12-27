import time
import CustomPokeApiWrapper as PokeWrapper
from Load_Pokemon_Data import Load_Pokemon_Data
from Pokemon import Pokemon 
from Move import Move # I'm not sure if I need it.
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
    st = time.time()
    load_poke_data.load_pokemon(pokemon_1, pokemon_1_data)
    et = time.time()
    print("Pokemon 1 load_pokemon runtime: ", et - st)

    st = time.time()
    load_poke_data.load_pokemon(pokemon_2, pokemon_2_data)
    et = time.time()
    print("Pokemon2 load_pokemon runtime: ", et - st)

    print("Pokemon 1:", pokemon_1.name, "\tPokemon 2:", pokemon_2.name)  

    # pokemon_battle = Battle(pokemon_1, pokemon_2) # Executes after loading pokemon data is complete


if __name__ == "__main__":
    main()


