import redis

redis_client = redis.Redis(
    host="redis-15228.c257.us-east-1-3.ec2.redns.redis-cloud.com:15228",
    port=15228,
    password="uLGthfUGBWlDbLPsK7Ygj7AeWCstJmmX",
)

try:
    connection_status = redis_client.ping()
    if connection_status:
        print("Connected to Redis!")
    else:
        print("The connection to Redis was unsuccessful!")
except redis.ConnectionError as ex:
    print("An error ocurred while connecting to Redis: ", ex)


def store_data(key, value, time_to_live=None):
    try:
        if time_to_live is None:
            redis_client.set(key, value)
            print(f"Key '{key}' created with value '{value}'.")
        else:
            redis_client.setex(key, time_to_live, value)
            print(f"Key '{key}' created with value '{value}' and a ttl of {time_to_live}.")
    except redis.RedisError as error:
        print(f"An error ocurred while storing data in Redis: {error}")


store_data("full_name", "John Doe")
store_data("important_key", "Important Value!", time_to_live=100)


def check_key(key):
    try:
        key_exists = redis_client.exists(key)
        if key_exists:
            print(f"Key '{key}' exists in Redis.")
            ttl = redis_client.ttl(key)
            if ttl:
                print(f"Key '{key}' has a TTL of {ttl}.")

            return True, ttl

        print(f"Key '{key}' does not exist in Redis.")
        return False, None
    except redis.RedisError as error:
        print(f"An error ocurred while checking a key in Redis: {error}")
        return False, None
    
key_exists, ttl = check_key("important_key")
print("Key exists:", key_exists)
print("TTL:", ttl)


def get_data(key):
    try:
        output = redis_client.get(key)
        if output is not None:
            result = output.decode("utf-8")
            print(f"Value '{result}' found for key '{key}'.")
            return result
        else:
            print(f"No value found for key {key}.")
            return None
    except redis.RedisError as error:
        print(f"An error ocurred while retrieving data from Redis: {error}")

value = get_data("full_name")
print("Value:", value)


def delete_data(key):
    try:
        output = redis_client.delete(key)
        if output > 0:
            print(f"Key '{key}' and its value have been deleted.")
        else:
            print(f"Key '{key}' not found.")

        return output == 1
    except redis.RedisError as error:
        print(f"An error ocurred while deleting data from Redis: {error}")
        return False
result = delete_data("full_name")
print("Result:", result)

