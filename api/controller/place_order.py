import json
import psycopg2
from flask import jsonify
from flask import request
from db_connection.config import config
import jwt
from flask.views import MethodView
from connect import APP
from flask import Response

class PlaceOrder(MethodView):
    """ Place an order"""
    def post(self):

        """ place an order and insert in the order table """

        sql12 = """INSERT INTO orders (name,rate,quantity,amount, location)
                VALUES(%s,%s,%s,%s,%s);"""
        
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql12, (request.json['name'],request.json['rate'],request.json['quantity'],request.json['amount'],request.json['location']),)
            cur.execute("SELECT order_id,name,rate,quantity,amount,location,status FROM orders")
            tt = cur.fetchall()
            columns = ('order_id','name','rate','quantity','amount','location','status')
            result = []
            for row in tt:
                result.append(dict(zip(columns, row)))
            return jsonify({'Your order': result}), 201
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return jsonify({'Message': 'Invalid response'}),403
