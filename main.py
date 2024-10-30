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
# Things to build:
# Logging.
# Integration with AI? Some kind of external service.
# Maybe just write to a database instead?

import logging
import logging.handlers
import os.path
from flask import Flask
from menuParse import foodAspect, menuCreator

#Logging Configuration
path = os.path.dirname(os.path.realpath(__name__))
logFile = os.path.join(path,'apiExample.log')
log = logging.getLogger('apiExample')
log.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(log,maxBytes=1048576,backupCount=3)
handler.setFormatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s::%(lineno)d]')
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
    menu = menuCreator(foods,numOfMeals)
    return "Foods: {0}, Number Ordered: {1}".format(foods, numOfMeals)