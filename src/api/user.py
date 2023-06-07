from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api


from models.car import Car
from models.user import User


class UserApi(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return render_template('test.html')

    # Corresponds to POST request
    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
