# Imported Libraries

import asyncio
import aiopoke

# import pdb

# Imported Classes
# import Move
from Pokemon import Pokemon
from Battle import Battle
from Load_Pokemon_Data import Load_Pokemon_Data

async def main():
    async with aiopoke.AiopokeClient() as client:
        # some_data =  await client.get_move(192)
        # print(some_data.name)
        pokemon_1 = Pokemon()
        pokemon_2 = Pokemon()

        found = False
        while found == False:
            try:
                pokemon = input("Enter pokemon 1: ")
                pokemon = pokemon.lower()
                pokemon_1.name = pokemon
                pokemon_1_data = await client.get_pokemon(pokemon)
            except ValueError:
                print("Not a valid value.")
            else:
                found = True

        found = False
        while found == False:
            try:
                pokemon = input("Enter pokemon 2: ")
                pokemon = pokemon.lower()
                pokemon_2.name = pokemon
                pokemon_2_data = await client.get_pokemon(pokemon)
            except ValueError:
                print("Not a valid value.")
            else:
                found = True


        print("Pokemon 1:", pokemon_1_data.name, "\tPokemon 2:", pokemon_2_data.name)
        
        load_poke_data = Load_Pokemon_Data()
        await load_poke_data.load_pokemon(pokemon_1, pokemon_1_data)
        await load_poke_data.load_pokemon(pokemon_2, pokemon_2_data)

        # pokemon_battle = Battle(pokemon_1, pokemon_2) # Executes after loading pokemon data is complete

        print("Pokemon 1 data:", pokemon_1_data.types)
        print("Pokemon 2 data:", pokemon_2_data.types)



    # await client.close()

asyncio.run(main())
