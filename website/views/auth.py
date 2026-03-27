from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
# from . import db
import json

SUCCESS = "success"
ERROR = "error"
WARNING = "warning"

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":

        email = request.form.get('email')
        password = request.form.get('password')

        # flash("You have logged in.", category=SUCCESS)
        return redirect(url_for("user_views.home"))
    
    else:
        return render_template("user/user_auth/login.html")

@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        return redirect(url_for("user_views.home"))

    else:

        return render_template("user/user_auth/register.html")


# app.register_blueprint(views)=