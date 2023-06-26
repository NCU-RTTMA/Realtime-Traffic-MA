from models.car import Car
from datetime import datetime
from flask_socketio import send, emit

from generators import generate_car

def create_new_car(plate):
    car = generate_car(plate).save()
    return car

# Copy from DB to cache
def load_cache_from_db(plate):
    car = Car.objects.filter(plate=plate).first()
    if car == None:
        car = create_new_car(plate)
    return car.to_json()


# Update a particular cache
def update_car_cache(redis, plate, lat, lon):
    cache = redis.hgetall(plate) if redis.exists(plate) else load_cache_from_db(plate)

    if int(cache['vio_count']) > 5 or int(cache['danger_count']) > 2:
        emit('danger-alert', {
            'plate': plate,
            'lat': float(cache['lat']),
            'lon': float(cache['lon']),
        }, broadcast=True)

    cache['lat'] = float(lat)
    cache['lon'] = float(lon)
    cache['last_recorded'] = str(datetime.now())
    redis.hmset(plate, cache)
    redis.expire(plate, 10)



# This is called by the system every second
def _cache_loop_(redis):
    plates = redis.keys("*")
    for plate in plates:
        # if not len(plate) in [7,8] or not '-' in plate:
        #     continue
        if redis.ttl(plate) <= 0:
            # mongodb.print(plate)
            cache = redis.hgetall(plate)

            if int(cache['vio_count']) > 5 or int(cache['danger_count']) > 0:
                emit('danger-alert', {
                    'plate': plate,
                    'lat': float(cache['lat']),
                    'lon': float(cache['lon']),
                })


            car = Car.objects.get(plate=plate)
            car.lat = float(cache['lat'])
            car.lon = float(cache['lon'])
            car.last_recorded = datetime.now()
            car.vio_count = int(cache['vio_count'])
            car.danger_count = int(cache['danger_count'])
            car.save()
