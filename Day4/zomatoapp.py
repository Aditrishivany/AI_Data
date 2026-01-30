print("Welcome to Zomato Order Calculator")
menu={
1:("Burger",120),
2:("Pizza",250),
3:("Fries",80),
4:("Cold Drink",40),
5:("Chicken Biryani",180),
6:("Veg Biryani",150),
7:("Chicken Shawarma",90),
8:("Paneer Roll",70),
9:("Chicken Noodles",130),
10:("Veg Fried Rice",110),
11:("Gulab Jamun",50),
12:("Ice Cream",60)
}
print("Menu:")
for n,i in menu.items():print(f"{n}. {i[0]} - Rs.{i[1]}")
try:
    choice=int(input("Enter item number: "))
    if choice not in menu:raise ValueError("Invalid menu item")
    name,price=menu[choice]
    qty=int(input(f"Enter quantity of {name}: "))
    if qty<=0:raise ZeroDivisionError("Quantity must be greater than zero")
    total=price*qty
except ValueError as ve:
    print("Value Error:",ve)
except ZeroDivisionError as zde:
    print("Quantity Error:",zde)
except TypeError as te:
    print("Type Error:",te)
except Exception as e:
    print("Unknown Error:",e)
else:
    print("Order Placed Successfully!")
    print("Item:",name)
    print("Quantity:",qty)
    print("Total Amount: Rs.",total)
finally:
    print("Thank you for using Zomato Order Calculator")
