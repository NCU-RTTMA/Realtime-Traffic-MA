# Persistent Car table (MongoDB)

from mongoengine import *
from datetime import datetime

class Car(Document):
    plate = StringField(unique=False)
    type = StringField(max_length=10, required=True)
    color = StringField(max_length=10, required=True)
    lat = FloatField(required=True)
    lon = FloatField(required=True)
    last_recorded = DateTimeField(default=datetime.utcnow)
    vio_count = IntField(required=True, default=0)
    danger_count = IntField(required=True, default=0)

    def to_json(self):
        return {
            'plate': self.plate,
            'type': self.type,
            'color': self.color,
            'lat': self.lat,
            'lon': self.lon,
            'last_recorded': self.last_recorded,
            'vio_count': self.vio_count,
            'danger_count': self.danger_count,
        }
