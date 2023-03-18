from flask import render_template, request, redirect, url_for, flash, session
from flask import current_app as app
from application.models import Venues, Shows, Users, addUser, addShow, createVenue
from application.validate import isValidUser


@app.route("/")
def home():
    login = False
    user_name = ""
    if "username" in session:
        login = True
        user_name = session["username"]

    return render_template("user.html", login=login, user_name=user_name)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = request.form["userID"]
        password = request.form["password"]
        isAdmin = False
        try:
            if request.form["isAdmin"] == "on":
                isAdmin = True
        except:
            pass

        if isAdmin and isValidUser(user_name, password, isAdmin):
            session["username"] = user_name
            session["admin"] = True
            session["badlogin"] = False
            return redirect(url_for("adminDashboard"))
        elif isValidUser(user_name, password, isAdmin):
            session["username"] = user_name
            session["admin"] = False
            session["badlogin"] = False
            return redirect(url_for("userDashboard"), username=session["username"])
        else:
            session["badlogin"] = True

    if "badlogin" in session.keys():
        flash("Either Username or Password is wrong!")
        return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))


@app.route("/new_user", methods=["GET", "POST"])
def new_user():
    if request.method == "GET":
        return render_template("new_user.html", inputUser="")

    elif request.method == "POST":
        user_name = request.form["userID"]
    password = request.form["password"]
    confirm = request.form["passwordConfirm"]
    isAdmin = 0
    try:
        if request.form["isAdmin"] == "on":
            isAdmin = 1
    except:
        pass

    if password != confirm:
        flash("Passwords do not match!")
        return render_template("new_user.html", inputUser=user_name)
    else:
        addUser(Users(UserName=user_name, Password=password, Admin=isAdmin))
        return redirect(url_for("login"))


@app.route("/admin/", methods=["GET", "POST"])
def adminDashboard():
    if "username" in session.keys() and session["admin"]:
        return render_template(
            "admin.html",
            events=Shows.query.all(),
            venues=Venues.query.all(),
        )
    else:
        return redirect(url_for("login"))


@app.route("/admin/addEvent", methods=["GET", "POST"])
def addEvent():
    if "username" in session.keys() and session["admin"]:
        if request.method == "POST":
            request.form[""]
            pass
        else:
            venues = Venues.query.all()
            return render_template("eventForm.html", venues=venues)
    else:
        return redirect(url_for("login"))


@app.route("/admin/addVenue", methods=["GET", "POST"])
def addVenue():

    if "username" in session.keys() and session["admin"]:
        if request.method == "POST":
            venueName = request.form["venueName"]
            City = request.form["City"]
            Place = request.form["Place"]
            Capacity = request.form["capacity"]
            createVenue(
                Venues(Name=venueName, Place=Place, City=City, Capacity=Capacity)
            )
            print("here")
            return redirect(url_for("adminDashboard"))
        else:
            return render_template("venueForm.html")
    else:
        return redirect(url_for("login"))


@app.route("/user/<username>/Dashboard", methods=["GET", "POST"])
def userDashboard(username):
    return render_template("user.html")
