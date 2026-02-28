import os
import time
import json
from concurrent.futures import ThreadPoolExecutor

# -------------------------------------------------
# Decorator for measuring execution time
# -------------------------------------------------
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start
    return wrapper

# -------------------------------------------------
# Generator to read files line-by-line
# -------------------------------------------------
def file_reader(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            yield line

# -------------------------------------------------
# Process single file (count lines)
# -------------------------------------------------
def process_file(filepath):
    count = 0
    for _ in file_reader(filepath):
        count += 1
    return count

# -------------------------------------------------
# Baseline single-thread processing
# -------------------------------------------------
@time_it
def baseline_process(folder):
    counts = []
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            counts.append(process_file(filepath))
    return counts

# -------------------------------------------------
# Optimized multi-thread processing
# -------------------------------------------------
@time_it
def optimized_process(folder):
    files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]

    counts = []
    with ThreadPoolExecutor() as executor:
        for result in executor.map(process_file, files):
            counts.append(result)

    return counts

# -------------------------------------------------
# Main controller
# -------------------------------------------------
def run_speed_test(folder, output_file):
    # Run baseline
    _, baseline_time = baseline_process(folder)

    # Run optimized
    _, optimized_time = optimized_process(folder)

    files_processed = len(os.listdir(folder))
    speedup = baseline_time / optimized_time if optimized_time > 0 else 0

    results = {
        "filesProcessed": int(files_processed),
        "baselineSeconds": float(round(baseline_time, 5)),
        "optimizedSeconds": float(round(optimized_time, 5)),
        "speedupX": float(round(speedup, 3)),
        "methodUsed": "threading"
    }

    # Save to output JSON
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print("✔ Performance Test Complete!")
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    run_speed_test("bulk_data", "output/performance_results.json")