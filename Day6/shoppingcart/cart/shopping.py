from products.items import products

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product_id):
        if product_id in products:
            self.cart.append(products[product_id])
            print(f"Added to Cart: {products[product_id][0]}")
        else:
            print("Invalid Product ID")

    def show_cart(self):
        if not self.cart:
            print("Cart is Empty")
            return
        
        print("\nYour Cart Items:")
        total = 0
        for item, price in self.cart:
            print(f"- {item}: ₹{price}")
            total += price

        print("\nTotal Amount:", total)
