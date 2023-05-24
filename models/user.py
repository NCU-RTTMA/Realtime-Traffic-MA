# Persistent User table (MongoDB)

from mongoengine import *
from datetime import datetime

class User(Document):
    userId = StringField(primary_key=True)
    lat = FloatField(required=True)
    lon = FloatField(required=True)
