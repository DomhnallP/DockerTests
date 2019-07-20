#
from concurrent.futures import ThreadPoolExecutor
import docker
import random
import time
def fun(message, client):
    container = client.containers.run("md5summer", environment=["var=%s" % message], detach=True)
    logs = container.logs()
    
    for line in container.logs(stream=True):
        print (line.strip())

client1 = docker.DockerClient(base_url='tcp://52.14.62.247:4243',  tls=False)
client2 = docker.DockerClient(base_url='tcp://3.16.163.113:4243',  tls=False)
messages= ["c4ca4238a0b923820dcc509a6f75849b",
            "c4ca4238a0b923820dcc509a6f758491",
            "c4ca4238a0b923820dcc509a6f75849c",
            "c4ca4238a0b923820dcc509a6f75849d",
            "c4ca4238a0b923820dcc509a6f75849b",
            "c4ca4238a0b923820dcc509a6f758491",
            "c4ca4238a0b923820dcc509a6f75849c",
            "c4ca4238a0b923820dcc509a6f75849d",
            "c4ca4238a0b923820dcc509a6f75849b",
            "c4ca4238a0b923820dcc509a6f758491",
            "c4ca4238a0b923820dcc509a6f75849c",
            "c4ca4238a0b923820dcc509a6f75849d"]

pool = ThreadPoolExecutor(10)
clients = [client1, client2]
i = 0
t1 = time.time()
futures = []
for my_message in messages:
    future = pool.submit(fun, (my_message), clients[i])
    futures.append(future)
    i+=1
    if(i>=len(clients)): i=0

while any(not future.done() for future in futures):
        time.sleep(0.01)

t2 = time.time()
print("Porcessing time: " + str(t2 - t1) + " seconds")