import time
import threading
from multiprocessing import Process, cpu_count

def heavy_calculation(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

def normal_execution():
    print("\n--- Normal Execution Started ---")
    start = time.time()

    heavy_calculation(10_000_000)
    heavy_calculation(10_000_000)

    end = time.time()
    print("Normal Execution Time:", end - start)

def threading_execution():
    print("\n--- Threading Execution Started ---")
    start = time.time()

    t1 = threading.Thread(target=heavy_calculation, args=(10_000_000,))
    t2 = threading.Thread(target=heavy_calculation, args=(10_000_000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()
    print("Threading Execution Time:", end - start)

def multiprocessing_execution():
    print("\n--- Multiprocessing Execution Started ---")
    start = time.time()

    p1 = Process(target=heavy_calculation, args=(10_000_000,))
    p2 = Process(target=heavy_calculation, args=(10_000_000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print("Multiprocessing Execution Time:", end - start)

if __name__ == "__main__":
    print("CPU Count:", cpu_count())

    normal_execution()
    threading_execution()
    multiprocessing_execution()