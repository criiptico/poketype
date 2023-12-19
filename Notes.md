# Notes:

#### _12-19-23_
I've tried deleting the old virtual environment and installing a new one, but it didn't work. Since I've had this issue for a long time, I'm going to have to use another api-wrapper.
I'll be trying https://github.com/PokeAPI/pokebase and https://github.com/PokeAPI/pokepy and any other one on the pokeapi website.
I'm hopeful I can get the code on poketype updated to work with a new api-wrapper. I also anticipate that the only difference is the delimeter. I'll have to 
see how they both work and if either of them can work around the issue that I have with aiopokeapi.

#### _12-18-23_
I ran into a massive issue. I can't for the life of me get through this error: https://github.com/beastmatser/aiopokeapi/issues/79 
I also posted it on stack overflow: https://stackoverflow.com/questions/76517244/typeerror-argument-after-must-be-a-mapping-not-a-nonetype-error-fro. 
This is what chat gpt says to do: https://chat.openai.com/share/cd2cabd6-cb6f-4a2d-9e7e-8a7557d47496. 
So, I'll clean my virtual environment and if it doesn't work, then....... 
I really don't want to recode this codebase a third time and this time with a completely new api-wrapper to learn.

#### _11-16-23_
I just found this website called firebase. I've decided to try using flask with firebase so I can launch the server- but of course it'd be great to test it out on GitHub first.
Here are some resources I found on how to use flask:
https://www.techwithtim.net/tutorials/flask/a-basic-website
https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
https://flask.palletsprojects.com/en/2.3.x/quickstart/
Also to note, look up HTTP methods.


