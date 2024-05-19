from flask import Flask, render_template, request
import os
from poketypeadvantage import eval_pokemon, get_pokemon
from heap_sort_custom_data_structure import heap_sort_custom

app = Flask(__name__, template_folder="../templates/", static_folder="../static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/evaluate-pokemon", methods=['GET'])
def evaluate_pokemon():
    if request.method == 'GET':
        pokemon_1 = request.args['pokemon_1']
        pokemon_2 = request.args['pokemon_2']

        return __eval_pokemon(pokemon_1, pokemon_2)
    

@app.route("/evaluate-pokemon/<pokemon_1>-versus-<pokemon_2>")
def __eval_pokemon(pokemon_1, pokemon_2):
    try:
        pokemon_1_data = get_pokemon(pokemon_1)
        pokemon_2_data = get_pokemon(pokemon_2)
    except ValueError:
        return render_template("eval_pokemon_value_error.html")
    move_efficacy = eval_pokemon(pokemon_1, pokemon_2) # Returning list(dict(list()), dict(list()))

    return render_template("eval_pokemon.html", pokemon1=pokemon_1, pokemon2=pokemon_2, efficacy=heap_sort_custom(move_efficacy), pokemon_1_sprite=get_sprite(pokemon_1_data), pokemon_2_sprite=get_sprite(pokemon_2_data))


def get_sprite(pokemon_data):
    if pokemon_data.sprites["front_default"] != None:
        return pokemon_data.sprites["front_default"]
    return "../static/assets/images/no_pokemon_asset.jpg"

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    app.run(debug=True)
    