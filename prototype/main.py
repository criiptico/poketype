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
    

# The input should be everything after PokemonMove and up to the next PokemonMove or a \n
def loadMoves(pokemon, moves, moveMap): # What data type is moves??? Is moves a list?
    count = 0
    for i in moves: 
        currentMove = str(i)
        moveIt = str(i).find(',')
        findMoves(str(i), ',', 3, moveMap)
        # print(str(i))
    return moveMap


def findMoves(s, toFind, n, moveMap):
    itFind = s.find(toFind)
    itName = s.find("name=") + 6
    # moveMap = {}
    i = 0
    for i in range(n):
        itFind = s.find(toFind, itFind + 1)
    moveName = s[itName:itFind - 2]
    moveMap[findId(s)] = moveName
    # print(s[itName:itFind - 2])
    # moveSet[] = moveName
    return moveMap

def findId(s):
    itFind = s.find(',')
    itId = s.find("id=")
    i = 0
    for i in range(1):
        itFind = s.find(',', itFind + 1)
    moveId = s[itId + 3:itFind]
    # print(moveId)
    return moveId

def dumpMoves(pokeName, moves):
    print(pokeName, "has", str(len(moves)), "moves.")
    print("ID:", "Name:")
    for key in moves:
        print(key, "->", moves[key])



# You can only access api through these two lines. Treat this as the main function.
async def main() -> None:
    async with aiopoke.AiopokeClient() as client:
        pokemonOneMoves = {}
        pokemonTwoMoves = {}
        # search = 'pikachu'
        # pokemon = await client.get_pokemon(search)
        # ability = await client.get_ability(search)
        # ability = await client.get_berry_firmness("chesto")
        # print(ability)
        # json.loads(pokemon.moves)
        opponentOne = input("Enter pokemon 1: ")
        opponentTwo  = input("Enter pokemon 2: ")
        opponentOne = opponentOne.lower()
        opponentTwo = opponentTwo.lower()

        pokemonOne = await client.get_pokemon(opponentOne)
        pokemonTwo = await client.get_pokemon(opponentTwo)        

        loadMoves(pokemonOne.name, pokemonOne.moves, pokemonOneMoves)
        loadMoves(pokemonTwo.name, pokemonTwo.moves, pokemonTwoMoves)


        # Search moves' base damage | Make another dict with the id and the move's base damage?
        # Develop type chart matrix, function, and txt file to read from.
        # Search moves on type chart in comparison against opposing pokemon.
            # sort move effectiveness in a max and min heap for each pokemon. (2 min and 2 max)
        
        print("Pokemon 1: " + pokemonOne.name)
        print("Pokemon 1 moves: ")
        dumpMoves(pokemonOne.name, pokemonOneMoves)
        
        print("Pokemon 2: " + pokemonTwo.name)
        print("Pokemon 2 moves: ")
        dumpMoves(pokemonTwo.name, pokemonTwoMoves)

        
    
asyncio.run(main())