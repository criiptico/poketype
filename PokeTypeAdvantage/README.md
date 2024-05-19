# PokeTypeAdvantage

This python package communicates with PokeApi endpoints to retrieve pokemon data
and to process it so that it takes the most effective move from one pokemon against another.

## Pokemon Api used:
https://pokeapi.co/

## How to use:
Due to issues with the package, include it into your project like this:
```
import sys
sys.path.append('../../PokeTypeAdvantage/PokeTypeAdvantage')
from PokeTypeAdvantage import eval_pokemon, get_pokemon
```


## Source Code
Most of the source code is located under PokeTypeAdvantage/PokeTypeAdvantage and contains these files:
- poketypeadvantage.py
    + Contains abstracted functions that the user must use to make requests to the pokemon api.
- Battle.py
    + A class that evaluates the moves of two pokemon.
- CustomPokeApiWrapper.py
    + Performs the request to the pokemon api to this endpoint https://pokeapi.co/api/v2/pokemon/{endpoint}
    and this endpoint https://pokeapi.co/api/v2/move/{endpoint} . This file provides to functions to retrieve, package, and return pokemon objects and move objects as defined in the pokemon api.
- Load_Pokemon_data.py
    + Loads the pokemon data that was requested by the user into a custom data type.
- Move.py
    + A custom class used as a custom data type.
- Pokemon.py
    + A custom class used as a custom data type.
- poketype.py
    + Used to test code.
