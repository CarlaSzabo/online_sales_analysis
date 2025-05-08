
import product
from product_manager import ProductManager

# Creating product_list with objects
product_list = [
        product.Product("Laptop", 1500, 8),
        product.Product("Computer", 3500, 10),
        product.Product("Keyboard", 500, 20),
        product.Product("Mouse", 100, 22),
        product.Product("Headphones", 200, 13),
]

# Creating product_manager instance
product_manager = ProductManager(product_list)

# Adding new products to the product_list
while True:
    try:
        new_product = product.Product(input("Introduce the name of a new product: "), int(input("Introduce the price of the new product: ")), int(input("Introduce the quantity of the product: ")))
    except:
        break
    product_manager.add_products(new_product)

# Printing the product_list
print("Products display information : ")
product_manager.display_products()

# Printing total inventory
product_manager.total_inventory()

