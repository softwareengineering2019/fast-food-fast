"""
    Module for making tests on the app for sign in
"""
import unittest
import json
import psycopg2
import os
import jwt
from run import APP
from api.controller.post_menu import PostMenu
from api.controller.get_menu import GetMenu
from api.controller.place_order import PlaceOrder
from api.controller.get_an_order_history import GetAnOrderHistory
from api.controller.fetch_specific_order import FetchSpecificOrder
from api.controller.update_order_status import UpdateOrderStatus
from api.controller.get_all_orders import GetAllOrders
from api.controller.update_user_roles import UpdateUserRoles


class TestViews(unittest.TestCase):
    """
    Class for making tests on sign in
    """

    def setUp(self):
        """
           Method for making the client object
        """
        self.client = APP.test_client
        APP.config['TESTING'] = True
        self.app = APP


    def test_place_an__order(self):
        """
            Method for testing to place an order
        """
        result = self.client().post('/api/v2/users/orders')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 401)
        self.assertIsInstance(respond, dict)
   

    def test_get_menu(self):
        """
            Method for testing to get the menu
        """
        result = self.client().get('/api/v2/menu')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Available Menu', respond)
        self.assertIsInstance(respond, dict)

    def test_adding_an_item_on_menu(self):
        """
            Method for testing to add an item on to the menu by admin
        """
        result = self.client().post('/api/v2/menu')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 401)
        self.assertIsInstance(respond, dict)
    

    def test_updating_order_status(self):
        """
            Method for testing toupdate an order_status by admin
        """
       
        result = self.client().put('/api/v2/orders/1')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code,401)
        self.assertIsInstance(respond, dict, )
        
    
    # def test_fetch_all_orders(self):
    #     """
    #     Method for testing get all orders by the admin
    #     """
    #     result = self.client().get('/api/v2/orders/')
    #     respond = json.loads(result.data.decode("utf8"))
    #     self.assertEqual(result.status_code, 200)
    #     self.assertIn('Orders', respond)
    #     self.assertIsInstance(respond, dict)
    
    # def test_get_one_specific_order(self):
    #     """
    #         Method for testing to get only one specfic order by the admin
    #     """
    #     result = self.client().get('/api/v1/orders/1')
    #     result2 = self.client().get('/api/v1/orders/a')
    #     respond = json.loads(result.data.decode("utf8"))
    #     self.assertEqual(result.status_code, 200)
    #     self.assertEqual(result2.status_code, 404)
    #     self.assertIsInstance(respond, dict)

    # def test_get_order_for_specific_user(self):
    #     """
    #         Method for testing to get orders for a particular user
    #     """
    #     result = self.client().get('/api/v1/users/orders')
    #     respond = json.loads(result.data.decode("utf8"))
    #     self.assertEqual(result.status_code, 401)
    #     self.assertIsInstance(respond, dict)
     
    # def test_post_with_an_empty_fields(self):
    #     """
    #         Method for testing the post function for empty fields
    #     """
    #     result = self.client().post('/api/v2/users/orders',
    #                                 content_type="application/json",
    #                                 data=json.dumps(dict(item_id="")))        
        
    #     respond = json.loads(result.data.decode("utf8"))
    #     self.assertIn('Message', respond)        
    #     self.assertTrue(result.json["Message"])