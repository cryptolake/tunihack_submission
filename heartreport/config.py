#!/usr/bin/python3
"""Default configuration settings."""
from os import environ
from flask_mongoengine import MongoEngine
from flask import Flask

DB_HOST = environ.get("DB_HOST")
MONGODB_SETTINGS = {
        "host": DB_HOST}

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
db = MongoEngine(app)
