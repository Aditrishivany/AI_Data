n=int(input())
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  print()

n=int(input())
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

n=int(input())
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or (i+j==n-1):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

n=int(input())
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or (i==j):
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

n=int(input())
for i in range(1,n+1):
  for j in range(i):
    print("*",end=" ")
  print()

n=int(input())
for i in range(n,0,-1):
  for j in range(i):
    print("*",end=" ")
  print()

n = 5

for i in range(1, n + 1):

    # Leading spaces to center the row
    print("  " * (n - i), end="")

    # Numbers separated widely to maintain triangle symmetry
    for j in range(i):
        print(i, end="   ")

    print()

driver="Ravi"
pickup="kompally"
drop="uppal"
fare=250.50
status="completed"
summary=f"Driver {driver} picked you up from {pickup} and dropped at {drop}, total fare is {fare} and the ride is {status.capitalize()}"
print(summary)

mobile="9000055050"
masked=mobile[0:2]+"******"+mobile[-2:]
print(masked)

song="shape OF you"
artist="ed ShEERAN"
formatted=f"{song.title()} - {artist.title()}"
print(formatted)

location=" chenai central"
fixed_location=location.replace("chenai","chennai")
print(fixed_location)

#extract id from booking message
message="your uber bookin ID:UB12345. please keep it safe"
booking_id=message.split(":")[1].split(".")[0]
print(booking_id)

msg="use ZOMATO100 to get Rs.100 off on your first order!"
if "ZOMATO100" in msg:
  print("Offer Applied")

feedback="the driver was polite and the ride was smooth"
print(feedback.find("polite"))

fullname = "Adirishivany tatipally"
initials = "".join(fullname.split(" ")[0][0].upper()+fullname.split(" ")[1][0].upper())
print(initials)

fullname = "Aditri shivany tatipally"
initials = "".join(w[0].upper() for w in fullname.split())
print(initials)

dirty_input="  aditri      "
clean=dirty_input.strip()
print(clean)

dirty = "   Aditrishivany     tatipally     is   here   "
clean = " ".join(dirty.split())
print(clean)

msg = "  Hello   this is  a  message  "
count = len(msg.split())
print(count)

username=input("enter the username: ")
pwd=input("enter the password: ")
if username=="admin" and pwd=="1234":
  print("login successful")
else:
  print("invalid username and password")

marks=int(input("Enter marks: "))
att=int(input("Enter attendance: "))
if marks>=50 and att>=75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")

recharge=int(input("Enter recharge amount: "))
data=int(input("Enter data balance (in GB): "))
if recharge>399 and data> 2:
    print("Bonus 2GB is available")
else:
    print("No bonus available")

bill = float(input("Enter bill amount: "))
day = input("Enter day of week: ").lower()
membership = input("Enter membership type(Gold/Silver): ").lower()
if bill > 1000 and day in ("saturday", "sunday") and membership=="gold":
    discount = bill * 0.20
    final = bill - discount
    print("20% discount applied. Final bill:", final)
else:
    print("No discount. Final bill:", bill)

correct_pin="1234"
attempts=0
while attempts<3:
    pin=input("Enter ATM PIN: ")
    if pin==correct_pin:
        print("login successful")
        break
    else:
        attempts+=1
        remaining=3 - attempts
        if remaining>0:
            print(f"Wrong PIN, only {remaining} attempt(s) left")
        else:
            print("Account blocked due to 3 incorrect attempts")

cart = []
while True:
    item = input("Enter item to add to cart (type 'done' to finish): ").strip().lower()
    if item == "done":
        break
    else:
        cart.append(item)
        print(f"'{item}' added to cart")
print("\nYour cart items are:")
for i in cart:
    print("-", i)

def greet(name):
  print(f"welcome to {name}")
greet("uber")

def add(a,b):
  return a+b
result=add(5,10)
print(result)

def add_all(*args):
  sum=0
  for num in args:
    sum+=num
  return sum
print(add_all(1,2,3,4,5))
#multiple unnamed values
#works as a tuple

def print_data(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}: {value}")
print_data(name="Aditri",age=20)
#works as a dictionary

def profile_generator(**kwargs):
    profile_text = ""
    for key, value in kwargs.items():
        profile_text += f"{key.capitalize():}: {value}\n"
    return profile_text
name = input("Enter your full name: ").strip()
age = input("Enter your age: ").strip()
city = input("Enter your city: ").strip()
email = input("Enter your email: ").strip()
phone = input("Enter your phone number: ").strip()
result = profile_generator(
    name=name,
    age=age,
    city=city,
    email=email,
    phone=phone
)
print()
print(result)

#default parameter value
def greet(name="uber"):
  print(f"welcome to {name}")
greet()
greet("aditri")

def total_trip_bill(*args):
    return sum(args)
def show_trip_summary(**kwargs):
    phone=kwargs["phone"].strip()
    masked=phone[0:2]+"******"+phone[-2:]
    print()
    print("TRIP SUMMARY:")
    print(f"Name: {kwargs['name'].title()}")
    print(f"Age: {kwargs['age']}")
    print(f"Phone: {masked}")
    print("Places Visited:")
    for p in kwargs["places"]:
        print(p)
    print("Restaurants:")
    for r in kwargs["restaurants"]:
        print(r)
    print("Bills:")
    count = 1
    for amt in kwargs["bills"]:
      print(f"Bill {count}: Rs.{amt}")
      count += 1
    print(f"Total Trip Bill: Rs.{kwargs['total']}")
name=input("Enter name: ").strip()
age=input("Enter age: ").strip()
phone=input("Enter phone: ").strip()
places=["Hyderabad","Chennai","Goa"]
restaurants=["Paradise","Blue Sea","Sindhu"]
bills=[1200,890,450]
total=total_trip_bill(*bills)
show_trip_summary(
    name=name,
    age=age,
    phone=phone,
    places=places,
    restaurants=restaurants,
    bills=bills,
    total=total
)