import os
import shutil

source = r"D:\Users\Admin\Desktop\AI&Data\Day4\file_manager_source"
organized = []

for file in os.listdir(source):
    path = os.path.join(source, file)

    if os.path.isfile(path):
        ext = file.split(".")[-1].lower()
        folder = os.path.join(source, ext)

        if not os.path.exists(folder):
            os.makedirs(folder)

        new_path = os.path.join(folder, file)
        shutil.move(path, new_path)
        organized.append(f"{file} --> {folder}")

        print(f"Moved: {file} --> {folder}")

with open("output_file.txt", "a", encoding="utf-8") as out:
    out.write("=== File Manager Report ===\n")
    for line in organized:
        out.write(line + "\n")
    out.write("\n")

print("File organization completed.")
