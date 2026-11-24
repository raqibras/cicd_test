from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/health")
def health():
    return "APIs Healthy"

if __name__ == "__main__":
    app.run(debug=False)