#### _11-8-23_
I reworked the data structures used for each state in the program, Pokemon, Move, Battle, and Load_PokemonData python files
were created to promote encapsulation and modularity. The last thing I need to transfer over from the previous version is
loading in the type chart in the Battle class, then further develop the Battle class to evaluate a pokemon. Then some
smaller steps is to implement [PyScript](https://pyscript.net/) or [Brython](https://brython.info/) so I can use this code in the html file. This would make it possible to launch this website on github pages (Since you can only launch static pages on GitHub). 
But if that fails, then I'll have to figure out how to setup an Apache HTTP server.

In summary,
Roadmap (as of now):
1. Develop **Battle** Class:
	+ Load in the type chart
	+ Develop damage calculations
2. Launch some type of code in python using [PyScript](https://pyscript.net/) or [Brython](https://brython.info/) in GitHub's Pages Website feature.
	- If it's a success, find a way to bind the my code from another directory to where the html files are.
		+ Then, develop the front end (Follow the mockup in the Front-end folder)
	- If it's not a success, use Apache HTTP to launch a server, test, then develop and repeat.
3. Finish front end design to list out the moves, move type, and effectiveness against their respective opponent. (Also, make it colorful 🌈)

#### _8-15-23_
I just added a Pokemon and a Move class which will be imported to the renamed main file, pokeType.py. 
Next is to- well, either to iden- yup. Next is to identify the places where I can easily utilize these classes.
Development of the program will continue once the new system is in place.

On another note, I think I found another way to implement the matrix, but the issue is that I'd need to make a 
class- or I'd need to make it in-scope for the new Pokemon class and the Move class. So what I'm thinking is
that instead of using a separate function to determine the level of efficacy a move has on a pokemon, that function 
can be implemented in the Pokemon class... but it w-. I'll think of implementing it once I'm done with the whole program.
I realize two things, I can't make every change I want (I'm implementing the Pokemon and Move class since they're 
genuinely useful), not all changes are good and this is one of those. 
To do it:
Pros: It'll encapsulate code. 
Cons: ... 

To not do it:
Pros: ...
Cons: Gather all information of each pokemon, then use one function to get the return data.

But... it also makes sense to have it as a separate function for all pokemon... I'll just do that then.

#### _8-22-23_
You know... maybe it **would** be better to make my own pokemon object. Considering the recent issue with transferring
data like a pokemon's type. i.e name, moves, - wait, what if I make a move type too, that way everything is in one place.
Hmmmm, definitely something to consider, that way if I **were** to make moves in my own pokemon class, then I can insert that move there and just access different things.... through it.... hmmm.
Hmmm I'm definitely considering that.

#### _8-15-23_
So I've noticed a couple of things on how to make an adjacency matrix. I was thinking of putting a map inside itself if it came to the same value, but I see that that wouldn't work since for example: Fire -> Grass and Grass -> Fire aren't the same thing. 
So, there's two ways to go about it.
1. 🔴 Make a list with numerical values that stand for different Pokémon types, then store a map that contains different Pokémon types with multipliers as values for a Pokémon with some attack defending of some def.
2. 🟡Make a map inside a map. This is an improved version of the version above. Instead of having numerical values symbolize the different pokemon types, the names would. This would make things simpler when the program would need to interpret pokemon types. Then the value of each key on this map is another map. The input for this nested map is the defending pokemon's type and the value of this map is the multiplier.
	- There's one way I want to improve this approach and that's to generalize this. As it stands, I need to input the number of Pokémon types that there are. To change this, I could change the single_type_chart.txt's second line to include all the different types included in the file or I could add them onto the dictionary, with respect to attacking Pokémon attacks, as the program is reading them. The latter is probably a better approach since I'd need data for attacking move types and the type of the Pokémon that's defending. 
	^ Go with this second approach. 👍

#### _07/06/2023_ 
#### Pyscript and Flask:
Well, I just found out about pyscript. I think I'm still going to use
Flask though. There's two reasons for it. One: to learn how to use it.
I'm planning on making a website that rates a university department's
courses **[NOT PROFESSORS]**. So I'll continue working with flask, but
I need to remember pyscript so I can learn how to use it for simple stuff.

#### PaaS and other cloud environments:
Huh, it looks like the back end of sites is a bit complicated. I'm still
a bit confused on one thing. Is this where the site is launching? Environments with PaaS are run online on servers, but I have no idea
if it actually launches a server. So I think they do launch the website.
So, the two PaaS that I'm looking into to use are https://caprover.com and https://dokku.com 
It looks like I can develop as I go for dokku, so I think that one 
might be the bese one for me since I want to make sure I can develop 
it... in real time if I need to.
On another note, I stumbled on this https://asciinema.org/ it records from the terminal and it's free.
^ It's pretty cool, neat, and useful.
Lastly, this https://www.pythonanywhere.com/ is also an option.
Here are others to consider: https://medium.com/@theHocineSaad/heroku-is-no-longer-free-here-are-the-best-alternatives-1c22d814e51d
	

#### NEW PLAN:
Develop the application with github and flask, but find a remote server or make
a local server to launch the site. There's no exception.

#### 06/24/23: Can't run flask.
So I can't use flask because it launches a server on its own. 
That is the issue. So since the plan is to launch this app
with GitHub pages, I guess my only choice is to learn how to 
use php.
CORRECTION: GitHub Pages only supports static websites. Static websites
are websites that display content exactly as it's stored in the system it's
serving it from. So..... I can still make it with flask, but I won't be able
to launch it through GitHub pages, instead a remote server or a local server 
woule work best. Well, that is a dealbreaker.

#### 06/23/23: Flask resources
Just a couple of recources to learn flask.
https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
https://flask.palletsprojects.com/en/2.3.x/quickstart/


#### 06/22/23: front end
Since the back end is experiencing some... issues ;-; it's time to get back to working on the
front end, at least for now. One thing for sure, I'd love to make this more modern.
But how?! I also need to figure out how to use python and flask. So I guess that's what I'll
do next. 

#### 06/16/23: pokeAPI Changes
I legigimately have no idea why, but I can't use the get_pokemon function from the aiopoke api.
So, I'm considering using another pokemon api wrapper to get this data.

Here is the link the the api wrapper I'm considering:
https://pokeapi.github.io/pokepy/usage/#api
Here is the link to the repo:
https://github.com/PokeAPI/pokepy

Thankfully, I haven't delved too far into this project- and it doesn't look like this one uses asyncio,
so it'll be less of a hassle. It also looks like it was made by Paul Hallett, who was the founder of the
the original pokeapi... so I probably should have gone with this more stable version- I don't know why 
get_pokemon isn't working... it worked before, but here we are now. I'll make the change by Monday.



#### 06/06/23
So, I've organized a way to input a pokemon's moves and created a way to dump all their moves.
The next steps are as shown below:
	- Search moves' base damage | Make another dict with the id and the move's base damage?
	- Develop type chart matrix, function, and txt file to read from.
	- Search moves on type chart in comparison against opposing pokemon.
		+ sort move effectiveness in a max and min heap for each pokemon. (2 min and 2 max)


#### 06/05/23
There are a couple of things that I could make. I could make a map to store
all of the relevant information regarding some pokemon. In addition, I could also 
use a max and a min heap to filter the max and min damage
of each move to the pokemon against each of them.
	- General database <- where everything is stored
	- It'd make sense to store the id's instead of all the dadta, faster? 
		+ max damage database <- where id's are stored and they're ordered from max to min
		+ min damage database <- where id's are stored and they're ordered from in to max

#### 06/04/23
Success! I've parsed the string up to the move name. There's two things that
I need to do now. I need to make a hash map or a map or sorts to 
insert the id and the name of the move onto with the key.

#### 05/31/23
As of now, I've discovered that 
(- now that I think about it, I should consider using jupyter notebooks, 
but md is good to learn too, but anyway,) when I retrieve pokemon.moves on lines 59 
and 60, it actually retrieves a... something that I think is a json object. Notice output.txt. 
I've been messing with the main python file and trying to figure out 
how to parse through it, but the issue is that it doesn't read each character of 
each line, instead it sort of reads an object...?
Anyway, here are some links to get started researching:
https://stackoverflow.com/questions/16129652/accessing-json-elements
https://realpython.com/python-json/
https://stackoverflow.com/questions/45029315/how-to-access-element-in-json-using-python
https://www.w3schools.com/python/python_json.asp
https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/
	


#### ??/??/23:
Look for these sections in the api:
	Use Moves:Moves section
	Use Moves:Moves Damage Classes
	Use Moves:Moves Ailments


Need to make a pokemon type chart function.
https://pokemondb.net/type/dual



Read this article to learn to make a better makefile, even though this 
one is fine, another one might be better:
https://earthly.dev/blog/python-makefile/

