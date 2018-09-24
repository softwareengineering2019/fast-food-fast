
"""
This module assigns views to urls
"""
from api.views import GetOrder

class GetUrls:
    """
    Method that views with urls
    """
    @staticmethod
    def fetch_urls(app):
        """
        Method that views  urls
        """
        orders_view = GetOrder.as_view('orders')
        app.add_url_rule('/api/v1/orders', view_func=orders_view,
                         defaults={'order_id': None}, methods=['GET'])
        app.add_url_rule('/api/v1/orders/<int:order_id>', view_func=orders_view, methods=['GET'])
        app.add_url_rule('/api/v1/orders', view_func=orders_view, methods=['POST'])
        app.add_url_rule('/api/v1/orders/<int:id>', view_func=orders_view, methods=['PUT'])
