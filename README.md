
# Poketype:
Poketype is a web-application that takes two pokemon and gives you the most effective move in terms of move type and damage dealt to each pokemon.
The web version (thus far) can be viewed here: https://criiptico.github.io/poketype/

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
            + [x] Verify you can input pokemon
            - [ ] Verify you can retrieve the moves that are effective with that pokemon. This is sorted with respect to the type of move (which is its effectiveness) and how much damage the move actually does.
                - [ ] Filter for move type
                - [x] Filter for move damage
            + [x] Accessing different type of pokemon
            + [x] Accessing the types of attacks a particular pokemon can do
            + [x] Accessing damage an attack can do interms of type
        - Functions
            + Load chart - I'm not sure if the chart is going to be hard-coded or if I develop- or locate a type-chart.txt-esque file, then parse it.
                - I'm considering making or locating a file, then parsing it to load it each time the app is opened.
            + Type Chart Function - One of the most important functions in the program which serves in determining the effectiveness of a move.
            + Damage filter - If attack is neutral, search for most- uh oh, this feature doesn't work because it depends on move type not pokemon type.
                - Note, this still works if a move is not super or not effective against another pokemon.
            + Type filter - Standard type chart function?
            + On the design side, I plan on making an adjacency matrix that will work where I'll hard-code (since there's no api for it, I need to do it myself.) OR I could also load it in with a txt file, parse it, then input it into the matrix. Though, the purpose of the matrix is for the pokemon move type effectiveness. See: https://pokemondb.net/type
            + I'll think of more as I go along.
        - [ ] Finish the [[Prototype app]] program.
            - [x] Pokémon & Move Name
            - [x] Move Base Power
            - [x] Develop a txt file to store single type effectiveness of Pokémon of a single type. 
                - Note: This also works for dual type pokemon, refer to [[Notes#8-9-23]]
            - [ ] Pokémon type effectiveness needs:
                - [x] Attacking Move base power
                - [ ] Attacking Move type
                - [ ] Defending Pokémon type(s) {Single type and Dual type}
            - [x] ❗**Find a method to implement the dual type Pokémon chart**❗**Found!** 😁
            - [ ] Use Type Chart Function to Calculate Effectiveness of Move
                - [ ] No effect (0%) *No damage*
                - [ ] Not very effective (50%) *Cuts base power by half*
                - [ ] Normal (100%) *Normal base power*
                - [ ] Super-effective (200%) *Doubles base power*
        - [ ] Develop the front end and the back end (after the [[Prototype app]] is done)
            - [ ] Use flask and python to make a webapp of the [[Prototype app]]
## Things to note: 
I've been planning on working with Flask to retrieve and send information from the front end, but for now the priority is to get the back end working, then merge it with the front end.
