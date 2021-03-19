from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///register.db'
db = SQLAlchemy(app)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(20))


@app.route('/')
def index():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
