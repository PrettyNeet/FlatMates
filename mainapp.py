from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

#set file path
file_path = os.path.abspath(os.getcwd())+"/db/flatmates.db"

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path  # Replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = db.relationship('User', backref=db.backref('homes', lazy=True))

# Routes and views
@app.route('/')
# Routes and views
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('landing'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists in the database
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another username.', 'error')
        else:
            # Hash the password before storing it in the database
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            
            # Create a new user record in the database
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Find the user by their username in the database
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.username
            return redirect(url_for('landing'))
        else:
            flash('Invalid username or password. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/landing', methods=['GET', 'POST'])
def landing():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Access the username from the session
    username = session['user_id']

    if request.method == 'POST':
        # Create a new home
        home_name = request.form['home_name']
        owner_id = session['user_id']
        
        # Create a new home record in the database
        new_home = Home(name=home_name, owner_id=owner_id)
        db.session.add(new_home)
        db.session.commit()
    
    # Retrieve the homes owned by the user from the database
    user_homes = Home.query.filter_by(owner_id=session['user_id']).all()
    return render_template('landing.html', username=username, user_homes=user_homes)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/react')
def react_app():
    return render_template('react.html')

if __name__ == '__main__':
    app.run(debug=True)
