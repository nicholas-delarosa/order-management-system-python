# ==============================
# PROGRAM DATABASES
# ==============================

# ==============================
# CUSTOMER DATABASE
# ==============================
# Dictionary storing customer information
# Key: Customer ID (CC)
# Value: Dictionary with customer details
customer_database = {
    "123456": {"auto_id": 1, "name": "Jesus Lucena", "email": "jesus@gmail.com", "phone": "3011234567", "state": True},
    "654321": {"auto_id": 2, "name": "Ana Torres", "email": "ana@gmail.com", "phone": "3017654321", "state": True},
    "112233": {"auto_id": 3, "name": "Pedro Perez", "email": "pedro@gmail.com", "phone": "3021122334", "state": True},
    "445566": {"auto_id": 4, "name": "Maria Gomez", "email": "maria@gmail.com", "phone": "3024455667", "state": True},
    "778899": {"auto_id": 5, "name": "Luis Sanchez", "email": "luis@gmail.com", "phone": "3037788990", "state": True},
    "123455": {"auto_id": 6, "name": "Luis Sanchez", "email": "lus@gmail.com", "phone": "307788990", "state": True}
}

# ==============================
# PRODUCT DATABASE
# ==============================
# Dictionary storing product information
# Key: Product ID
# Value: Tuple (name, price, stock, category)
product_database = {
    1: ("Pan", 12.0, 100, "Groceries"),
    2: ("Queso", 20.0, 50, "Groceries"),
    3: ("Jugo", 10.0, 80, "Groceries"),
    4: ("Leche", 15.0, 60, "Groceries"),
    5: ("Zapatos", 120.0, 30, "Footwear"),
    6: ("Camiseta", 35.0, 40, "Clothing"),
    7: ("Laptop", 2500.0, 10, "Electronics"),
    8: ("Teclado", 150.0, 25, "Electronics"),
    9: ("Silla", 200.0, 15, "Home & Furniture"),
    10: ("Libro", 50.0, 40, "Stationery")
}

# ==============================
# ORDER DATABASE
# ==============================
# Dictionary storing all orders
# Key: Order ID
# Value: Dictionary with customer info and purchased products
order_database = {}

# Order 1 for Jesus
order_database[1] = {
    "cc": "123456",  # Customer ID
    "name": "Jesus Lucena",  # Customer name
    "producto1": (1, "Pan", 5, 60.0),  # (product_id, product_name, quantity, total_price)
    "producto2": (2, "Queso", 2, 40.0),
}

# Order 2 for Ana
order_database[2] = {
    "cc": "654321",
    "name": "Ana Torres",
    "producto1": (3, "Jugo", 3, 30.0),
    "producto2": (4, "Leche", 4, 60.0),
}

# Order 3 for Jesus again
order_database[3] = {
    "cc": "123456",
    "name": "Jesus Lucena",
    "producto1": (5, "Zapatos", 1, 120.0),
    "producto2": (6, "Camiseta", 2, 70.0),
}

# Order 4 for Pedro
order_database[4] = {
    "cc": "112233",
    "name": "Pedro Perez",
    "producto1": (1, "Pan", 10, 120.0),
    "producto2": (4, "Leche", 5, 75.0),
}

# Order 5 for Maria
order_database[5] = {
    "cc": "445566",
    "name": "Maria Gomez",
    "producto1": (7, "Laptop", 1, 2500.0),
    "producto2": (8, "Teclado", 1, 150.0),
}

# Order 6 for Luis
order_database[6] = {
    "cc": "778899",
    "name": "Luis Sanchez",
    "producto1": (9, "Silla", 2, 400.0),
    "producto2": (10, "Libro", 3, 150.0),
}

# ==============================
# PRODUCT CATEGORIES
# ==============================
# Tuple containing all available product categories
product_categories = (
    "Electronics",
    "Appliances",
    "Groceries",
    "Clothing",
    "Footwear",
    "Health & Beauty",
    "Home & Furniture",
    "Stationery",
    "Toys",
    "Sports",
    "Automotive",
    "Hardware & Tools"
)