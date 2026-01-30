from functions import mask, total, save, log, ticket
import os
os.makedirs("Tickets", exist_ok=True)
os.makedirs("Logs", exist_ok=True)
name = input("Enter name: ").strip().title()
age = input("Enter age: ").strip()
phone = input("Enter phone: ").strip()
mphone = mask(phone)
movies = ["Salaar", "Animal", "Kalki", "Leo"]
print("\nMovies:")
for i, m in enumerate(movies, 1):
    print(f"{i}. {m}")
mchoice = int(input("Choose movie (1-4): "))
movie = movies[mchoice - 1]
times = ["10:00 AM", "1:00 PM", "4:30 PM", "7:30 PM"]
print("\nShow Times:")
for i, t in enumerate(times, 1):
    print(f"{i}. {t}")
tchoice = int(input("Choose time (1-4): "))
show = times[tchoice - 1]
print("\nSeat Types:")
print("1. Premium - ₹250")
print("2. Gold - ₹180")
print("3. Silver - ₹120")
stype = int(input("Choose seat type (1-3): "))
count = int(input("Number of seats: "))
if stype == 1:
    price = 250
elif stype == 2:
    price = 180
else:
    price = 120
seat_total = count * price
snacks = []
print("\nAdd snacks (type 'done' to finish):")
while True:
    s = input("Snack: ").strip().title()
    if s.lower() == "done":
        break
    snacks.append(s)
snack_text = ", ".join(snacks) if snacks else "None"
coupon = input("\nEnter coupon code (if any): ").strip().upper()
final = seat_total
if "STUDENT10" in coupon:
    final *= 0.90
elif "FESTIVE20" in coupon:
    final *= 0.80
final = round(final)
summary = ticket(
    name=name,
    age=age,
    phone=mphone,
    movie=movie,
    time=show,
    seats=count,
    seat_type="Premium" if stype==1 else "Gold" if stype==2 else "Silver",
    snacks=snack_text,
    total=f"Rs.{final}"
)
fname = f"Tickets/ticket_{name.replace(' ', '_')}.txt"
save(fname, summary)
print(f"Ticket saved at: {fname}")
log("Logs/log.txt", f"{name} booked {movie} at {show} | Total Rs.{final}")
print("Booking Logged.")
