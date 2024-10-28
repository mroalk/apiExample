# Goal:
# Write an api that accepts a list of up to 10 food items, and number of meals desired.
# Call an AI API to build/save to db a menu, recipes, and list of groceries
#
# APIs to implement:
# POST /menus
# GET /menus/:id (gives a summary)
# GET /menus/:id/shopping-list
# GET /menus/:id/meals/:meal-id/recipe-instructions
#
#

from flask import Flask
app = Flask(__name__)

@app.route("/")
def basePath():
    # Set up a basic "how to use this API" response.
    return "Hello."

@app.route("/menus/:id")
def describeFoodItem():
    # This should provide a description of what the food item is.
    return "Hello Food Item."

@app.route("/menus/:id/shopping-list")
def listIngredients():
    # This should return a list of the ingredients for a food item
    return "Hello Ingredients."

@app.route("/menus/:id/meals/:meal-id/recipe-instructions")
def howToCook():
    # This should provide a recipe for the meal requested.
    return "Hello Recipe."

@app.route("/menus/")
def createMenu(foods,numOfMeals):
    # foods should be an array of ids.
    # numOfMeals is an int.
    #This takes up to 10 food items
    # builds/saves to db:
    #   the menu, the recipes, and the list of grocery items needed.
    return "Foods: {0}, Number Ordered: {1}".format(foods, numOfMeals)