from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"


@app.route("/Ariel")
def index():
    return "Hello, Ariel"

if __name__== "__main__":
    app.run(debug=True)