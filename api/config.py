import os

from flask import Flask
from flask_login import LoginManager
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy


# Set the database path
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database/test.db')
if os.path.exists(DATABASE):
    os.unlink(DATABASE)

# Create the Flask application and the Flask-SQLAlchemy object.
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % DATABASE
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.urandom(24)

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
