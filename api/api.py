from flask import abort
from flask import json
from flask import request
from flask_login import login_user, logout_user

from processors import *
from config import app, db, login_manager, manager

from models import Users, Messages

# Create the database tables.
db.create_all()

#### Example user ####
# TODO remove this
is_unq = Users.query.filter_by(username='example0').all()
if len(is_unq) == 0:
    user1 = Users(username='example0', password='example0p')
    db.session.add(user1)
    db.session.commit()
is_unq = Users.query.filter_by(username='example1').all()
if len(is_unq) == 0:
    user2 = Users(username='example1', password='example1p')
    db.session.add(user2)
    db.session.commit()
#### END_OF Example user ####


# Creates json responses with status code
def create_response(status, message=None):
    return json.jsonify({"status": status, "message": message}), status


# Login manager needs this
@login_manager.user_loader
def load_user(userid):
    return Users.query.get(userid)


#### Routes ####
# Index route
@app.route('/')
def hello_world():
    return 'Hello World!'


# Login only works with POST
# POST request example:
#    {"username":"example1", "password":"example1p"}
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If request is not in desired format, response is 400 - Bad Request
    if not request.json or 'username' not in request.json or 'password' not in request.json:
        abort(400)
    # Get username & password
    data = request.json
    username = data['username']
    password = data['password']

    # Search for the same username & password match in users table
    matches = Users.query.filter_by(username=username,
                                    password=password).all()
    # If there is a match, then user can login
    # Note: There must be only one match in the list, since username is unique in database
    if len(matches) > 0:
        login_user(matches[0])
        return create_response(message="Login is successful", status=200)
    return create_response(message="Username or Password is wrong", status=400)


@app.route('/logout')
def logout():
    logout_user()
    return create_response(message="User is logged out", status=200)
#### END_OF Routes ####

# Set processors
preprocessors_user = dict(GET_SINGLE=[user_auth_func],
                          GET_MANY=[user_auth_func])
preprocessors_message = dict(GET_SINGLE=[auth_func],
                             GET_MANY=[auth_func, message_location_filter],
                             POST=[auth_func, message_post])

# Create endpoints
manager.create_api(Users, exclude_columns=['password'], methods=['GET', 'POST'], preprocessors=preprocessors_user)
manager.create_api(Messages, methods=['GET', 'POST'], preprocessors=preprocessors_message)

# Run api loop
app.run()
