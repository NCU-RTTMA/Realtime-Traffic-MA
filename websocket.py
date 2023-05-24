# WebSocket event handlers

from flask_socketio import send, emit
from random import choice
from app import socketio

from models.car import Car
from models.user import User


@socketio.on('Client-connect')
def initialize_connection(data):
    user = User(ClientId=data['ClientId'], lat=0.0, lon=0.0).save()
    print(f'User {data["ClientId"]} connected successfully.')


@socketio.on('event-flag')
def handle_event_flag(data):
    print(f'Report received from user {data["ClientId"]}')

    for p in data['plates']:
        if Car.objects.filter(plate=p).count() > 0:
            update_car(p, data['lat'], data['lon'])
        else:
            add_car(p, 'sedan', 'white', data['lat'], data['lon'])

    events = identify_events(data['lat'], data['lon'], data['plates'])

    # Analyze identified events
    for e in events:
        if e['type'] == 'dangerous_driving':
            for plate in e['plates']:
                records[plate] = {
                    'count': records[plate]['count']+1 if plate in records else 1,
                    'lat': e['lat'],
                    'lon': e['lon'],
                }

                # Broadcast alert for dangerous cars
                if records[plate]['count'] >= 3:
                    emit('danger', { 'plate': plate, 'lat': records[plate]['lat'], 'lon': records[plate]['lon'] }, broadcast=True)

        # if e['type'] == 'accident':
        #     emit('accident', {  }, broadcast=True)


@socketio.on('Client-update')
def handle_Client_update(data):
    Client = User.objects.get(ClientId=data['ClientId'])
    Client.lat = data['lat']
    Client.lon = data['lon']
    Client.save()
    # print(f'Updating data for user {Client["ClientId"]}')
