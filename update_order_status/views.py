""" This module defines views """
from flask import jsonify, request
from flask.views import MethodView
class GetOrder(MethodView):
    """
    This class  defines views
    """
    orders = [
        {
            "id": 1,
            "list of items": [{
                "amount": 5650,
                "item_id": 1,
                "item_name": "Chicken",
                "quantity": 2,
                "rate": 5
            }],
            "status": "True00",
            "username": "James"
        },
        {
            "id": 2,
            "list of items": [{
                "amount": 5650,
                "item_id": 1,
                "item_name": "Chicken",
                "quantity": 2,
                "rate": 5
            }],
            "status": "True",
            "username": "James"
            }
        ]

    def put(self, id):
        """
         method to update specific order based on the id.
        """
        if id:
            for order in self.orders:
                if order["id"] == id:
                    some_json = request.get_json()
                    order['status'] = some_json['status']
                    return jsonify({"Updated list of dictionary":order}), 200
        else:
            return "You didn't specify an id"
