import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
