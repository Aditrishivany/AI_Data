import time
from multiprocessing import Pool
def simulate_region(region):
    print(f"calculating weather sum for {region}")
    time.sleep(2)
    return f"region {region} weather sum calculated"
if __name__ == "__main__":
    regions = ["north", "south", "east", "west"]
    with Pool() as p:
        results = p.map(simulate_region, regions)
    print(results)