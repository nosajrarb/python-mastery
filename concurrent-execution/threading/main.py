import threading 
import time

def download_file():
    print("downloading file")
    time.sleep(5)
    print("finished downloading")

def read_file():
    print("reading the file")
    time.sleep(3)
    print("finished reading the file")

#Without any threading - takes 8 secs
# download_file()
# read_file()

#With threading - takes 5 seconds
thread_1 = threading.Thread(target = download_file)
thread_2 = threading.Thread(target = read_file)

thread_1.start()
thread_2.start()

print(threading.active_count())
# threading.active_count() returns the total number of active threads
# here 3 threads are active (thread1, thread2, main program thread)j

#without .join() the main program ain't wait for the threads to finish
thread_1.join()
thread_2.join()

print("main program")