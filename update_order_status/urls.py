
"""
This module assigns views to urls
"""
from views import GetOrder

class GetUrls:
    """
    Method that views with urls
    """
    @staticmethod
    def fetch_urls(app):
        """
        Method that views with urls
        """
        orders_view = GetOrder.as_view('orders')
        app.add_url_rule('/api/v1/orders/<int:id>', view_func=orders_view, methods=['PUT'])
