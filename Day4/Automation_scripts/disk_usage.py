import shutil

total, used, free = shutil.disk_usage("/")

with open("outputs.txt", "a") as out:
    out.write("=== Disk Usage Report ===\n")
    out.write(f"Total: {total // (1024**3)} GB\n")
    out.write(f"Used: {used // (1024**3)} GB\n")
    out.write(f"Free: {free // (1024**3)} GB\n\n")

print("Disk usage written to outputs.txt")
