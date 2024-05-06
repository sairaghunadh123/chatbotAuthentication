from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract user input from form
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        # Check if username or email already exists in the database
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return 'Username or email already exists'
        
        # Create new user object and add to the database
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        
        # Redirect to login page after successful registration
        return redirect(url_for('login'))
    
    # Render registration form template for GET requests
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract user input from form
        username = request.form['username']
        password = request.form['password']
        
        # Query database for user
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            # Set session variable for logged-in user
            session['logged_in'] = True
            return redirect(url_for('chat'))
        
        # Render error message for invalid credentials
        return 'Invalid username or password'
    
    # Render login form template for GET requests
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
def logout():
    # Clear session variable for logged-in user
    session.pop('logged_in', None)
    
    # Redirect to login page after logout
    return redirect(url_for('login'))
