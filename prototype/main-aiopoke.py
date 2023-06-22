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

#         pokemon = await client.get_pokemon('pikachu')
#         print(pokemon.name)


def loadMoves(pokemon, moves, moveMap):
    count = 0
    for i in moves: 
        currentMove = str(i)
        moveIt = str(i).find(',')
        findMoves(str(i), ',', 3, moveMap)
    return moveMap

def findMoves(s, toFind, n, moveMap):
    itFind = s.find(toFind)
    itName = s.find("name=") + 6
    i = 0

    for i in range(n):
        itFind = s.find(toFind, itFind + 1)
    moveName = s[itName:itFind - 2]
    moveMap[findId(s)] = moveName

    return moveMap

def findId(s):
    itFind = s.find(',')
    itId = s.find("id=")
    i = 0

    for i in range(1):
        itFind = s.find(',', itFind + 1)
    moveId = s[itId + 3:itFind]
    return moveId

def dumpMoves(pokeName, moves):
    print(pokeName, "has", str(len(moves)), "moves.")
    print("ID:", "Name:")
    for key in moves:
        print(key, "->", moves[key])

async def loadBaseDamage(pokemon, moves):
    async with aiopoke.AiopokeClient() as client:
        print("Displaying the damage of each move: ")
        for move in moves.keys():
            moveData = await client.get_move(move)
            print(pokemon.name, ":", move, "->", moveData.power)
            

# You can only access api through these two lines. Treat this as the main function.
async def main():
    async with aiopoke.AiopokeClient() as client:
        # Available moves each opponent has
        opponentOneMoves = {}
        opponentTwoMoves = {}
        
        # Store the base damage of each move for both opponents
        baseOne = {}
        baseTwo = {}
        

        pokemonOne = input("Enter pokemon 1: ")
        pokemonTwo  = input("Enter pokemon 2: ")
        pokemonOne = pokemonOne.lower()
        pokemonTwo = pokemonTwo.lower()

        opponentOne = await client.get_pokemon(pokemonOne)
        loadMoves(opponentOne.name, opponentOne.moves, opponentOneMoves)

        opponentTwo = await client.get_pokemon(pokemonTwo)
        loadMoves(opponentTwo.name, opponentTwo.moves, opponentTwoMoves)

        await loadBaseDamage(opponentOne, opponentOneMoves)
        await loadBaseDamage(opponentTwo, opponentTwoMoves)


        # Note: Make a min and max heap for each pokemon with respect to their opposing pokemon
        ## The idea is to make a min and max of moves that are most effective for each pokemon
        ## against the pokemon they're against.
        oneMin = [None] * len(opponentOneMoves)
        oneMax = [None] * len(opponentOneMoves)
        twoMin = [None] * len(opponentTwoMoves)
        twoMax = [None] * len(opponentTwoMoves)


        # Search moves' base damage | Make another dict with the id and the move's base damage?
        # Develop type chart matrix, function, and txt file to read from.
        # Search moves on type chart in comparison against opposing pokemon.
            # sort move effectiveness in a max and min heap for each pokemon. (2 min and 2 max)
        
        print("Pokemon 1: " + opponentOne.name)
        print("Pokemon 1 moves: ")
        dumpMoves(opponentOne.name, opponentOneMoves)
        print()
        
        print("Pokemon 2: " + opponentTwo.name)
        print("Pokemon 2 moves: ")
        dumpMoves(opponentTwo.name, opponentTwoMoves)

        
    
asyncio.run(main())