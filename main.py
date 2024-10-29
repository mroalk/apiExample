# Goal:
# Write an api that accepts a list of up to 10 food items, and number of meals desired.
# Call an AI API to build/save to db a menu, recipes, and list of groceries
#
# APIs endpoints:
# POST /menus - Not Implemented
# GET /menus/:id (gives a summary) - Written
# GET /menus/:id/shopping-list - Written
# GET /menus/:id/meals/:meal-id/recipe-instructions - Not Implemented
#
#

import menuParse

from flask import Flask

from menuParse import foodAspect

app = Flask(__name__)


@app.route("/")
def basePath():
    # Set up a basic "how to use this API" response.
    return "Hello."


@app.route("/menus/:id")
def describeFoodItem():
    # This should provide a description of what the food item is.
    description = foodAspect(id,"Description")
    return description


@app.route("/menus/:id/shopping-list")
def listIngredients():
    # This should return a list of the ingredients for a food item
    ingredients = foodAspect(id,'Ingredients')
    return ingredients


@app.route("/menus/:id/meals/:meal-id/recipe-instructions")
def howToCook():
    # This should provide a recipe for the meal requested.
    recipe = foodAspect(id, 'Recipe')
    return recipe

@app.route("/menus/")
def createMenu(foods,numOfMeals):
    # foods should be an array of ids.
    # numOfMeals is an int.
    #This takes up to 10 food items
    # builds/saves to db:
    #   the menu, the recipes, and the list of grocery items needed.
    return "Foods: {0}, Number Ordered: {1}".format(foods, numOfMeals)