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

def parser(moves):
    print("These are the parsed moves of the pokemon:")
    for i in range(moves):
        currentString = ""
        if moves[i] != ' ':
            print("what")
            
    

# You can only access api through these two lines. Treat this as the main function.
async def main() -> None:
    async with aiopoke.AiopokeClient() as client:
        search = 'pikachu'
        pokemon = await client.get_pokemon(search)
        # ability = await client.get_ability(search)
        # ability = await client.get_berry_firmness("chesto")
        # print(ability)
        print("Pokemon: " + pokemon.name)
        print("Pokemon moves: ")
        print(pokemon.moves)
        parser(pokemon.moves)
        
        

asyncio.run(main())