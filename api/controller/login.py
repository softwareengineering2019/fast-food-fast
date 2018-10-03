import json
import psycopg2
from flask import jsonify
from flask import request
from db_connection.config import config
import jwt, datetime
from flask.views import MethodView
from connect import APP
from flask import make_response


class LoginUsers(MethodView):

    def post(self):
        APP.config['SECRET_KEY'] = 'secretkey'
        
        email=request.json['email']
        password=request.json['password']

        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute("SELECT email,password FROM  accounts")
            user = cur.fetchall()
            for usr in user:
                if usr[0]==email and usr[1]==password:
                    token = jwt.encode({'password':usr[0][4],'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, APP.config['SECRET_KEY'])
                    return jsonify({'token' : token.decode('UTF-8')})
                elif usr[0]!=email and usr[1]!=password:
                    return jsonify({'Message':'Email or password is wrong'}), 400 
                
            # return jsonify({'message':'Your not logged in, please provide right credentials'})
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                    conn.close()
        return jsonify({'message':'Server error'}), 500
