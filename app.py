from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO
from uuid import uuid4
from pymongo import MongoClient
from datetime import datetime
from flask_restful import Resource, Api

from models.car import Car
from models.user import User



# Flask app initialization
app = Flask(__name__)


# MongoDB initialization
from mongoengine import *
client = MongoClient('localhost', 27017)
connect('cardetect')


# REDIS cache server initialization
from flask_redis import FlaskRedis
REDIS_URL = "redis://localhost:6379/0"
redis = FlaskRedis()
redis.init_app(app)


# REST API initialization
from api.user import UserApi
from api.car import CarApi
api = Api(app)
api.add_resource(UserApi, '/user')
api.add_resource(CarApi, '/car')


# A simple home page
@app.route('/home')
def home():
    return render_template('test.html')



# WebSocket initialization
import websocket
socketio = SocketIO(app)



# [TEST] This creates a car in the DB
# car = Car(plate='ABC-1234', type='sedan', color='white', lat=22.674341, lon=120.375476)
# car.save()


# The cache event loop
from cache import _cache_loop_
from time import sleep
from threading import Thread
def periodic():
    while True:
        _cache_loop_(redis)
        sleep(1)

daemon = Thread(target=periodic, args=(), daemon=True, name='_cache_loop_')
daemon.start()


# App entry
if __name__ == '__main__':
    socketio.run(app, debug=True)
