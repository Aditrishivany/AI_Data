import os, time

folder = r"D:\Users\Admin\Desktop\AI&Data\day4\file_manager_source"
days = 30
limit = days * 86400
now = time.time()

deleted = []

for f in os.listdir(folder):
    path = os.path.join(folder, f)
    if os.path.isfile(path):
        if now - os.path.getmtime(path) > limit:
            os.remove(path)
            deleted.append(f)
            print("Deleted:", f)

with open("output_file.txt", "a") as out:
    out.write("=== Folder Cleanup Report ===\n")
    if deleted:
        for item in deleted:
            out.write(f"Deleted: {item}\n")
    else:
        out.write("No files deleted.\n")
    out.write("\n")
