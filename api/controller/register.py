import json
import psycopg2
from flask import jsonify
from flask import request
from db_connection.config import config
import jwt, datetime
from flask.views import MethodView
from connect import APP
from flask import Response

class RegisterUsers(MethodView):
    """RegisterUser extends Resource class methods post for creating a new user"""
    def post(self):

        """ insert a new user into the accounts table """
        name =request.json['name']
        email = request.json['email']
        phone = request.json['phone']
        password = request.json['password']
        if name == "" or email =="" or phone == "" or password == "":
            return jsonify({'Message':'One of the required fields is empty'}), 400

        sql = """INSERT INTO accounts(name,email,phone,password)
                VALUES(%s,%s,%s,%s) RETURNING id;"""
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (request.json['name'],request.json['email'],request.json['phone'],request.json['password']))
            
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            return jsonify({'message':'User succefully registered'}), 201
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            return ({'message':'Please provide the right inputs'})
        finally:
            if conn is not None:
                conn.close()

