
# Poketype:
Poketype is a web-application that takes two pokemon and gives you the most effective move in terms of move type and damage dealt to each pokemon.

###### Please note: This is a work in progress build and I'm learning these technologies along the way. This is my first time dealing with python, html forms, and Flask in the context of a web application. I appreciate your patience.

#### Pokemon API being used:
Repo Location: https://github.com/beastmatser/aiopokeapi
Documentation: https://beastmatser.github.io/aiopoke/docs/


## Plans:
As of now, I'm planning on making a prototype and then following it up with a more in depth implementation in the web version.
- Roadmap:
    + Front-end
        - App Instructions
        - Form handling
    + Back-end 
        - API related
            + Verify you can input pokemon
            - Verify you can retrieve the moves that are effective with that pokemon. This is sorted with respect to the type of move (which is its effectiveness) and how much damage the move actually does.
                - Filter for move type
                - Filter for move damage
            + Accessing different type of pokemon
            + Accessing the types of attacks a particular pokemon can do
            + Accessing damage an attack can do interms of type
        - Functions
            + Load chart - I'm not sure if the chart is going to be hard-coded or if I develop- or locate a type-chart.txt-esque file, then parse it.
                - I'm considering making or locating a file, then parsing it to load it each time the app is opened.
            + Type Chart Function - One of the most important functions in the program which serves in determining the effectiveness of a move.
            + Damage filter - If attack is neutral, search for most- uh oh, this feature doesn't work because it depends on move type not pokemon type.
                - Note, this still works if a move is not super or not effective against another pokemon.
            + Type filter - Standard type chart function?
            + On the design side, I plan on making an adjacency matrix that will work where I'll hard-code (since there's no api for it, I need to do it myself.) OR I could also load it in with a txt file, parse it, then input it into the matrix. Though, the purpose of the matrix is for the pokemon move type effectiveness. See: https://pokemondb.net/type
            + I'll think of more as I go along.
## Things to note:
I've been planning on working with Flask to retrieve and send information from the front end, but for now the priority is to get the back end working, then merge it with the front end.