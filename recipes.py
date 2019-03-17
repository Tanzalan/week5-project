import sqlite3

DB_FILE_PATH = 'data/data.db'


class Recipes:
    def __init__(self):
        '''Set up necessary database objects that will be reused by
        other functions of this class.'''
        self.connect =sqlite3.connect('data/data.db')
        self.cursor = self.connect.cursor()

    def get_recipes(self, user_id):
        '''Get a list of dictionaries(!) representing recipes that belong
        to the given user.'''
        query = "SELECT * FROM recipes WHERE user_id='{}'".format(user_id)
        self.cursor.execute(query)
        recipes = self.cursor.fetchall()
        # self.connect.close()
        return recipes


    def get_recipe(self, recipe_id):
        '''Get a dictionary(!) of the data for the dictionary whose ID
        matches the given ID.'''
        query = "SELECT * FROM recipes WHERE recipe_id={}".format(recipe_id)
        self.cursor.execute(query)
        recipe = self.cursor.fetchone()
# Perhaps you need to put recipe_id in the parentheses of fethone 
        self.connect.close()
        return recipe

    def add_recipe(self, data, user_id):
        '''Add a recipe to the database. Use the given dictionary of data
        as well as the given user ID as data for the new row.'''
        new_tuple = data['recipe'], data['ingredients'], data['pic']
        query = "INSERT INTO recipes (data, user_id) VALUES ('{}', '{}')".format(data, user_id)
        self.cursor.execute(query)
        self.connect.commit()
        self.connect.close()
        return recipe
