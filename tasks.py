import socket
REDIS_HOST = '18.188.58.132'

def helloWorld():
    return 'hello World, from node ' + socket.gethostname()
