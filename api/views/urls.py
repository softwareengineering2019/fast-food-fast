"""
This module assigns views to urls
"""
from api.controller.login import LoginUsers

class Urlz:
    """
    class that connects views with specific urls
    """
    @staticmethod
    def get_urls(app):
        """
        Method that connects views to specific urls urls
        """
        
        # Use registered user to login
        auth_users = LoginUsers.as_view('auth_users')
        app.add_url_rule('/api/v2/auth/login', view_func=auth_users, methods=['POST', ])
        