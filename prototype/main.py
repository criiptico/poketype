# print("Hello World!")


# Test code provided by AioPokeApi at https://beastmatser.github.io/aiopoke/
# Running this code to test how it works.

import asyncio
import aiopoke

# Below is test code
# async def main() -> None:
#     print("Hello world!")
#     async with aiopoke.AiopokeClient() as client:
#         berry = await client.get_berry(1)
#         print(berry)

#         # An object can also have 'MinimalResources' as attributes
#         # You can fetch those with .fetch(), for example:
#         # item = await berry.item.fetch() # This is the line that is making the program crash on line 22. I don't know what's wrong with this, but it doesn't work.
#         print(berry.item.name)
#         growth = berry.growth_time
#         print(growth)

# def parser(data, toFind):
#     for i in range(len(data)):
#         if data[i:i+11] == "PomemonMove":
            

# def moveLocator(pokemon, moves):
    

# The input should be everything after PokemonMove and up to the next PokemonMove or a \n
def moveLocator(pokemon, moves, moveSet): # What data type is moves??? Is moves a list?
    count = 0
    print("These are the parsed moves of the pokemon:")
    for i in moves: # In response to line 40, it seems that each PokemonMove string is an iterative string with respect to PokemonMove
        # currentString = ""
        print(str(i) + " times iterating through the string.")
        print("At " + str(moves[i]) + " right now.")
        if moves[i:i+11] == "PokemonMove": # new move found # Wait a minute, how is this working?
            # != changes the counter and == doesn't. So it isn't reading correctly?
            print("Move found.")
            count+=1
    print("Pokemon " + pokemon + " has " + str(count) + " possible move(s).")
            
    

# You can only access api through these two lines. Treat this as the main function.
async def main() -> None:
    async with aiopoke.AiopokeClient() as client:
        moveSet = set()
        search = 'pikachu'
        pokemon = await client.get_pokemon(search)
        # ability = await client.get_ability(search)
        # ability = await client.get_berry_firmness("chesto")
        # print(ability)
        print("Pokemon: " + pokemon.name)
        print("Pokemon moves: ")
        print(pokemon.moves)
        moveLocator(pokemon.name, pokemon.moves, moveSet)
        
        

asyncio.run(main())