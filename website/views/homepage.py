from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# from . import db
import json
user_views = Blueprint('user_views', __name__)

@user_views.route('/')
def home():
    return render_template("home.html")


# app.register_blueprint(views)