import json
import psycopg2
from flask import jsonify
from db_connection.config import config
import jwt
from flask.views import MethodView
from connect import APP
# from api.controller.token_required import token_required


class FetchSpecificOrder(MethodView):
    """Fetch a specific order by id"""
    # @token_required
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
            specific_order = cur.fetchone()
            columns = ('order_id','name','rate','quantity','amount','location','status'), 200
            result = []
            for row in specific_order:
                result.append(dict(zip(columns, row)))
            return jsonify({'Specific Order':result})
            
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'message':'Id doesnot exist'}), 404
        finally:
            if conn is not None:
                conn.close()

        
        
