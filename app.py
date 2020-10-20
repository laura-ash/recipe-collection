import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("pages/recipes.html", recipes=recipes,title="Recipe main page")


@app.route("/<bob>")
def get_bob(bob):
    recipes = mongo.db.recipes.find()
    return render_template("pages/recipes.html", recipes=recipes,title="Recipe main page",heaven=bob)


@app.route("/register", methods=["GET","POST"])
def get_register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, this username already exists!")
            return redirect(url_for("get_register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("pages/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check against existing users 
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if password matches user's input
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # if passwords don't match
                flash("Looks like this is an invalid username and/or password!")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Looks like this is an invalid username and/or password!")
            return redirect(url_for("login"))
    return render_template("pages/login.html")


@app.route("/profile/<username>", methods=["GET","POST"])
def profile(username):
    # get username from mongo
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("pages/profile.html", username=username)

    return render_template("profile.html", username=username)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
