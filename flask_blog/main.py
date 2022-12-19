from flask import Flask, render_template, request
# Import sqlalchemy to connect to database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# here configure your database url and db name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/cleanblog'
db = SQLAlchemy(app)

# create a class to send the details to database table
class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(80))
    msg = db.Column(db.String(120))
    phone = db.Column(db.Integer)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

# create a end point with GET and POST method to add the record to the database.
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contact(name=name, phone = phone, msg = message, email = email )
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')



if __name__ == "__main__":
    app.run(debug=True)

