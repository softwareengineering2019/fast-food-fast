"""
    Module for making tests on the app for sign up
"""
import unittest
import json
import psycopg2
from run import APP
from api.controller.login import LoginUsers
from api.controller.register import RegisterUsers
import os

class TestViews(unittest.TestCase):
    """"
        Class for testing  signing up
        params: unittest.testCase
    """

    def setUp(self):
        """
           Method for making the client object
        """
        # self.client = APP.test_client
        APP.config['TESTING'] = True
        self.app = APP
        self.client = APP.test_client
        # GetAllOrder.__init__(APP) 
    def test_sign(self):
        """
            Method for testing the post function which adds new user
        """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(name="moses", email="moses@gmail.com",phone="0764324040",
                                                         password="moses")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["message"])

    