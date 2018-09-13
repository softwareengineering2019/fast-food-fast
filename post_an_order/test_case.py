"""
import packages fromflask
"""
from flask import json
import pytest
from app import APP
from views import GetOrder

Order = GetOrder()
client = APP.test_client

def test_if_data_posted_is_in_form_of_json():
    """
    method to test whether data posted is in json format.
    """
    results = client().post('/api/v1/orders', content_type='application/json', data=json.dumps(
        {
            "username": "james", "list_item": 
            [{"item_id":1, "item_name":"Chicken", "rate":5, "quantity":2, "amount":5650}], "status": "Declined"
        }))  
    assert results.status_code == 201