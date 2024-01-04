from flask import Flask, render_template, request

# Following error from this line: Traceback (most recent call last):
#   File "/home/adrian/projects/poketype-copy/poketype/Front-end/main/home.py", line 4, in <module>
#     from PokeTypeAdvantage.main.PokeTypeAdvantage import eval_pokemon
# ModuleNotFoundError: No module named 'PokeTypeAdvantage'
#
# Read up on this link to formalize PokeTypeAdvantage as a formal python package:
# https://www.freecodecamp.org/news/build-your-first-python-package/
from PokeTypeAdvantage.main.PokeTypeAdvantage import eval_pokemon

app = Flask(__name__, template_folder="../templates/")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/evaluate-pokemon", methods=['GET'])
def evaluate_pokemon():
    if request.method == 'GET':
        pokemon_1 = request.args['pokemon_1']
        pokemon_2 = request.args['pokemon_2']
        print(pokemon_1, pokemon_2)
        
        return __eval_pokemon(pokemon_1, pokemon_2)
    
@app.route("/evaluate-pokemon/<pokemon_1>-versus-<pokemon_2>")
def __eval_pokemon(pokemon_1, pokemon_2):
    eval_pokemon(pokemon_1, pokemon_2)

    return f"Hello {pokemon_1} and {pokemon_2}!"

if __name__ == '__main__':
    app.run(debug=True)
    