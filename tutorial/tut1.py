"""
Flask documentation
https://flask.palletsprojects.com/en/2.0.x/quickstart/
Run below command to start your flask application
set FLASK_APP=tut1
flask run
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"