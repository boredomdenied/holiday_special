import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())
root@redis-queue-server:~/app# cat main.py 
from rq import Connection, Queue, Retry
from redis import Redis
from count_words import count_words_at_url # added import!
import time

redis_conn = Redis()
q = Queue(connection=redis_conn)
job = q.enqueue(count_words_at_url,'http://nvie.com', retry=Retry(max=3, interval=[3,6,12]))
print(job)
time.sleep(2)
print(job.result)
