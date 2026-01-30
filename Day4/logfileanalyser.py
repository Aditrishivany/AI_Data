import re

error_pattern = r"(error|failed|critical|exception|warning|denied)"
regex = re.compile(error_pattern, re.IGNORECASE)

with open("sample.log", "r") as f:
    for line in f:
        if regex.search(line):
            print("ERROR FOUND →", line.strip())
