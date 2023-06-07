from models.car import Car
from datetime import datetime


# Copy from DB to cache
def load_cache_from_db(plate):
    car = Car.objects.filter(plate=plate).first()

    return {
        'plate': plate,
        'type': car.type,
        'color': car.color,
        'lat': car.lat,
        'lon': car.lon,
        'last_recorded': str(datetime.now()),
        'vio_count': car.vio_count,
        'danger_count': car.danger_count,
    }


# Update a particular cache
def update_car_cache(redis, plate, lat, lon):
    cache = redis.hgetall(plate) if redis.exists(plate) else load_cache_from_db(plate)
    cache['lat'] = lat
    cache['lon'] = lon
    cache['last_recorded'] = str(datetime.now())
    redis.hmset(plate, cache)
    redis.expire(plate, 10)
