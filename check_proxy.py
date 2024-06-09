import threading
import queue

import requests

q = queue.Queue()
valid_proxies = []

# Read proxies from file and add them to the queue
with open("proxy_list.txt", "r") as f:
    proxies = f.read().splitlines()  # Use splitlines to avoid empty strings
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            url = "http://www.ipinfo.io/json"
            res = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
            if res.status_code == 200:
                valid_proxies.append(proxy)
                print(f"Valid proxy: {proxy}")
        except: 
            continue

# Start threads to check proxies
threads = []
for _ in range(10):
    t = threading.Thread(target=check_proxies)
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Valid proxies: {valid_proxies}")
