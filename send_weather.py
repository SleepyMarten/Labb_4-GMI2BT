from random import randint
import requests,json

url = 'http://localhost:80/post_data'

def post_json():
    #Creating weather information for the server.
    data = {
    'sensor': 'BMO280',
    'temp': randint(-20, 32),
    'humidity': randint(10, 90),
    'pressure': randint(100, 2000),
    }
    headers = {'Content-Type': 'application/json'}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.status_code)

post_json()