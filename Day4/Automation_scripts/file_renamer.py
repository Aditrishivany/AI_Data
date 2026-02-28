import os

old_file = r"D:\Users\Admin\Desktop\AI&Data\Day4\Automation_scripts\outputs_file.txt"
new_file = os.path.join(os.path.dirname(old_file), "output_file.txt")

os.rename(old_file, new_file)

print("File renamed successfully!")

with open("output_file.txt", "a") as out:
    out.write(f"Renamed file:\n{old_file} --> {new_file}\n\n")
