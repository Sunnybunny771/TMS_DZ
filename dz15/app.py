from flask import Flask, redirect, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Registration(db.Model):
    id =db.Column(db.Integer, primary_key = True)
    first_name =db.Column(db.String(30), nullable=False)
    name =db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    
    def __repr__(self) -> str:
        return '<Article %r>' % self.id



@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/users')
def users():
    users = Registration.query.order_by(Registration.first_name).all()
    return render_template("users.html", users=users)


@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == "POST":
        first_name = request.form['first_name']
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']

        registration = Registration(first_name=first_name, name=name, username=username, email=email)

        try:
            db.session.add(registration)
            db.session.commit()
            return redirect(url_for('home'))
        except Exception:
            return 'Ошибка регистрации'
    else:
        return render_template("registration.html")


if __name__ =="main":
    app.run(debug=True)