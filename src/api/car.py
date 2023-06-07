from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

from models.car import Car
from models.user import User

from cache import *


class CarApi(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        cache_from_db('ABC-1234')
        return render_template('test.html')

    # Corresponds to POST request
    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201

    def update(self):
        data = request.get_json()     # status code
        car = Car.objects.filter(plate=plate).first()
        car.lat = lat
        car.lon = lon
        car.last_recorded = datetime.now()
        car.save()
