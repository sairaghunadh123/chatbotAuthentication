from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# Initialize SQLAlchemy database object
db = SQLAlchemy(app)

# Import routes from routes.py
from routes import *

# Run Flask application
if __name__ == '__main__':
    # Create database tables
    db.create_all()
    # Run Flask app in debug mode
    app.run(debug=True)
