
# Poketype:
Poketype is a web-application that takes two pokemon and gives you the most effective move in terms of move type and damage dealt to each pokemon.
The web version (thus far) can be viewed here: https://criiptico.github.io/poketype/

###### Please note: This is a work in progress build and I'm learning these technologies along the way. This is my first time dealing with python, html forms, and Flask in the context of a web application. I appreciate your patience.


## Plans:
As of now, I'm planning on making a prototype and then following it up with a more in depth implementation in the web version.
- Roadmap:
    + Front-end
        - App Instructions
        - Form handling
    + Back-end 
        - API related
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
            + I'll think of more as I go along.
## Things to note:
I've been planning on working with Flask to retrieve and send information from the front end, but for now the priority is to get the back end working, then merge it with the front end.
