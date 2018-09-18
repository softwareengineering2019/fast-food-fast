"""
import packages from flask and 
"""
from flask import json
import pytest
from app import APP
from views import GetOrder

ORDER = GetOrder()
CLIENT = APP.test_client

def test_if_data_is_in_json():
    """
    method to test whether data is in json format.
    """
    results = CLIENT().post('/api/v1/orders', content_type='application/json', data=json.dumps(
        {
            "username": "james", "list_item":
            [{"item_id":1, "item_name":"Chicken", "rate":5, "quantity":2,
              "amount":5650}], "status": "Declined"}))
    assert results.status_code == 201
