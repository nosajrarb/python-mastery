"""
10 threads each increment a shared counter 100,000 times. Run it first without a lock → you'll get a wrong result. Then add a Lock and get the correct 1,000,000.
"""

### Without lock

# import threading

# counter = 0
# threads = []

# def increment_counter():
#     global counter
#     for i in range(100000):
#         counter += 1
        
# for _ in range(10):
#     t = threading.Thread(target=increment_counter)
#     threads.append(t)
#     t.start()

# for thread in threads:
#     thread.join()
    
# print(counter)
    
import threading

counter = 0
lock = threading.Lock()
threads = []

def increment_counter():
    global counter
    for i in range(100000):
        with lock:
            counter += 1
        
for _ in range(100):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()
    
print(counter)  # always 10000000