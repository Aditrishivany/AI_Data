import time
from multiprocessing import Pool
def analyze_logs(chunk):
    print("analysing chunk for {chunk}")
    time.sleep(2)
    return f"chunk {chunk} analyzed"
if __name__ == "__main__":
    chunks=[1,2,3,4]
    with Pool(4) as p:
        results=p.map(analyze_logs,chunks)
    print(results)