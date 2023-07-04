from flask import Flask
from flask import render_template

app = Flask(__name__)

# It's not launching...
# Is the issue that it doesn't have the required files? css and jpg for example?
@app.route("/")
def home():
    # return "Hello World!" 
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)