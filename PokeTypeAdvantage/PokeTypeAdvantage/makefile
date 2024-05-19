INPUT_SRC := ../resources/input.txt
OUTPUT := ../output/output.txt

run:
	python3 poketype.py

input: $(INPUT_SRC)
	python3 poketype.py < $(INPUT_SRC)

output:
	python3 poketype.py > $(OUTPUT)

io:
	python3 poketype.py < $(INPUT_SRC) > $(OUTPUT)

venv:
	echo source ../resources/pokeTypeVenv/bin/activate
