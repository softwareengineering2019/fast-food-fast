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
  def post(self):
    """
    method to post an order
    """
    list_of_items=[]
    list_of_items=request.json['list_item']
    usern=request.json['username']
    status=request.json['status']
    
    if usern.strip()=="":
        return jsonify({'error':'username is missing!'}),403
    
    if status =="":
        return jsonify({'error':'Status is empty!'}),403

    order={"id":len(self.orders) + 1, "username":usern,"list of items":list_of_items,"status":status}
    self.orders.append(order)
    return jsonify({'New_orders':order } ),201
  
          