from flask import Flask, render_template, request
from poketypeadvantage import eval_pokemon

app = Flask(__name__, template_folder="../templates/")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/evaluate-pokemon", methods=['GET'])
def evaluate_pokemon():
    if request.method == 'GET':
        pokemon_1 = request.args['pokemon_1']
        pokemon_2 = request.args['pokemon_2']
        # print(pokemon_1, pokemon_2)
        
        return __eval_pokemon(pokemon_1, pokemon_2)
    
@app.route("/evaluate-pokemon/<pokemon_1>-versus-<pokemon_2>")
def __eval_pokemon(pokemon_1, pokemon_2):
    move_efficacy = eval_pokemon(pokemon_1, pokemon_2)
    # for item in some_items:
    #     print(f"".join(str(item))) # Try this: https://www.youtube.com/watch?v=tMNJtYDSOBY they use jinja and js

    return render_template("eval_pokemon.html", pokemon1=pokemon_1, pokemon2=pokemon_2, efficacy=move_efficacy)
    # return f"Hello {pokemon_1} and {pokemon_2}!"

if __name__ == '__main__':
    app.run(debug=True)
    