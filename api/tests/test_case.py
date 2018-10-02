import unittest
import json
from api.controller.login import LoginUsers
from api.controller.register import RegisterUsers
# from db_connection.create_tables import config

# from app.models.models import drop, initialize
from connect import APP


class LoginRegisterTestCase(unittest.TestCase):

    def setUp(self):
        self.client = APP.test_client(self)
        user={
        "name": "james",
        "email": "james@gmail.com",
        "phone":"0784909440",
        "password": "james"
        }

    def test_user_can_login(self):
        '''This tests whether a registered user can login'''
        result = self.client.post('/api/v2/auth/signup', data=json.dumps(self.user, content_type='application/json'))

        # result  = self.client.post(
            # '/api/v2/auth/login', data=json.dumps(self.data["login"]), content_type='application/json')
        self.assertEqual(result.status_code, 200)
        # self.assertTrue(b'Login successfull!', res.data)

    # def test_wrong_password(self):
    #     '''This tests whether a user cannot login with a wrong password'''
    #     result  = self.client.post(
    #         '/api/v2/auth/signup', data=json.dumps(self.data["user"]), content_type='application/json')
    #     result  = self.client.post(
    #         '/api/v2/auth/login', data=json.dumps(self.data["wrong_password"]), content_type='application/json')
    #     self.assertEqual(res.status_code, 401)
    #     self.assertTrue(b'password incorrect!', res.data)

    # def test_unknown_user_cannot_login(self):
    #     '''This tests whether an unknown user cannot login'''
    #     result  = self.client.post(
    #         '/api/v2/auth/login', data=json.dumps(self.data["unknown"]), content_type='application/json')
    #     self.assertEqual(res.status_code, 400)
    #     self.assertTrue(b'User does not exist!', res.data)