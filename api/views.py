""" 
module that defines views
 """
from flask import jsonify, request
from flask.views import MethodView


class GetOrder(MethodView):
    """
    class that  defines views
    """
    orders = []
    
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
        rate = list_of_items[0]['rate'] 
        quantity = list_of_items[0]['quantity']
        amount = list_of_items[0]['amount'] 
        if rate == "" or quantity == "" or amount=="":
            return jsonify({error}), 400
        if  list_of_items[0]['item_name'] == "":
            return jsonify({'error':'item name is missing!'}), 403
        usern = request.json['username']
        status = request.json['status']
        if usern.strip() == "":
            return jsonify({'error':'username is missing, please fill it!'}), 403
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
        elif id == "":
            return ({error}), 404
        else:
            return({error}), 405
 