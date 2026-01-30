errors = []

with open("app.log", "r") as f:
    for line in f:
        if "error" in line.lower():
            errors.append(line)

with open("outputs.txt", "a") as out:
    out.write("=== Extracted Errors ===\n")
    out.writelines(errors)
    out.write("\n")

print("Errors extracted to outputs.txt")