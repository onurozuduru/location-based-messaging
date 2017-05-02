import datetime
import random
from flask import abort
from flask import json
from flask import request
from flask_login import login_user, logout_user

from processors import *
from config import app, db, login_manager, manager

from models import Users, Messages, MessagesFound

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
is_unq = Messages.query.filter_by(sender=1).all()
if len(is_unq) == 0:
    # Range limits for the coordinates, it will generate it based on these limits.
    lat_limits = (64.5, 66.0)
    lon_limits = (24.5,26.0)
    for i in range(5):
        msg = Messages(sender=1, sendername='example0', message="sender1 test msg " + str(i),
                       timestamp=datetime.datetime.now(),
                       latitude=random.uniform(lat_limits[0], lat_limits[1]),
                       longitude=random.uniform(lon_limits[0], lon_limits[1]))
        db.session.add(msg)
    db.session.commit()
is_unq = Messages.query.filter_by(sender=2).all()
if len(is_unq) == 0:
    # Range limits for the coordinates, it will generate it based on these limits.
    lat_limits = (64.5, 66.0)
    lon_limits = (24.5,26.0)
    for i in range(5):
        msg = Messages(sender=2, sendername='example1', message="sender2 test msg " + str(i),
                       timestamp=datetime.datetime.now(),
                       latitude=random.uniform(lat_limits[0], lat_limits[1]),
                       longitude=random.uniform(lon_limits[0], lon_limits[1]))
        db.session.add(msg)
    db.session.commit()

is_unq = MessagesFound.query.filter_by(user_id=1).all()
if len(is_unq) == 0:
    for i in range(3):
        msg = MessagesFound(user_id=1, message_id=i+1)
        db.session.add(msg)
    db.session.commit()
is_unq = MessagesFound.query.filter_by(user_id=2).all()
if len(is_unq) == 0:
    for i in range(3):
        msg = MessagesFound(user_id=2, message_id=5+i+1)
        db.session.add(msg)
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
# preprocessors_user = dict(GET_SINGLE=[user_auth_func],
#                           GET_MANY=[user_auth_func])
preprocessors_message = dict(GET_MANY=[message_location_filter])
preprocessors_messages_found = dict(GET_MANY=[messages_found_user_filter])

# Create endpoints
manager.create_api(Users, exclude_columns=['password'], methods=['GET', 'POST'])
manager.create_api(Messages, methods=['GET', 'POST'], preprocessors=preprocessors_message, results_per_page=20)
manager.create_api(MessagesFound, methods=['GET', 'POST'],
                   preprocessors=preprocessors_messages_found, exclude_columns=['user.password'],
                   results_per_page=20)

# Run api loop
app.run()
