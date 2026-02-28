import os
import time
import random
from datetime import datetime

users_file="users.txt"
trips=[]
available_drivers={"Ravi","Ashwin","Ramu","Ramesh","Suresh"}
busy_drivers=set()

distances={
("chennai","mumbai"):1330,
("mumbai","chennai"):1330,
("chennai","hyderabad"):630,
("hyderabad","chennai"):630,
("hyderabad","pune"):560,
("pune","hyderabad"):560,
("mumbai","pune"):150,
("pune","mumbai"):150
}

price_per_km=12

if not os.path.exists("invoices"):
    os.mkdir("invoices")

def save_user(username,password):
    with open(users_file,"a") as f:
        f.write(f"{username},{password}\n")

def authenticate(username,password):
    if not os.path.exists(users_file):
        return False
    with open(users_file,"r") as f:
        for line in f:
            u,p=line.strip().split(",")
            if u==username and p==password:
                return True
    return False

def calculate_fare(src,dst):
    if (src,dst) in distances:
        return distances[(src,dst)]*price_per_km
    return None

def assign_driver():
    if not available_drivers:
        return "No Driver Available"
    d=random.choice(list(available_drivers))
    available_drivers.remove(d)
    busy_drivers.add(d)
    return d

def generate_invoice(trip):
    filename=f"invoices/invoice_{trip['id']}.txt"
    with open(filename,"w",encoding="utf-8") as f:
        f.write("UBER INVOICE\n")
        f.write(f"Trip ID: {trip['id']}\n")
        f.write(f"User: {trip['user']}\n")
        f.write(f"Driver: {trip['driver']}\n")
        f.write(f"Source: {trip['source']}\n")
        f.write(f"Destination: {trip['destination']}\n")
        f.write(f"Fare: Rs.{trip['fare']}\n")
        f.write(f"Status: {trip['status']}\n")
        f.write(f"Feedback: {trip['feedback']}\n")
        f.write(f"Generated: {datetime.now()}\n")

def auto_status(trip):
    stages=["waiting","arrived","started","completed"]
    for i in range(1,4):
        time.sleep(5)
        trip["status"]=stages[i]
        print("Status:",trip["status"])
    busy_drivers.remove(trip["driver"])
    available_drivers.add(trip["driver"])
    fb=input("Enter feedback: ")
    trip["feedback"]=fb
    generate_invoice(trip)

def create_trip(user,**kwargs):
    trip_id=len(trips)+1
    trip={
    "id":trip_id,
    "user":user,
    "provider":"uber",
    "source":kwargs.get("source"),
    "destination":kwargs.get("destination"),
    "fare":kwargs.get("fare"),
    "status":"waiting",
    "driver":assign_driver(),
    "feedback":"Not Given"
    }
    trips.append(trip)
    print("\nTrip Added Successfully!\n")
    print("Status: waiting")
    generate_invoice(trip)
    print("Auto updating status...\n")
    auto_status(trip)
    print(f"Invoice saved: invoices/invoice_{trip_id}.txt\n")

def view_trips(user):
    t=[x for x in trips if x["user"]==user]
    if not t:
        print("\nNo trips found!\n")
        return
    for i in t:
        print(i)
    print()

def search_location(loc,user):
    print("\nSearch Results:")
    f=False
    for t in trips:
        if t["user"]==user and (t["source"]==loc or t["destination"]==loc):
            print(t);f=True
    if not f:
        print("No trips found for this location.")
    print()

def remove_trip(tid,user):
    for t in trips:
        if t["id"]==tid and t["user"]==user:
            trips.remove(t)
            print("Trip removed.\n")
            return
    print("Invalid Trip ID\n")

def login_system():
    print("Are you registered? (yes/no)")
    a=input().lower()
    if a=="yes":
        u=input("Enter username: ")
        p=input("Enter password: ")
        if authenticate(u,p):
            print("Login successful\n")
            return u
        else:
            print("Invalid credentials\n")
            return login_system()
    else:
        u=input("Create username: ")
        p=input("Create password: ")
        save_user(u,p)
        print("Registered. Login now.\n")
        return login_system()

def menu(user):
    while True:
        print("""
UBER APPLICATION:
1. Book a Trip
2. View Trips
3. Search Trips by Location
4. Remove Trip
5. Exit
""")
        c=input("Enter option: ")
        if c=="1":
            src=input("Enter Source: ").lower()
            dst=input("Enter Destination: ").lower()
            fare=calculate_fare(src,dst)
            if fare is None:
                print("Route not available in system!\n")
                continue
            create_trip(user,source=src,destination=dst,fare=fare)
        elif c=="2":
            view_trips(user)
        elif c=="3":
            loc=input("Enter Location to Search: ").lower()
            search_location(loc,user)
        elif c=="4":
            tid=int(input("Enter Trip ID: "))
            remove_trip(tid,user)
        elif c=="5":
            print("Thankyou")
            break
        else:
            print("Invalid Option\n")

user=login_system()
menu(user)
