from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "Bye"


@app.route("/username/<name>")
def hello_name(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
