INPUT_SRC := ../resources/input.txt
OUTPUT := ../resources/output

run:
	python3 pokeType_main.py

input: $(INPUT_SRC)
	python3 pokeType_main.py < $(INPUT_SRC)

output:
	python3 pokeType_main.py > $(OUTPUT)

io:
	python3 pokeType_main.py < $(INPUT_SRC) > $(OUTPUT)

venv: # Just use this to get the pathing, then do more research on this later.
	# source ~/projects/virtualEnvironments/pokeTypeVenv/bin/activate
	echo source /home/adrian/projects/virtualEnvironments/pokeTypeVenv/bin/activate
	