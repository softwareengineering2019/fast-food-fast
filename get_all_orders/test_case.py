"""
import packages fromflask
"""
from flask import json
import pytest
from app import APP
from views import GetOrder

Order = GetOrder()
client = APP.test_client

def test_get_orders():
    """
    method to test all orders.
    """
    result = client().get('/api/v1/orders')
    assert result.status_code == 200