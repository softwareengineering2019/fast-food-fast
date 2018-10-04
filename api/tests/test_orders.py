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

    def test_updating_order_status(self):
        """
        Method for testing toupdate an order_status by admin
        """
       
        result = self.client().put('/api/v2/orders/1')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code,401)
        self.assertIsInstance(respond, dict, )
        
    