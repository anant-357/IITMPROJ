from flask import render_template, request
from flask import current_app as app
from application.models import Venues, Shows


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return """wrong"""


@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form["userID"]
        password = request.form["password"]
        return render_template("index.html", user_name=user_name, password=password)
    else:
        return """wrong"""
