"""import the flask name from the api folder"""
from api import APP
from api.urls import GetUrls
"""
module for running the application
"""
APP.env = 'development'
APP.testing = True
GetUrls.fetch_urls(APP)

if __name__ == '__main__':
    """ This keeps the serve running"""
    APP.run(debug=True)
    