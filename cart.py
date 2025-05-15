import product
from product_manager import ProductManager


class Cart():
    
    def __init__(self, cart_items):
        self.cart_items = cart_items
        
    # Function that adds new products  
    def add_products (self, new_product):
        self.cart_items.append(new_product)
        
    #Function that updates items quantity in the cart
    def quantity_update (self, item):
        for p in self.cart_items:
            if p.name == item:
                p.quantity += 1
                

    # Function that calculates the total sum of the cart            
    def total_inventory (self):
        total_cart_sum = 0 
        for p in self.cart_items:
            total_cart_sum += p.quantity * p.price
        print(f"Total sum of the cart is {total_cart_sum}")
        
    # Function that displays the products from the cart
    def display_products(self):
        for i, item in enumerate(self.cart_items):
            print(f"{i+1}.")
            print(f"{item.name}, {item.price}, {item.quantity}")