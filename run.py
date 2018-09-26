"""import the flask name from the api folder"""
from api import APP
from api.urls import GetUrls
from flask import jsonify
"""
module for running the application
"""
APP.env = 'development'
APP.testing = True
GetUrls.fetch_urls(APP)

@APP.errorhandler(405)
def url_not_found(error):
    return jsonify({'message':'Requested method not allowed'}), 405

@APP.errorhandler(404)
def page_not_found(error):
    return jsonify({'message':'page not found, check the url'}), 404

@APP.errorhandler(500)
def internal_error(error):
    return "500 error"

if __name__ == '__main__':
    """ This keeps the serve running"""
    APP.run(debug=True)
    