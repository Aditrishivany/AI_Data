# from multiprocessing import Process
# def worker():
#     print("worker is running")

# if __name__ == "__main__":
#     p=Process(target=worker)
#     p.start()
#     p.join()
#     print("main process finished")


# from multiprocessing import Pool
# import time
# def square(n):
#     return n * n
# if __name__ == "__main__":
#     numbers = [10*7, 102, 103, 104, 10*5]
#     start = time.time()
#     with Pool() as p:
#         p.map(square, numbers)
#     print(time.time() - start)


