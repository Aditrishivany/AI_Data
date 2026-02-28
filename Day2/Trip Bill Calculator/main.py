from functions import total_trip_bill, show_trip_summary
name = input("Enter name: ").strip()
age = input("Enter age: ").strip()
phone = input("Enter phone: ").strip()
places = ["Hyderabad", "Chennai", "Goa"]
restaurants = ["Paradise", "Blue Sea", "Sindhu"]
bills = [1200, 890, 450]
total = total_trip_bill(*bills)
show_trip_summary(
    name=name,
    age=age,
    phone=phone,
    places=places,
    restaurants=restaurants,
    bills=bills,
    total=total
)
