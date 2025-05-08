
import product

class ProductManager ():
    def __init__(self, product_list):
        self.product_list = product_list
        

# Function that adds new products  
    def add_products (self, new_product):
        self.product_list.append(new_product)
        
# Function that displays the products and their data
    def display_products(self):
        for i, p in enumerate(self.product_list):
            print(f"{i+1}.")
            product.Product.display_info(p)

# Function that calculates the total inventory             
    def total_inventory (self):
        total_inventory = 0 
        for p in self.product_list:
            total_inventory += p.quantity
        print(f"Total inventory is {total_inventory}")
        
        
    
    