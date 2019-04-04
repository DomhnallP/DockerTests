import socket
import requests

REDIS_HOST = '3.17.190.7'

def helloWorld():
    r = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
    response_json = r.json()
    region = response_json.get('region')
    instance_id = response_json.get('instanceId')
    return 'Wello World, from node ' + instance_id
