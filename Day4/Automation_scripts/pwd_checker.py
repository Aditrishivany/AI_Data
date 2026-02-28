password = input("Enter password: ")
strength = 0
if len(password) >= 8: strength += 1
if any(c.islower() for c in password): strength += 1
if any(c.isupper() for c in password): strength += 1
if any(c.isdigit() for c in password): strength += 1
if any(c in "@#$%!&*" for c in password): strength += 1
levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
result = levels[min(strength,4)]
print("Strength:", result)
with open("outputs.txt", "a") as out:
    out.write(f"Password: {password} | Strength: {result}\n")
