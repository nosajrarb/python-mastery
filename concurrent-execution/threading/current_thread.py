import threading
import time

print(threading.current_thread()) # Main thread 
print(threading.active_count()) # 1 active thread (main thread)

def download_file():
    print("Downloading the file")
    time.sleep(5)
    print(threading.active_count()) # 3 active threads (main thread, thread_1, thread_2)
    print(threading.current_thread())
    print("Finished downloading the file")
    
def read_file():
    print("Reading the file")
    time.sleep(7)
    print(threading.active_count()) # 2 active threads (main thread, thread_2)
    print(threading.current_thread())
    print("Finished reading the file")
    
thread_1 = threading.Thread(target= download_file)
thread_2 = threading.Thread(target= read_file)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

"""
t=0s   main thread runs → prints MainThread, prints 1
t=0s   thread_1 starts  → prints "Downloading the file" → sleeps 5s
t=0s   thread_2 starts  → prints "Reading the file"     → sleeps 7s

t=5s   thread_1 wakes up → prints 3 active count (main+t1+t2 all still alive)
                         → prints Thread-1
                         → prints "Finished downloading"
                         → thread_1 DIES

t=7s   thread_2 wakes up → prints 2 active count (main+t2, thread_1 is dead)
                         → prints Thread-2
                         → prints "Finished reading"
"""
