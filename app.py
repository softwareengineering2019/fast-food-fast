# -*- coding: utf-8 -*-
"""
module for running the application
"""
from flask import Flask
from urls import GetUrls
APP = Flask(__name__)
APP.env = 'development'
APP.testing = True
GetUrls.fetch_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)
