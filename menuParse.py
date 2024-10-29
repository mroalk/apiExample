#
# Helper functions used by API.
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
