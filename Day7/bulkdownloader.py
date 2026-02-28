import threading
import urllib.request

def download(url, filename):
    print("Downloading:", filename)
    urllib.request.urlretrieve(url, filename)
    print("Done:", filename)

files = [
    ("https://httpbin.org/encoding/utf8", "sample1.txt"),
    ("https://raw.githubusercontent.com/vinta/awesome-python/master/README.md", "sample2.md"),
    ("https://www.google.com/robots.txt", "robots.txt"),
    ("https://httpbin.org/uuid", "uuid.json")
]

threads = []
for url, name in files:
    t = threading.Thread(target=download, args=(url, name))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All downloads complete")
