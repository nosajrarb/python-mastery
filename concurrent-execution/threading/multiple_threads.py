import threading
import time

def download_file(download_time):
    print("Started download")
    time.sleep(download_time) #secs
    print("Finished download")
    
threads = []

for _ in range(10):
    t = threading.Thread(target=download_file, args=[1.5])
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()

print('Finished dowloading all the files') # all files downloaded in 1.5 seconds
