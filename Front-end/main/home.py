from flask import Flask, render_template, request
from poketypeadvantage import eval_pokemon, get_pokemon

app = Flask(__name__, template_folder="../templates/", static_folder="../static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/evaluate-pokemon", methods=['GET'])
def evaluate_pokemon():
    if request.method == 'GET':
        pokemon_1 = request.args['pokemon_1']
        pokemon_2 = request.args['pokemon_2']

        # Some Resources To Display Pokemon Images...
        # Found a good stack overflow method to do this: https://stackoverflow.com/questions/46785507/python-flask-display-image-on-a-html-page
        # This one might not be as good: https://kanchanardj.medium.com/how-to-add-images-to-html-in-a-flask-app-4dbcc92e3aeb
        
        return __eval_pokemon(pokemon_1, pokemon_2)
    

@app.route("/evaluate-pokemon/<pokemon_1>-versus-<pokemon_2>")
def __eval_pokemon(pokemon_1, pokemon_2):
    try:
        pokemon_1_data = get_pokemon(pokemon_1)
        pokemon_2_data = get_pokemon(pokemon_2)
    except ValueError:
        # Return the home template, but with an error popup
        return render_template("eval_pokemon_value_error.html") # TODO: Develop this template to include a popup

    move_efficacy = eval_pokemon(pokemon_1, pokemon_2)
    # for item in some_items:
    #     print(f"".join(str(item))) # Try this: https://www.youtube.com/watch?v=tMNJtYDSOBY they use jinja and js

    return render_template("eval_pokemon.html", pokemon1=pokemon_1, pokemon2=pokemon_2, efficacy=move_efficacy)
    # return f"Hello {pokemon_1} and {pokemon_2}!"


if __name__ == '__main__':
    app.run(debug=True)
    