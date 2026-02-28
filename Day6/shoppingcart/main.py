from decorators.registration import registration
from cart.shopping import ShoppingCart
@registration
def start_shopping(name, email, phone):
    print("You can now add products to your cart!")
start_shopping("Aditri", "aditri@example.com", 9876543210)
cart = ShoppingCart()
cart.add_to_cart(1)
cart.add_to_cart(3)
cart.add_to_cart(5)
cart.show_cart()
