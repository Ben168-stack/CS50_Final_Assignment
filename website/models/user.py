from . import db
# from this package import db
# I can access anything from __init__.py
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    # maximum length of email is 150 characters and unique = true makes it so that no user can have an email that
    # already exist on the site
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
