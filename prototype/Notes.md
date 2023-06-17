# Notes:


##### 06/16/23: pokeAPI Changes
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



##### 06/06/23
	So, I've organized a way to input a pokemon's moves and created a way to dump all their moves.
	The next steps are as shown below:
		- Search moves' base damage | Make another dict with the id and the move's base damage?
        - Develop type chart matrix, function, and txt file to read from.
        - Search moves on type chart in comparison against opposing pokemon.
            + sort move effectiveness in a max and min heap for each pokemon. (2 min and 2 max)


##### 06/05/23
	There are a couple of things that I could make. I could make a map to store
	all of the relevant information regarding some pokemon. In addition, I could also 
	use a max and a min heap to filter the max and min damage
	of each move to the pokemon against each of them.
		- General database <- where everything is stored
		- It'd make sense to store the id's instead of all the dadta, faster? 
			+ max damage database <- where id's are stored and they're ordered from max to min
			+ min damage database <- where id's are stored and they're ordered from in to max

##### 06/04/23
	Success! I've parsed the string up to the move name. There's two things that
	I need to do now. I need to make a hash map or a map or sorts to 
	insert the id and the name of the move onto with the key.

##### 05/31/23
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
	


##### ??/??/23:
	Look for these sections in the api:
		Use Moves:Moves section
		Use Moves:Moves Damage Classes
		Use Moves:Moves Ailments


	Need to make a pokemon type chart function.
	https://pokemondb.net/type/dual



	Read this article to learn to make a better makefile, even though this 
	one is fine, another one might be better:
	https://earthly.dev/blog/python-makefile/

