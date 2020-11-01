import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

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

cloudinary.config(
    cloud_name=os.environ.get('CLOUD_NAME'),
    api_key=os.environ.get('API_KEY'),
    api_secret=os.environ.get('API_SECRET')
) 


@app.route("/")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("pages/recipes.html", recipes=recipes,title="Recipe main page")


@app.route("/<bob>")
def get_bob(bob):
    recipes = mongo.db.recipes.find()
    return render_template("pages/recipes.html", recipes=recipes,title="Recipe main page",heaven=bob) 


@app.route("/register", methods=["GET","POST"])
def register():
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
    return render_template("pages/auth.html", login=False)


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
    return render_template("pages/auth.html", login=True)


@app.route("/profile/<username>", methods=["GET","POST"])
def profile(username):
    # get username from mongo
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("pages/profile.html", username=username)

        return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET","POST"])
def add_recipe():
    if request.method == "POST":
        photo = request.files['photo_url']
        photo_upload = cloudinary.uploader.upload(photo)
        recipe = {
            "name": request.form.get("recipe_name"),
            "author": request.form.get("author"),
            "category_name": request.form.get("category_name"),
            "health_rating": request.form.get("health_rating"),
            "serves": request.form.get("serves"),
            "date_baked": request.form.get("date_baked"),
            "notes": request.form.get("notes"),
            "ingredients": request.form.get("ingredients").split('/'),
            "method": request.form.get("method").split('/'),
            "created_by": session["user"],
            "photo_url": photo_upload["secure_url"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe successfully submitted")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name",1)
    ratings = mongo.db.health_rating.find().sort("health_rating",1)
    return render_template("pages/add_recipe.html", categories=categories, ratings=ratings)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):     
    if request.method == "POST":
        photo = request.files['photo_url']
        photo_upload = cloudinary.uploader.upload(photo)
        submit = {
            "name": request.form.get("recipe_name"),
            "author": request.form.get("author"),
            "category_name": request.form.get("category_name"),
            "health_rating": request.form.get("health_rating"),
            "serves": request.form.get("serves"),
            "date_baked": request.form.get("date_baked"),
            "notes": request.form.get("notes"),
            "ingredients": request.form.get("ingredients").split('/'),
            "method": request.form.get("method").split('/'),
            "created_by": session["user"],
            "photo_url": photo_upload["secure_url"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)},submit)
        flash("Recipe successfully updated")
        return redirect(url_for("get_recipes"))
    
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name",1)
    ratings = mongo.db.health_rating.find().sort("health_rating",1)
    ingredients = ", ".join(recipe["ingredients"])
    method = ", ".join(recipe["method"])
    return render_template("pages/edit_recipe.html", recipe=recipe, categories=categories, ratings=ratings, ingredients=ingredients, method=method)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted")
    return redirect(url_for("get_recipes"))


@app.route('/recipes/<recipe>', methods=["GET"])
def recipe_page(recipe):
    recipe = mongo.db.recipes.find_one({"name": recipe})
    return render_template("pages/recipe_page.html", recipe=recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)


