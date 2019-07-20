from redis import Redis
from rq import Queue
import tasks
import time

c = Redis(host=tasks.REDIS_HOST)
q = Queue(connection=c)

t0 = time.time()
jobs = []
for i in range(100):
    jobs.append(q.enqueue(tasks.helloWorld))

print("all jobs loaded")
while any(!job.is_finished for job in jobs):
    print("computing")
    for job in jobs:
        if job.is_finished:
            print(job.return_value +  " - job number: " + str(jobs.index(job)))
            jobs.pop(jobs.index(job))       
    
t1 = time.time()
print(t1 - t0)