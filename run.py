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
def method_not_allowed(error):
    return jsonify({'message':'Requested method not allowed or specify an integer id to fetch the exact order for an update'}), 405

@APP.errorhandler(400)
def field_missing(error):
    return jsonify({'message':'One of the required fields is empty, please fill all the fields'}), 400

@APP.errorhandler(404)
def page_not_found(error):
    return jsonify({'message':'page not found or input an integer id'}), 404
    

if __name__ == '__main__':
    """ This keeps the serve running"""
    APP.run(debug=True)
    