import json
import psycopg2
from flask import jsonify
from db_connection.config import config
import jwt
from flask.views import MethodView
from connect import APP


class GetAnOrderHistory(MethodView):
    """get order history for a specific user """

    def get(self,id):
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute("SELECT order_id,name,rate,quantity,amount,location,status FROM orders WHERE order_id = (%s)", (id,))
            order_history = cur.fetchone()
            columns = ('order_id','name','rate','quantity','amount','location','status')
            result = []
            for row in order_history:
                result.append(dict(zip(columns, row)))
            return jsonify({'Order History for a specific user': result})
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'message':'Id doesnot exist'}), 404
        finally:
            if conn is not None:
                conn.close()

        
        
