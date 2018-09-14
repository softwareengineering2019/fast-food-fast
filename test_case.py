"""
import packages fromflask
"""
from flask import json
import pytest
from app import APP
from views import GetOrder

ORDER = GetOrder()
CLIENT = APP.test_client

def test_get_orders():
    """
    method to test all orders.
    """
    result = CLIENT().get('/api/v1/orders')
    assert result.status_code == 200

def test_get_specific_order():
    """
    method to test a specific order.
    """
    myresult = CLIENT().get('/api/v1/orders/1')
    assert myresult.status_code == 200

def test_if_data_posted_is_in_form_of_json():
    """
    method to test whether data posted is in json format.
    """
    results = CLIENT().post('/api/v1/orders', content_type='application/json', data=json.dumps(
        {
            "username": "james", "list_item":
            [{"item_id":1, "item_name":"Chicken", "rate":5, "quantity":2,
              "amount":5650}], "status": "Declined"}))
    assert results.status_code == 201

def test_update_order():
    """
    method to test an update on a specific order.
    """
    results = CLIENT().put('/api/v1/orders/2', content_type='application/json',
                           data=json.dumps({"status": "decline"}))
    assert results.status_code == 200

def test_if_parameter_passed_to_function_is_a_string():
    """
    method to whether the parameter passed is a string.
    """
    with pytest.raises(TypeError):
        ORDER.get("andela")
