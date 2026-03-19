import validations 
import database
import utilities

def View_Registered_Orders():

            # Validate if required databases are empty
            if database.product_database == {} or database.customer_database == {} or database.order_database == {}:
                print("\n\033[1;31m" + "-"*60 + f"\nError: No data was found to create an order." + "\n" + "-"*60 + "\033[0m\n")
                return

            # Display section title
            utilities.title(f"View Order")

            while True:

                # Ask for customer ID (CC)
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

                # Validate numeric length (6–10 digits)
                error = validations.validate_numeric_length(customer_id, "CC Number", 6, 10)
                if error:
                    print(error)
                    continue

                # Validate if ID exists in database
                error = validations.validate_duplicate_id(customer_id, database.customer_database)
                if not error:
                    print("\n\033[1;31m" + "-"*60 + f"\nError: CC Number of the Customer was not found." + "\n" + "-"*60 + "\033[0m")
                    break  

                # Call function to consult orders
                orders_consult(database.order_database,customer_id)

                # Exit loop if all validations pass
                break


def orders_consult(order_db,field_value):
        
        # Flag to check if the user has orders
        has_orders = False

        # Check if at least one order exists for the user
        for pedido in order_db.values():
            if pedido.get("cc") == field_value:
                has_orders = True
                break

        # If no orders found, show error
        if not has_orders:
            print("\n\033[1;31m" + "-"*60 +
                f"\nError: There are no orders from this user." +
                "\n" + "-"*60 + "\033[0m")
            return  
        
        # Print header (only once)
        for pedido in order_db.values():
                
            cc = pedido.get("cc"," ")

            if cc == field_value:
                print("\n\033[34m" + "-"*60)
                print("ORDER CREATION HISTORY")
                print("\033[34m" + "-"*60)

                # Get customer data
                cc = pedido.get("cc", "")
                nombre = pedido.get("name", "")
                
                print(f"CC: {cc} - Nombre: {nombre}")
                print("\033[34m" + "-"*60)

                # Print table header
                print(f"{'Producto':<20} {'Cantidad':<10}  {'Price':<10}  {'Total':<20}")

                break

        # Iterate through all orders of the user
        for pedido in order_db.values():
                
            cc = pedido.get("cc"," ")

            if cc == field_value:
                
                if pedido:

                    # Flag to check if order has products
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

                    # If no products found in the order
                    if not has_products:
                        print("No tiene productos.")
                        print("\033[34m" + "-"*60)