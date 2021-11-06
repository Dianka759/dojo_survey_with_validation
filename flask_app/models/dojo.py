from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.favorite_language = data['favorite_language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate(dojo):        
        is_valid = True
        if len(dojo["name"]) <= 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo["location"]) < 1:
            flash("Please choose a location.")
            is_valid = False
        if len(dojo['favorite_language']) < 1:
            flash("Please choose a favorite langauge")
            is_valid = False
        if len(dojo["comment"]) < 1:
            flash("Please leave a comment, we love to see it!")
            is_valid = False

        return is_valid

    @classmethod
    def save(cls,data):
        query = "INSERT into dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(favorite_language)s,%(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db(query,data)

    @classmethod
    def result(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        return  connectToMySQL('dojo_survey_schema').query_db(query)
