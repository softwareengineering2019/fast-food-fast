"""
import packages fromflask
"""
from flask import json
import pytest
from app import APP
from views import GetOrder

ORDER = GetOrder()
CLIENT = APP.test_client

def test_update_order():
    """
    method to test an update on a specific order.
    """
    results = CLIENT().put('/api/v1/orders/2', content_type='application/json',
                           data=json.dumps({"status": "decline"}))
    assert results.status_code == 200
    
