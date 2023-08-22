import asyncio
import aiopoke

def loadMatrix(parsedData, typeMatrix): # Need typeMatrix to be pass by reference
    # print("Data:", parsedData)
    # print(str(parsedData[0]), str(parsedData[1]), str(parsedData[2])) #issue with last float value of fairy fairy 0.5 from single_type_chart.txt file.

    # if the attacking value isn't found in the outer map
    if (str(parsedData[0]) in typeMatrix) == False: # Look up how to access the first value 
        # add a new value to outer matrix
        newMap = {}
        typeMatrix[str(parsedData[0])] = newMap
    # else access the value of the attacking value and add the defending type as the key and its multiplier as its value
    # Continue until there's no more parsedData given to us.
    typeMatrix[str(parsedData[0])][str(parsedData[1])] = float(parsedData[2])

# populates and returns a vector with parsed "typeMultiplier" data. 
# Unparsed data is in this form: attack_data defend_data multiplier_data
def findTypeChart(typeMultiplier):
    typeData = ""
    parsedData = []
    for character in typeMultiplier:           
        if character == typeMultiplier[len(typeMultiplier) - 2] or character == ' ':
            if character == typeMultiplier[len(typeMultiplier) - 2]:
                typeData = "".join([typeData, character])
            parsedData.append(typeData)
            typeData = ""
            continue
        typeData = "".join([typeData, character])
            
    return parsedData
 
# Opens file and iterates through the single_type_chart txt file
def loadTypeChart(typeChart): # Also send a map, referenced below as someMap.
    file_path = "single_type_chart.txt"

    print()
    print("Loading type chart...")
    print()
    
    with open(file_path) as file:
        next(file)

        for line in file:
            # Create a vector (python equivalent is a list)
            parsedData = []
            parsedData = findTypeChart(line) # Return a vector with parsed types and multiplier / load a vector
            # print("Line of data:", line)
            # for data in parsedData:
            #     print(data)
            loadMatrix(parsedData, typeChart) # Loads vector data onto matrix
                # Iterate through vector
                # Store data from vector to a map | Needs its own function.
        # print(typeChart)

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
        findMoves(str(i), moveMap) # The intention is for this to be changed here.

    # return moveMap # What is it returning?

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
    # return moveMap

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
    pokemonTypes = set()
    type = ""
    # print(pokemon.name, "data.")
    # print(pokemon.types) # Parse to get data types.
    data = str(pokemon.types)
    typeNameIt = data.find("name='")

    print("Parsing", pokemon.name, "data...")
    while typeNameIt != -1:

        # for character in data:
        for i in range(typeNameIt + 6, len(data)):
            if data[i] == "'":
                break
            type = "".join([type, data[i]])
        pokemonTypes.add(type)
        type = ""
        data = data.replace("name='", "", 1)
        typeNameIt = data.find("name='")

    print(pokemonTypes)

    return pokemonTypes # pokemonType is a list... or a set? A set.


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


async def loadBaseDamage(pokemon, moves, baseMoveDamage):
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
        # print("Displaying the damage of each move: ")
        for move in moves.keys():
            moveData = await client.get_move(move)
            baseMoveDamage[move] = moveData.power
            print(pokemon.name, ":", move, "->", baseMoveDamage[move], "-", moveData.type)
            

# You can only access api through these two lines. Treat this as the main function.
async def main():
    async with aiopoke.AiopokeClient() as client:
        # Available moves each opponent has | in the form [id] = name
        opponentOneMoves = {}
        opponentTwoMoves = {}
        
        # Store the base damage of each move for both opponents | form the [id] = power | Note: convert the value into a list... need the power type. OR make another map.
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
                # found = False
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
                # found = False
            else: # Valid Pokemon
                found = True

        loadMoves(opponentOne.moves, opponentOneMoves)        
        loadMoves(opponentTwo.moves, opponentTwoMoves)

        print("Pokemon 1: " + opponentOne.name)
        print("Pokemon 1 moves: ")
        # dumpMoves(opponentOne.name, opponentOneMoves)
        await loadBaseDamage(opponentOne, opponentOneMoves, baseOne) # Need to get the move type from here as well. Same thing in line 234
        print()
        
        print("Pokemon 2: " + opponentTwo.name)
        print("Pokemon 2 moves: ")
        # dumpMoves(opponentTwo.name, opponentTwoMoves)
        await loadBaseDamage(opponentTwo, opponentTwoMoves, baseTwo)

        # Load the type chart txt into an adjacency.... list, was it a list or a matrix? # TODO: Look back on notes if it was a list or matrix. I thinK it was MATRIX
        # Do this at the beginning of the program so it doesn't load it each time.
        typeChart = {}

        loadTypeChart(typeChart) # Send an adjacency matrix | Use the unique values value, then use a map that contains a map as a value for repeated values.


        # Get opponentOne and opponentTwo pokemon types.
        findType(opponentOne)
        findType(opponentTwo)

        # For each pokemon, look at each move
            # While looking at each move, make a max heap with respect to the moves that are most effective.
        # State each pokemon's moves' effectiveness by name and numerically against the opposing pokemon, traverse the loaded max heap


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