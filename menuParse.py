#
# Helper functions used by API.
#
# TO DO:
# Finish MenuCreator
# Integrate with something to retrieve ingredients/cooking instructions?
# Save menus to db for retrieval
# Create actual DB, validate.

import json
import os
import pymysql

def dbConn():
    conn = pymysql.connect(
        host='localhost',
        user='user',
        password='password',
        db='db1',
        charset='utf8mb4',
    )
    return conn

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
    #This removes duplicates before processing:
    foodList = list(set(foodList))
    menuList = []
    for f in foodList:
        recipe = foodAspect(f,'Recipe')
        shoppingList = foodAspect(f,'Ingredients')
        foodPlot = [recipe,shoppingList,mealCount]
        menuList.append(foodPlot)
    return menuList

def menuStorage(menu):
    # Format this to take the data from menuCreator and section it into table data for a database.
    # Pausing this until I can find an easily portable DB tech to standup and use for testing.
    # This should then return a menu ID which can be retrieved via subsequent API calls.
    conn = dbConn()
    try:
        with conn.cursor() as cursor:
            sqlStatement = "INSERT into `menus` (`recipe`,`shoppingList`,`orderCount`) VALUES (%s, %s, %s)"
            cursor.execute(sqlStatement, (menu['recipe'],menu['shoppingList'],menu['mealCount']))
        conn.commit()
    finally:
        #Finally needs to retrieve the id of the row created.
        conn.close()
        return "menuStorage."