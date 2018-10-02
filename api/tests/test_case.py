"""
    Module for making tests on the app for sign up
"""
import unittest
import json
import psycopg2
import os, jwt
from run import APP
from api.controller.login import LoginUsers
from api.controller.register import RegisterUsers


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

    def test_sign_with_other_criedientials(self):
        """
            Method for testing the post function for posting a user with other signup credientials
        """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(name  = "james", email = "jjamess@gmail.com.com",phone="0786543212", password = "jameds")))
        
        self.assertEqual(result.status_code, 201)
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)        
        self.assertTrue(result.json['message'])

    # def test_login(self):
    #     """
    #         Method for testing the  logging method for a user with only a user_name
    #     """
    #     result = self.client().post('/api/v2/auth/login',
    #                                 content_type="application/json",
    #                                 data=json.dumps(dict(name="moses", password="moses")))
    #     respond = json.loads(result.data.decode("utf8"))
    #     self.assertIn('message', respond)
    #     self.assertIsInstance(respond, dict)
    #     self.assertEqual(result.status_code, 400)
    #     self.assertTrue(result.json["message"])


    # def test_sign_with_an_empty_name(self):
    #     """
    #         Method for testing the post function for testing user with empty name
    #     """
    #     result = self.client().post('/api/v2/auth/signup',
    #                                 content_type="application/json",
    #                                 data=json.dumps(dict(name="moses", email="mosesgmail.com",phone="0785432317",
    #                                                         password="moses")))        
        
    #     respond = json.loads(result.data.decode("utf8"))
    #     self.assertIn('name', respond)        
    #     self.assertTrue(result.json["name"])