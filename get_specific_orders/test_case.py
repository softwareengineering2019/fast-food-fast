"""
import packages fromflask
"""
from flask import json
import pytest
from app import APP
from views import GetOrder

Order = GetOrder()
client = APP.test_client

def test_get_specific_order():
    """
    method to test a specific order.
    """
    myresult = client().get('/api/v1/orders/1')
    assert myresult.status_code == 200