# List of products
products = ["laptop", "smartphone", "tablet", "headphones"]

products.append("monitor")  # Adding a new product
products[0] = "gaming laptop"  # Updating a product
products.remove("tablet")  # Removing a product

print(products)

print("watch" in products)  # Check if "watch" is in the list

# Tuple of product prices
product = ("P1", "Keyboard", 3500)
product = ("P2", "Mouse", 1500)
product_id, name, price = product  # Unpacking the tuple

# Dictionary of product details
inventory = {
    "P1": {"name": "Keyboard", "price": 3500, "quantity": 50},
    "P2": {"name": "Mouse", "price": 1500, "quantity": 100},
    "P3": {"name": "Monitor", "price": 12000, "quantity": 30}
}

print(inventory)
print(inventory.keys())
print(inventory.values())

#Sets

online_customers = {"Alice", "Bob", "Charlie", "David"}
returning_customers = {"Bob", "Eve", "Frank", "Charlie"}

# Union of two sets
print(online_customers | returning_customers)

# Intersection of two sets
print(online_customers & returning_customers)

# difference of two sets
print(online_customers - returning_customers)