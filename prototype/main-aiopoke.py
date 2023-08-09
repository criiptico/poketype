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


def loadMoves(pokemonMoves, moveMap):
    """
    Loads each move into a map, moveMap, in the format [id] = name

    Parameters
    ----------
    pokemonMoves : 
        An array of pokemon moves retrieved from aiopokeapi. Each index contains a long string of unparsed data.
    moveMap :
        A map to be populated with each move's id and name. Ex. [id] = name 
    """
    count = 0
    for i in pokemonMoves: 
        currentMove = str(i)
        moveIt = str(i).find(',')
        findMoves(str(i), moveMap)

    return moveMap

def findMoves(s, moveMap):
    """
    Finds all of the names and ids of a pokemon's moveset and adds them to the moveMap map.

    Parameters
    ----------
    s :
        A string of unparsed move data.
    moveMap :
        A map to be populated with each move's id ane name. Ex. [id] = name 
    """

    itNameBegin = s.find("name='") + 6
    itNameEnd = 0

    for i in range(0, len(s)): # In range of the whole single line string chars
        if s[itNameBegin + i] == ')': # Can also use find member function of a string
            itNameEnd = itNameBegin + i - 1
            break

    moveName = s[itNameBegin:itNameEnd]
    moveMap[findId(s)] = moveName
    return moveMap

def findId(s):
    """
    Finds the id from a string of unparsed move data.

    Parameters
    ----------
    s :
        A string of unparsed move data.
    """

    itIdBegin = s.find("id=") + 3
    itIdEnd = s.find(",")

    moveId = s[itIdBegin:itIdEnd]
    return moveId

# Used to find the type of a pokemon
def findType(pokemon):
    pokemonType = ""
    print(pokemon.name, " data.")
    print(pokemon.types)

    return pokemonType


def dumpMoves(pokeName, moves):
    """
    Dumps move name's and id's of pokemon.

    Parameters
    ----------
    pokeName :
        Name of pokemon.
    moves :
        Mapset of ids and moves of pokeName.
    """

    print(pokeName, "has", str(len(moves)), "moves.")
    print("ID:", "Name:")
    for key in moves:
        print(key, "->", moves[key])


async def loadBaseDamage(pokemon, moves):
    """
    Dumps move ids and its base damage.

    Parameters
    ----------
    pokemon : 
        Pokemon object obtained from aiopokeapi.
    moves :
        Map that contains ids and moves of a pokemon.

    """

    async with aiopoke.AiopokeClient() as client:
        print("Displaying the damage of each move: ")
        for move in moves.keys():
            moveData = await client.get_move(move)
            print(pokemon.name, ":", move, "->", moveData.power)
            

# You can only access api through these two lines. Treat this as the main function.
async def main():
    async with aiopoke.AiopokeClient() as client:
        # Available moves each opponent has | 
        opponentOneMoves = {}
        opponentTwoMoves = {}
        
        # Store the base damage of each move for both opponents
        baseOne = {}
        baseTwo = {}
        
        pokemonOne = ""
        pokemonTwo = ""

        # Exception handling for a ValueError to client.get_pokemon(). To validate pokemon.
        found = False
        while found == False: # Validating Pokemon 1
            try: # Enter pokemon name
                pokemonOne = input("Enter pokemon 1: ")
                pokemonOne = pokemonOne.lower()

                opponentOne = await client.get_pokemon(pokemonOne)
            except ValueError: # Invalid pokemon
                #other
                print("Not a valid value.")
                found = False
            else: # Valid Pokemon
                found = True

        found = False
        while found == False: # Validating Pokemon 2
            try: # Enter pokemon name
                pokemonTwo  = input("Enter pokemon 2: ")
                pokemonTwo = pokemonTwo.lower()

                opponentTwo = await client.get_pokemon(pokemonTwo)
            except ValueError: # Invalid pokemon
                #other
                print("Not a valid value.")
                found = False
            else: # Valid Pokemon
                found = True

        loadMoves(opponentOne.moves, opponentOneMoves)        
        loadMoves(opponentTwo.moves, opponentTwoMoves)

        print("Pokemon 1: " + opponentOne.name)
        print("Pokemon 1 moves: ")
        dumpMoves(opponentOne.name, opponentOneMoves)
        print()
        
        print("Pokemon 2: " + opponentTwo.name)
        print("Pokemon 2 moves: ")
        dumpMoves(opponentTwo.name, opponentTwoMoves)

        await loadBaseDamage(opponentOne, opponentOneMoves)
        await loadBaseDamage(opponentTwo, opponentTwoMoves)

        # Get opponentOne and opponentTwo pokemon types.
        findType(opponentOne)
        findType(opponentTwo)

        # Convert pokemon moves to the effective type against a pokemon

        # Note: Make a min and max heap for each pokemon with respect to their opposing pokemon
        ## The idea is to make a min and max of moves that are most effective for each pokemon
        ## against the pokemon they're against.
        # oneMin = [None] * len(opponentOneMoves)
        # oneMax = [None] * len(opponentOneMoves)
        # twoMin = [None] * len(opponentTwoMoves)
        # twoMax = [None] * len(opponentTwoMoves)


        # Search moves' base damage | Make another dict with the id and the move's base damage?
        # Develop type chart matrix, function, and txt file to read from.
        # Search moves on type chart in comparison against opposing pokemon.
            # sort move effectiveness in a max and min heap for each pokemon. (2 min and 2 max)
        
        

        
    
asyncio.run(main())