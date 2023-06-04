# print("Hello World!")


# Test code provided by AioPokeApi at https://beastmatser.github.io/aiopoke/
# Running this code to test how it works.

import asyncio
import aiopoke
import json

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
    

# The input should be everything after PokemonMove and up to the next PokemonMove or a \n
def loadMoves(pokemon, moves, moveSet): # What data type is moves??? Is moves a list?
    count = 0
    for i in moves: 
        currentMove = str(i)
        moveIt = str(i).find(',')
        findMoves(str(i), ',', 3)
        # print(str(i))

def findMoves(s, toFind, n):
    itFind = s.find(toFind)
    itName = s.find("name=") + 6
    i = 0
    for i in range(n):
        itFind = s.find(toFind, itFind + 1)
    print(s[itName:itFind - 2])

# You can only access api through these two lines. Treat this as the main function.
async def main() -> None:
    async with aiopoke.AiopokeClient() as client:
        moveSet = set()
        search = 'pikachu'
        pokemon = await client.get_pokemon(search)
        # ability = await client.get_ability(search)
        # ability = await client.get_berry_firmness("chesto")
        # print(ability)
        # json.loads(pokemon.moves)
        print("Pokemon: " + pokemon.name)
        print("Pokemon moves: ")
        loadMoves(pokemon.name, pokemon.moves, moveSet)

asyncio.run(main())