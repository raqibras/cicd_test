
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi World!. This is a UV project."

if __name__ == "__main__":
    app.run(debug=False)
