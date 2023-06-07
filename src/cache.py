from models.car import Car
from datetime import datetime


# In-memory cache
global_cache = { }


# This is called by the system every second
def _cache_loop_(redis):
    for plate, cache in global_cache.items():

        # If timed out, update to DB and remove from cache
        if cache['ttl'] < 0:

            # Write cache to persistent DB
            car = Car.objects.get(plate=plate)
            car.lat = cache['lat']
            car.lon = cache['lon']
            car.last_recorded = datetime.now()
            car.vio_count = cache['vio_count']
            car.danger_count = cache['danger_count']
            car.save()

            # Remove from cache
            redis.delete(plate)
            del global_cache[plate]
            print(f'Removed {plate} from cache and updated DB. (TTL timeout)')
            return

        # Subtract TTL of the cache, otherwise
        cache['ttl'] -= 1
        redis.hmset(cache['plate'], cache)


# Copy from DB to cache
def load_cache_from_db(plate):
    # car = Car.objects.filter(plate=plate).first()

    # Create a new cache
    global_cache[plate] = {
        'plate': plate,
        'type': 'suv',
        'color': 'white',
        'lat': 30,
        'lon': 60,
        'last_recorded': str(datetime.now()),
        'vio_count': 0,
        'danger_count': 0,
        'ttl': 10,
    }
    print(f'Loaded car {plate} from DB to cache.')


# Update a particular cache
def update_car_cache(plate, lat, lon):
    if not plate in global_cache:
        load_cache_from_db(plate)
    cache = global_cache[plate]
    cache['lat'] = lat
    cache['lon'] = lon
    cache['last_recorded'] = str(datetime.now())


# TEST
# update_car_cache('ABC-1234', 60, 39.5)
