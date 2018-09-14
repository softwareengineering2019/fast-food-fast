""" This module defines views """

from flask import jsonify, request, json, abort
from flask.views import MethodView

class GetOrder(MethodView):
  """
  This class  defines views
  """
  orders = [
  {
    "id": 1, 
    "list of items": [
      {
        "amount": 5650, 
        "item_id": 1, 
        "item_name": "Chicken", 
        "quantity": 2, 
        "rate": 5
      }
    ], 
    "status": "True00", 
    "username": "James"
  }, 
  {
    "id": 2, 
    "list of items": [
      {
        "amount": 5650, 
        "item_id": 1, 
        "item_name": "Chicken", 
        "quantity": 2, 
        "rate": 5
      }
    ], 
    "status": "True", 
    "username": "James"
  }
]
  def get(self):

    """
    method to get all orders.
    """
    return jsonify({'Available orders':self.orders})
    
          