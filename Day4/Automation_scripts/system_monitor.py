import psutil

cpu = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()
mem_total = memory.total // (1024**3)
mem_used = memory.used // (1024**3)
mem_free = memory.available // (1024**3)

disk = psutil.disk_usage("/")
disk_total = disk.total // (1024**3)
disk_used = disk.used // (1024**3)
disk_free = disk.free // (1024**3)

with open("outputs.txt", "a") as out:
    out.write("=== System Resource Report ===\n")
    out.write(f"CPU Usage: {cpu}%\n")
    out.write(f"Memory Total: {mem_total} GB\n")
    out.write(f"Memory Used: {mem_used} GB\n")
    out.write(f"Memory Free: {mem_free} GB\n")
    out.write(f"Disk Total: {disk_total} GB\n")
    out.write(f"Disk Used: {disk_used} GB\n")
    out.write(f"Disk Free: {disk_free} GB\n\n")

print("System resource report written to outputs.txt")
