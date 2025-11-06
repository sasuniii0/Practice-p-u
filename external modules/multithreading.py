import threading
import time

def worker(number):
    print(f"Worker {number} starting")
    time.sleep(2)
    print(f"Worker {number} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("All workers completed")

for t in threads:
    t.join()
print("All workers completed")