from time import time
from threading import Thread
from urllib import request

def task_io():
    with request.urlopen('http://python.org/') as response:
        print(response.status)

if __name__=="__main__":
    loop = 4
    
    time_start = time()
    for _ in range(loop):
        task_io()
    time_end = round((time() - time_start) * 1000, 1)
    print(f"tempo: {time_end}")

    time_start, threads = time(), []
    for _ in range(loop):
        threads.append(Thread(target=task_io))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    time_end = round((time() - time_start) * 1000, 1)
    print(f"tempo: {time_end}")
