from flask import Flask, Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# from . import db
import json

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
    
    else:
        return render_template("user/user_auth/login.html")

@auth.route('/register')
def register():
    return render_template("user/user_auth/register.html")


# app.register_blueprint(views)=