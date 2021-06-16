import redis


def save(username, record):
    redis.set(username, record, ex=604800)


def get_record(username):
    return redis.get(username)


redis = redis.Redis(host='localhost', port='6379')
