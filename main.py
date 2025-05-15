
import product
from product_manager import ProductManager
from cart import Cart

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

# Creating cart instance
cart = Cart([])

#Checking if the product from the cart is the same as one of our products from product list
new_product = input("Please insert desired product in your cart: ")
cart_list = []
while new_product:
    find_check = False
    if new_product in cart_list:
            find_check = True
            cart.quantity_update(new_product)
    else:
        for p in product_list:
            if new_product == p.name:
                find_check = True
                cart_list.append(new_product)
                cart.add_products(product.Product(p.name, p.price, p.quantity - p.quantity + 1))
    if find_check == False:
        new_product = input(f"Please insert one of the products from our products: ")
    new_product = input("Please insert desired product in your cart: ")

# Display the items of the cart
cart.display_products()

# Printing the total of the cart
cart.total_inventory()

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


