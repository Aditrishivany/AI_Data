# Speed Runner (PY2_SPEED_RUNNER_OPTIMIZER)

This project compares baseline (single-thread) file processing with an optimized
(threaded) version and measures speed improvement.

## How to Generate 200 Random Files
python generate_bulk_files.py

This will generate:
bulk_data/data_file_1.txt ... data_file_200.txt

## How to Run Performance Test
python speed_runner.py

This will generate:
output/performance_results.json

## Why Threading?
Threading is chosen because reading 200+ text files is an **I/O-bound** task.
Threading improves speed by overlapping file reads, while multiprocessing adds
overhead and provides no advantage for this workload.