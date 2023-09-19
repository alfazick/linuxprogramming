import json

def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config

config = read_config('config.json')
print(f"Environment: {config['environment']}")
print(f"Database host: {config['database']['host']}")
print(f"Database port: {config['database']['port']}")
