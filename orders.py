import validations 
import database
import utilities

def order_creation():

            # Dictionary to store order history during the session
            order_history = {}

            # Control variable to keep adding products
            or_act = True

            # Validate if required databases exist
            if database.product_database == {} or database.customer_database == {}:
                print("\n\033[1;31m" + "-"*60 + f"\nError: No data was found to create an order." + "\n" + "-"*60 + "\033[0m\n")
                return

            # Display title with next order number
            utilities.title(f"Order Creation N{len(database.order_database)+1}")

            while True:

                # Ask for customer ID
                customer_id = input("\n\033[34m >> \033[0mEnter your CC number: ")

                # Validate empty field
                error = validations.validate_not_empty(customer_id, "CC Number")
                if error:
                    print(error)
                    continue

                # Validate numeric input
                error = validations.validate_only_numbers(customer_id, "CC Number")
                if error:
                    print(error)
                    continue

                # Validate numeric length
                error = validations.validate_numeric_length(customer_id, "CC Number", 6, 10)
                if error:
                    print(error)
                    continue

                # Validate if customer exists
                error = validations.validate_duplicate_id(customer_id, database.customer_database)
                if not error:
                    print("\n\033[1;31m" + "-"*60 + f"\nError: CC Number of the Customer was not found." + "\n" + "-"*60 + "\033[0m")
                    break  

                # Create new order
                id_order = create_order(customer_id, order_history)

                break

            cont = 1

            # Display available products
            print("\n\033[34m" + "-"*80)
            print("PRODUCTS")
            print("\033[34m" + "-"*80)
            print(f"{'ID':<5} {'NAME':<22} {'CATEGIRIE':<20} {'STOCK':<10} {'PRICE':<10}")
            print("-"*80 + "\033[0m")

            for cc, data in database.product_database.items():
                print(
                    f"\033[1;32m{cc:<5} {data[0]:<22} {data[3]:<20} {data[2]:<10} {data[1]:<10}\033[0m"
                    )
                print("\033[34m" + "-"*80 + "\033[0m")

            # Loop to add products to the order
            while or_act:
                utilities.title(f"Product Order N{cont}")
        
                # ===== INPUT: PRODUCT ID =====
                while True:

                    try: 
                        product_id = int(input(f"\n\033[34m >> \033[0mEnter the number of the option for the products: "))
                    except ValueError:
                        print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                        continue

                    error = validations.validate_not_empty(product_id, "The option of the product")
                    if error:
                        print(error)
                        continue

                    error = validations.validate_category_option(product_id, 1, len(database.product_database))
                    if error:
                        print(error)
                        continue

                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # ===== INPUT: quantity order =====
                while True:
                                    
                    try:
                        quantity_order = int(input("\n\033[34m >> \033[0mEnter the quantity of products to order : "))
                    except ValueError:
                        print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                        continue

                    error = validations.validate_not_empty(quantity_order, "Products to order")
                    if error:
                        print(error)
                        continue

                    error = validations.validate_cuantiti_negative(quantity_order)
                    if error:
                        print(error)
                        continue

                    # Get product stock
                    stock = database.product_database[product_id][2]

                    # Validate stock availability
                    error = validations.validate_sale(stock, 3, quantity_order)
                    if error:
                        print(error)
                        continue

                    
                
                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # Add product to order
                add_products_order(id_order, product_id, quantity_order, cont, order_history)

                # Ask user if they want to continue adding products
                exit = utilities.confirm_exit()
                if exit == True:
                    or_act = False
                else:
                    cont += 1
                    continue

                # ===== PRODUCTS CREATION HISTORY =====
                display_order_summary(order_history)

                # Final separator
                print("\033[34m" + "-"*60 + "\033[0m\n")


def create_order(customer_id,order_history):
    """
    Function: create_order

    Parameters:

    - customer_id:
    Represents the customer's identification number (ID or "cédula").
    It is used to associate the new order with a specific customer.

    - Order_history:
    Dictionary that stores the history of recently created orders.
    This structure is used to save and track all orders made by customers.

    Description:
    This function creates a new order for a given customer and records it
    in the order history dictionary for future reference and tracking.
    """
    
    # Generate new order ID
    id_order = len(database.order_database) + 1

    # Get customer name
    customer_name = database.customer_database[customer_id]["name"]
    
    # Store order in main database
    database.order_database[id_order] = {
        "cc" : customer_id,
        "name": customer_name,
    }

    # Store order in temporary history
    order_history[id_order]  = {
        "cc" : customer_id,
        "name": customer_name,
    }

    return id_order


def add_products_order(id_order, product_id, quantity_order, cont, order_history):
    """
    Function: add_products_order

    Parameters:

    - id_order:
    Represents the unique identifier of the order to which products will be added.

    - product_id:
    Represents the ID of the product that the customer wants to order.

    - quantity_order:
    Indicates the quantity of the selected product to be added to the order.

    - cont:
    Counter used to track the number of products added to the order.
    For example, the first product added is 1, the next is 2, and so on.

    - order_history:
    Dictionary that stores the history of the most recent orders.
    It keeps track of the products added and their details within each order.

    Description:
    This function adds products to an existing order, updating the order history
    with the product ID, quantity, and sequence number of each added product.
    """
    
    # Get product name
    product_name = database.product_database[product_id][0]

    # Calculate total price
    total = quantity_order * database.product_database[product_id][1]
    
    # Store product in order (main database and history)
    database.order_database[id_order]["producto"+str(cont)] = (product_id,product_name,quantity_order,total)
    order_history[id_order]["producto"+str(cont)] = (product_id,product_name,quantity_order,total)


def display_order_summary(order_db):
    """
    Function: display_order_summary

    Parameters:

    - order_db:
    Dictionary that stores the order history.
    It contains the most recent records of orders created, including
    customer information and products associated with each order.

    Description:
    This function displays a summary of the latest orders stored in the
    order history, showing the most recent records created in the system.
    """

    for pedido in order_db.values():

        # Print order header
        print("\n\033[34m" + "-"*60)
        print("ORDER CREATION HISTORY")
        print("\033[34m" + "-"*60)

        # Get customer info
        cc = pedido.get("cc", "")
        nombre = pedido.get("name", "")
        
        print(f"CC: {cc} - Nombre: {nombre}")
        print("\033[34m" + "-"*60)

        # Print table header
        print(f"{'Producto':<20} {'Cantidad':<10}  {'Price':<10}  {'Total':<20}")
        
        # Flag to check if products exist
        has_products = False

        # Iterate directly over dictionary keys (NO list used)
        for k in sorted(pedido.keys()):
            if k.startswith('producto') and isinstance(pedido[k], tuple):

                has_products = True

                # Unpack tuple values
                _, producto_nombre, cantidad, total = pedido[k]

                # Print product information
                print(f"{producto_nombre:<20} {cantidad:<10} X {total/cantidad:<10} : {total:<20}")
                print("\033[34m" + "-"*60)

        # If no products found
        if not has_products:
            print("No tiene productos.")
            print("\033[34m" + "-"*60)