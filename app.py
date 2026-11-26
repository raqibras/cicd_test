from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/health")
def health():
    return "Health"

@app.route("/version")
def version():
    return "Version 1.0.0"

@app.route("/author")
def author():
    return "Admin"

if __name__ == "__main__":
    app.run(debug=False)
