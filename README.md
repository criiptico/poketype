
# Poketype:
Poketype is a web-application that takes two pokemon and gives you the most effective move in terms of move type and damage dealt to each pokemon.
The web version (thus far) can be viewed here: https://criiptico.github.io/poketype/

###### Please note: This is a work in progress build and I'm learning these technologies along the way. This is my first time dealing with python, html forms, and Flask in the context of a web application. I appreciate your patience.

#### Pokemon API being used:
Repo Location: https://github.com/beastmatser/aiopokeapi
Documentation: https://beastmatser.github.io/aiopoke/docs/


## TODO:
As of now, I'm planning on making a prototype and then following it up with a more in depth implementation in the web version.
- TODO:
    + [x] Review README.md and Notes.md. Might want to modify the roadmap on README.md.
    + Front-end
        - [ ] Use flask and python to make the webapp
        - [ ] App Instructions | Self explanatory & you can use normal html.
        - Form handling
            + [ ] Managing dynamic data with and without flask and/or python. | Dynamic: ex. What is your name: _INPUT:_ someName \ _OUTPUTS:_ Hi someName!
                - [ ] Receiving data
                    + [ ] Figure out how to access it once it's received
                    + [ ] Figure out how to use it
                - [ ] Sending data
                    - [ ] Non-calculative and dynamic data
                    - [ ] Calculative and dynamic data
                    - [ ] Figure out how to send it back
                    - [ ] Figure out how to output data onto client
        - [ ] Design | A decent design would be awesome ;-;
    + Back-end 
        - [x] API related
            + [x] Verify you can input pokemon
            + [x] Verify you can retrieve the moves that are effective with that pokemon. This is sorted with respect to the type of move (which is its effectiveness) and how much damage the move actually does.
                - [x] Filter for move type | **Not Possible** 
                - [x] Filter for move damage
            + [x] Accessing different type of pokemon
            + [x] Accessing the types of attacks a particular pokemon can do
            + [x] Accessing damage an attack can do interms of type
        - Functions
            + Load chart - I'm not sure if the chart is going to be hard-coded or if I develop- or locate a type-chart.txt-esque file, then parse it.
                - [x] I'm considering making or locating a file, then parsing it to load it each time the app is opened.
                - [x] Parse data | Self explanatory
                - [x] Store data
                    + On the design side, I plan on making an adjacency matrix that will work where I'll hard-code (since there's no api for it, I need to do it myself.) OR I could also load it in with a txt file, parse it, then input it into the matrix. Though, the purpose of the matrix is for the pokemon move type effectiveness. See: https://pokemondb.net/type
            + Type Chart Function - One of the most important functions in the program which serves in determining the effectiveness of a move.
            + Type filter - Dumps all data processed with the type chart.
            + **Additional Feature** Damage filter - If attack is normal, then search for the normal move with the most damage. Same with any other move effectiveness.
        - [ ] Finish the [[Prototype app]] program.
            - [ ] Parse api data
                + [x] Pokémon & Move Name
                + [x] Move Base Power
                + [ ] Move type
            - [x] Develop a txt file to store single type effectiveness of Pokémon of a single type. 
                - **Found one online** Refer to: https://github.com/johanngan/pokemon_types/blob/master/type_chart.txt
                - Note: This also works for dual type pokemon, refer to Notes#8-9-23
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
                - [ ] Figure out how data should be looked up and stored in
                the matrix with all the effectiveness data.
        - [ ] Develop the front end after the Prototype app is done
## Note: 
I've been planning on working with Flask to retrieve and send information from the front end, but for now the priority is to get the back end working, then merge it with the front end.
