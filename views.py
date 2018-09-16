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
                "amount": 10000,
                "item_id": 1,
                "item_name": "Burger",
                "quantity": 4,
                "rate": 2500
            }],
            "status": "Completed",
            "username": "James Kisuule"
        },
        {
            "id": 2,
            "list of items": [{
                "amount": 6000,
                "item_id": 2,
                "item_name": "Chicken",
                "quantity": 2,
                "rate": 3000
            }],
            "status": "Rejected",
            "username": "Kalyesubula Noah"
            },
             {
            "id": 3,
            "list of items": [{
                "amount": 20000,
                "item_id": 3,
                "item_name": "Chips",
                "quantity": 4,
                "rate": 5000
            }],
            "status": "Accepted",
            "username": "Ssevume Ronald"
            }
        ]
    def get(self, order_id):
        """
         method to get all or specific orders.
        """
        if order_id == None:
            return jsonify({'Available orders':self.orders})
        else:
            if type(order_id) in [int]:
                ord = [order for order in self.orders if order['id'] == order_id]
                return jsonify({'Specific Order': ord})
            else:
                raise TypeError("Order_id should be a non negative integer")

    def post(self):
        """
        method to post an order
        """
        list_of_items = []
        list_of_items = request.json['list_item']
        usern = request.json['username']
        status = request.json['status']
        if usern.strip() == "":
            return jsonify({'error':'username is missing!'}), 403
        if status == "":
            return jsonify({'error':'Status is empty!'}), 403

        order = {"id":len(self.orders) + 1, "username":usern,
                 "list of items":list_of_items, "status":status}
        self.orders.append(order)
        return jsonify({'New_orders':order}), 201

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
