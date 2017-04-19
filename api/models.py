from flask_login import UserMixin

from config import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender = db.Column(db.Integer, db.ForeignKey('users.id'))
    message = db.Column(db.String())
    timestamp = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


class MessagesFound(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    message_id = db.Column(db.Integer, db.ForeignKey('messages.id'))


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True)


class ItemsOwned(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
