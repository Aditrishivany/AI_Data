import shutil
import datetime
import time
import os

src = r"D:\Users\Admin\Desktop\AI&Data\Day3"
backup_root = r"D:\Users\Admin\Desktop\AI&Data\backups"
os.makedirs(backup_root, exist_ok=True)

print("Waiting for 11:28 AM to run backup...")

while True:
    now = datetime.datetime.now()

    if now.hour == 11 and now.minute == 28:
        dst = os.path.join(
            backup_root,
            "backup_" + now.strftime("%Y%m%d_%H%M%S")
        )

        shutil.copytree(src, dst)
        print("Backup created:", dst)

        with open("outputs.txt", "a") as out:
            out.write("=== Backup Created ===\n")
            out.write(f"Backup Path: {dst}\n")
            out.write(f"Time: {now}\n\n")

        time.sleep(60) 

    time.sleep(1)  
