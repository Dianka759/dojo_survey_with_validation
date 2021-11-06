from flask import flash
import re

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.gender = data['gender']
        self.location = data['location']
        self.favorite_language = data['favorite_language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate(dojo):        
        is_valid = True
        if len(dojo["name"]) <= 3:
            flash("We need your full name")
            is_valid = False
        if len(dojo["location"]) < 1:
            flash("Please choose a location")
            is_valid = False
        if len(dojo['favorite_language']) < 1:
            flash("Langauge required")
            is_valid = False
        if len(dojo["comment"]) < 1:
            flash("Comment required")
            is_valid = False
        # if len(dojo['gender']) < 1:
        #     flash("Gender option required")
        #     is_valid = False
        # if "sub" not in dojo['subscribe']:
        #     flash("You need to sub!")
        #     is_valid = False

        return is_valid
