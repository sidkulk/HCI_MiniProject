from flask import Flask, render_template, request
from flask_table import Table, Col
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(20))

    def __repr__(self) -> str:
        return f"Register('{self.username}', '{self.email}')"


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = Register(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'Successfully registered!'

@app.route('/users')
def users():
    users = Register.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
