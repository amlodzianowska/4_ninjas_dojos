from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos = []
        for data in results:
            dojos.append( cls(data) )
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)
        return cls(results[0])
        

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas( cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojo.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db( query, data )
        dojo = cls( results[0])
        for row in results:
            ninja_data = {
                "id" : row['ninja.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "created_at" : row['ninja.created_at'],
                "updated_at" : row['ninja.updated_at']
            }
        dojo.ninjas.append( ninja.Ninja(ninja_data))
        return dojo