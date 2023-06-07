from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO
from uuid import uuid4
from pymongo import MongoClient
from datetime import datetime
from flask_restful import Resource, Api

from models.car import Car
from models.user import User

from cache import update_car_cache


# Flask app initialization
app = Flask(__name__)

# A simple home page
@app.route('/home')
def home():
    return render_template('test.html')

# MongoDB initialization
from mongoengine import *
client = MongoClient('mongodb://mongo', 27017)
connect('cardetect', host="mongo", port=27017)


from redis import Redis
redis = Redis(host='redis', port=6379)


# REST API initialization
from api.user import UserApi
from api.car import CarApi
api = Api(app)
api.add_resource(UserApi, '/user')
api.add_resource(CarApi, '/car')



# WebSocket initialization
from flask_socketio import send, emit
socketio = SocketIO(app)

@socketio.on('user-connect')
def handle_client_connect(data):
    user = User(userId=data['userId'], lat=0.0, lon=0.0).save()
    emit('user-connect-ok', {  })
    print(f'User {data["userId"]} connected successfully.')


@socketio.on('user-update')
def handle_client_update(data):
    user = User.objects.get(userId=data['userId'])
    user.lat = data['lat']
    user.lon = data['lon']
    user.save()


@socketio.on('user-report')
def handle_client_report(data):
    emit('user-report-ack', {  })
    for plate in data['plates']:
        if plate == '':
            continue
        update_car_cache(redis, plate, data['lat'], data['lon'])



# Generate some random new cars
# Comment this out if you don't want to spawn new cars
from generators import generate_car
generate_car().save()


# App entry
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
