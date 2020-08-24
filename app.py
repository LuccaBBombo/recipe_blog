import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'data_centric'
app.config["MONGO_URI"] = os.environ['MONGO_URI']

mongo = PyMongo(app)

#---------------------Recipes--------------------------------------------

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recipes')
def recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find(),
                           categories=mongo.db.categories.find())


@app.route('/search', methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = mongo.db.recipes.find({"$text": {"$search": query}})
    return render_template('recipes.html', recipes=recipes,
                           categories=mongo.db.categories.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))


@app.route('/insert_review/<recipe_id>', methods=['POST'])
def insert_review(recipe_id):
    recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))


@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    # find the recipe with the id
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # get the ingredients from it and split the string into a list
    recipe_ing = recipe['recipe_ingredients'].split('/')
    # get the cooking method from it and split the string into a list
    recipe_cook = recipe['recipe_prepare_method'].split('/')
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_page.html", recipe=the_recipe,
                           recipe_ingredients=recipe_ing,
                           recipe_method=recipe_cook,
                           reviews=mongo.db.reviews.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')), debug=True)
