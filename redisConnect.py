from redis import Redis
from rq import Queue
import tasks
import time

c = Redis(host=tasks.REDIS_HOST)
q = Queue(connection=c)

t0 = time.time()
jobs = []
for i in range(10):
    jobs.append(q.enqueue(tasks.helloWorld))
while any(not job.is_finished for job in jobs):

    time.sleep(2)
t1 = time.time()
for job in jobs:
    print(job.return_value)
print(t1 - t0)