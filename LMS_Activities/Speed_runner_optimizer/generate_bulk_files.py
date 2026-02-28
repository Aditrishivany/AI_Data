import os
import random
import string

def generate_random_line(min_len=20, max_len=100):
    """Generate a random text line."""
    length = random.randint(min_len, max_len)
    return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))

def generate_random_file(filepath, min_lines=20, max_lines=200):
    """Generate a file with random number of lines."""
    lines = random.randint(min_lines, max_lines)
    with open(filepath, "w", encoding="utf-8") as f:
        for _ in range(lines):
            f.write(generate_random_line() + "\n")

def generate_bulk_files(folder="bulk_data", count=200):
    os.makedirs(folder, exist_ok=True)

    print(f"Generating {count} random files...")

    for i in range(1, count + 1):
        filename = f"data_file_{i}.txt"
        filepath = os.path.join(folder, filename)
        generate_random_file(filepath)

    print(f"✔ Successfully generated {count} random test files in '{folder}'")

if __name__ == "__main__":
    generate_bulk_files()