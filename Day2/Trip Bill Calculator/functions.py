def total_trip_bill(*args):
    return sum(args)
def show_trip_summary(**kwargs):
    phone = kwargs["phone"].strip()
    masked = phone[0:2] + "******" + phone[-2:]
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
