import socket
import requests

REDIS_HOST = '18.191.206.43'

def helloWorld():
    r = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
    response_json = r.json()
    region = response_json.get('region')
    instance_id = response_json.get('instanceId')
    return 'Wello World, from node ' + instance_id
