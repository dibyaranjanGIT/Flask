
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/homepage') # This creates an endpoint
def home_page():
    return render_template('index.html')

@app.route('/about')
def about():
    name = "Dibyaranjan Jena" # How to pass an variable to a template
    return render_template('about.html', full_name=name)

if __name__ == "__main__":
    app.run(debug=True) # with debug=True any changes to the current file will reflected in your webpage