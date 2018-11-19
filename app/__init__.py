import os
from flask import Flask, jsonify
import psycopg2
from flask_bcrypt import Bcrypt

# Initialize application
app = Flask(__name__)

# Initialize Bcrypt
app.config['SECRET_KEY'] = '12345678'
bcrypt = Bcrypt(app)

conn = psycopg2.connect(database = "fastfoodfast",user="postgres", password="james",host="localhost",port=5432)

# Import the application views
from app.views.user_views import GetAuthUrls
GetAuthUrls.fetch_urls(app)