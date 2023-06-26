import string
from random import choice, randint
from models.car import Car

def generate_plate():
    type = randint(0, 2)

    if type == 0:
        left = ''.join([choice(string.ascii_uppercase) for i in range(3)])
        right = ''.join([choice(string.digits) for i in range(4)])
        return f'{left}-{right}'

    if type == 1:
        left = ''.join([choice(string.digits) for i in range(4)])
        right = ''.join([choice(string.ascii_uppercase) for i in range(2)])
        return f'{left}-{right}'

def generate_car(plate=None):
    plate = plate if plate else generate_plate()
    type = choice(['sedan', 'suv', 'hatchback', 'pickup'])
    color = choice(['white', 'black', 'blue', 'green', 'red', 'grey', 'silver', 'yellow'])
    lat, lon = 0, 0
    return Car(plate=plate, type=type, color=color, lat=lat, lon=lon)
