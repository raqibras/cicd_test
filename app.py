from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bug fix 1"


if __name__ == "__main__":
    app.run(debug=False)
