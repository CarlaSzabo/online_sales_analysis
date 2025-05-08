

class Product ():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Method for displaying the information about the product
    def display_info(self):
       print(f"Product: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}")

# Method that updates the quantity of the products    
    def quantity_actualization(self, new_quantity):
        try:
            new_quantity / 2 and new_quantity > 0
            self.quantity = new_quantity
        except:
            print("The quantity introduced has to be a number higher than 0.")