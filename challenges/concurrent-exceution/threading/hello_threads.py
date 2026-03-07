"""
Create 5 threads. Each thread should print "Thread X started" and "Thread X finished" with a 1-second sleep in between.
"""

import threading
import time

threads = []

def f():
    print('Thread X started')
    time.sleep(5)
    print('Thread X finished')
    

for _ in range(5):
    t = threading.Thread(target=f)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()