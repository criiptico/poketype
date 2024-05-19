# Poketype:
Poketype is a web-application that takes two pokemon and gives you the most effective move in terms of move type and damage dealt to each pokemon.

## The project is now **live**
Click here http://criiptico.pythonanywhere.com/ to view the build.

## Want to run this app locally?
To run this app locally, from the main directory go to `poketype/Front-end/main`, then run the `home.py` file.

## Reflection:
The pokemon PokeType web-app is finally up! I hope you enjoy using it as much as I did creating it.
For my first web-app project, I think I did pretty well. I identified a problem and decided that this was a good solution to it,
then I tried to stick to it without changing it too much, then I finally finished it.

Working on this project has been awesome but I wish I had more wiggle room to experiment with threads and integrate
Javascript into the application. The issue was that I didn't want to introduce Javascript because I don't know it, but I know
that I want to use it for sure in my next project "YouTube Purger", an app that unsubscribes you from youtube channels.
Another reason why I didn't use Javascript was because I wasn't sure how threads was going to interact with wherever I 
was going to deploy my application. This was a huge issue because I can't assume something if I've never worked with it before.
I think I still have that worry, so I'll have to thoroughly research that topic for my next project.

## Final Notes:
This app will not be maintained but feel free to use this code in whichever code you might need it for.
I especially encourage using the pokemon api wrapper that I made which you can access here https://github.com/criiptico/PokeTypeAdvantage. 
This api wrapper is where I spent most of my time learning and debugging. 
It has useful info on serialization, retrieval, and processing json from the PokeApi which can be found here https://pokeapi.co/.



##### Milestones:
- [x] Back-end
- [x] Hosting and Development
- [x] Front-end

##### TODO:
+ Back-end
    - [x] Implementing Move and Pokemon class into all functions.
    - [x] API related
        + [x] Verify you can input pokemon
        + [x] Verify you can retrieve the moves that are effective with that pokemon. This is sorted with respect to the type of move (which is its effectiveness) and how much damage the move actually does.
            - [x] Filter for move type | **Not Possible** 
            - [x] Filter for move damage
        + [x] Accessing different type of pokemon
        + [x] Accessing the types of attacks a particular pokemon can do
        + [x] Accessing damage an attack can do interms of type
    - [x] Finish the Prototype app program.
        - [x] Documentation
        - [x] Parse api data
            + [x] Pokémon & Move Name
            + [x] Move Base Power
            + [x] Move type
        - [x] Pokémon type effectiveness needs:
            - [x] Attacking Move base power
            - [x] Attacking Move type
            - [x] Defending Pokémon type(s) {Single type and Dual type}
        - [x] Develop a txt file to store single type effectiveness of Pokémon of a single type. 
            - **Found one online** Refer to: https://github.com/johanngan/pokemon_types/blob/master/type_chart.txt
            - Note: This also works for dual type pokemon. Refer the the bullet point below.
        - [x] Find a method to implement the dual type Pokémon chart. Refer to the raw format of README.md for a formatted explanation.
            + Suppose we have Charizard, charizard is of these types:
                
                    defType1 = Fire
                    defType2 = Flying
                
                Charizard needs to defend against this type of move
                
                    atkType = Water
                
                Using the single type chart for each type that Charizard is:

                **Atk** **Def**

                Water vs. Fire = 200% (Super-Effective aka 2) 
                Water vs. Flying = 100% (Normal aka 1)

                Then multiplying those effectiveness: 
                2 (Water vs. Fire) * 1 (Water vs. Flying) = 2 (Resulting Effectiveness)
        - [x] Parse and Load type chart from https://github.com/johanngan/pokemon_types/blob/master/type_chart.txt
            + [x] Load Type Chart Function - Loads the type chart with data from https://github.com/johanngan/pokemon_types/blob/master/type_chart.txt
            + This is unnecessary, ~~Type Chart Dump - Dumps all data processed with the type chart.~~
        - [x] Eval efficacy function - One of the most important functions in the program which serves in determining the effectiveness of a move.
            + [x] Use these in to return the resulting effectiveness of a Move with respect to its type and the defending pokemon's defense
                - [x] No effect (0%) *No damage*
                - [x] Not very effective (50%) *Cuts base power by half*
                - [x] Normal (100%) *Normal base power*
                - [x] Super-effective (200%) *Doubles base power*
            + [x] Pokemon Type Efficacy Dump - Dumps all effective moves against a pokemon.
        - **Additional Feature** Damage filter - If attack is normal, then search for the normal move with the most damage. Same with any other move effectiveness.

+ Hosting and Development:
    - [x] Use flask and python to make a webapp prototype - Preferably one that works like a "portfolio". Ex. portfolio.com/poketype, portfolio.com/about, etc.
        - Form handling
            + [x] Managing dynamic data with and without flask and/or python. - Dynamic: ex. What is your name: _INPUT:_ someName \ _OUTPUTS:_ Hi someName!
                - [x] Receiving data
                    + [x] Figure out how to access it once it's received
                    + [x] Figure out how to use it
                - [x] Sending data
                    - [x] Non-calculative and dynamic data
                    - [x] Calculative and dynamic data
                    - [x] Figure out how to send it back
                    - [x] Figure out how to output data onto client
    ~~- [ ] Find a way to host on Firebase~~
    ~~- [ ] Purchase a domain - Build around a "portfolio" website. Ex. portfolio.com/poketype, portfolio.com/about, etc.~~

+ Front-end
    - [x] Web Design
        + [x] Work on a Mockup - Refer to "../Front-end/pokeType_mockup.png" and "../Front-end/poketype.fig"
            - [x] Different stages of the mockup - Unloaded and loaded pokemon
        + [x] Include App Instructions in the mockup - Self explanatory & you can use normal html.
