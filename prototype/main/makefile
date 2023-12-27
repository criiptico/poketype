INPUT_SRC := ../resources/input.txt
OUTPUT := ../output/output.txt

run:
	python3 pokeType_main.py

input: $(INPUT_SRC)
	python3 pokeType_main.py < $(INPUT_SRC)

output:
	python3 pokeType_main.py > $(OUTPUT)

io:
	python3 pokeType_main.py < $(INPUT_SRC) > $(OUTPUT)

venv:
	echo source ../resources/pokeTypeVenv/bin/activate
