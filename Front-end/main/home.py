from flask import Flask, render_template, request

# from ..prototype.main.poketype import eval_pokemon
# import sys
# print(sys.path)
import sys
sys.path.append('~/poketype/PokeTypeAdvantage')
from PokeTypeAdvantage import eval_pokemon

# sys.path.append('/home/adrian/projects/poketype')
# from prototype.main.poketype import eval_pokemon
# from ...prototype.main.poketype import eval_pokemon
# from poketype import eval_pokemon

# from prototype.main.poketype import eval_pokemon
# import sys
# print(sys.path)
# sys.path.insert(0, '/home/adrian/projects/poketype')
# from PokeTypeAdvantage.main.poketype import eval_pokemon

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
    