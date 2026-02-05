# import threading
# def say_hello():
#     print("Hello from thread")
# t = threading.Thread(target=say_hello)
# t.start()
# t.join()
# print("task finished")


# import time
# def task():
#     print("task started")
#     time.sleep(2)
#     print("task completed")
# task()
# print("program finished")


# import threading
# def greet(name):
#     print(f"hello,{name}!")
# t=threading.Thread(target=greet,args=("divya"))
# t.start()


# import time
# def greet(name):
#     time.sleep(3)
#     print("hello",name)
# name=input("enter name")
# greet(name)


# def worker(num):
#     print(f"worker {num} is running")
#     time.sleep(1)
#     print(f"worker {num} is finished")
# for i in range(5):
#     t= threading.Thread(target=worker,args=(i,))
#     t.start()


# import urllib.request
# import threading
# import time
# def download_file():
#     url="http://127.0.0.1:5500/Day7/Threading/jk.txt"
#     filename='download_test.txt'
#     print("starting download...")
#     urllib.request.urlretrieve(url,filename)
#     time.sleep(2)
#     print("download completed.")
# t=threading.Thread(target=download_file)
# t.start()
# print("main program continues to run...")


import urllib.request
import time
def download_file():
    url = "http://127.0.0.1:5500/Day7/Threading/jk.txt"
    filename = 'download_test.txt'
    print("starting download...")
    urllib.request.urlretrieve(url, filename)
    time.sleep(2)
    print("download completed.")
download_file()
print("main program continues to run...")
