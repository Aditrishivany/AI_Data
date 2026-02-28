import csv
import psutil

cpu = psutil.cpu_percent()

memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

with open("system_report.csv", "a", newline="") as f:
    w = csv.writer(f)
    w.writerow([cpu, memory.used, memory.free, disk.used, disk.free])

with open("outputs.txt", "a") as out:
    out.write(f"CPU: {cpu}% | Mem Used: {memory.used} | Mem Free: {memory.free} | Disk Used: {disk.used} | Disk Free: {disk.free}\n")
