#
# Helper functions used by API.
#
# TO DO:
# Finish MenuCreator
# Integrate with something to retrieve ingredients/cooking instructions?
# Save menus to db for retrieval?
#
import json
import os

def getFoodJson():
    currentPath = os.path.dirname(os.path.realpath(__name__))
    foodFilePath = currentPath+"\\fooditems.json"
    foodJson = json.loads(open(foodFilePath).read())
    return foodJson

def foodAspect(id,characteristic):
    foodJson = getFoodJson()
    for i in foodJson['foodItems']:
        if foodJson['foodItems'][i]['id'] == id:
            return foodJson['foodItems'][i][characteristic]

def menuCreator(foodList,mealCount):
    #Resolve duplicate ids before generating list?
    menuList = []
    for f in foodList:
        recipe = foodAspect(f,'Recipe')
        shoppingList = foodAspect(f,'Ingredients')
        foodPlot = [recipe,shoppingList]
        menuList.append(foodPlot)
