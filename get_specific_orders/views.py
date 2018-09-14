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
    
    def get(self, order_id):
        """
         method to get all or specific orders.
        """
        if type(order_id) in [int]:
            ord = [order for order in self.orders if order['id'] == order_id]
            return jsonify({'Specific Order': ord})
        else:
            raise TypeError("Order_id should be a non negative integer")