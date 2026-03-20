import database

def daily_income_calculation():

    # Variable to store the total income of the day
    total_sum = 0

    # Counter to enumerate orders
    cont = 1
    
    # Iterate through all orders in the database
    for pedido in database.order_database.values():

        # Print order header
        print("\n\033[34m" + "-"*60)
        print(f"ORDER - N{cont}")
        print("\033[34m" + "-"*60)

        # Increase order counter
        cont += 1

        # Get customer information from the order
        cc = pedido.get("cc", "")
        nombre = pedido.get("name", "")
        
        # Print customer information
        print(f"CC: {cc} - Nombre: {nombre}")
        print("\033[34m" + "-"*60)

        # Print table header for products
        print(f"{'Producto':<20} {'Cantidad':<10}  {'Price':<10}  {'Total':<20}")
        
        # Flag to check if products exist
        has_products = False

        # Iterate directly over dictionary keys (NO list used)
        for k in sorted(pedido.keys()):
            if k.startswith('producto') and isinstance(pedido[k], tuple):

                has_products = True

                # Unpack tuple values
                _, producto_nombre, cantidad, total = pedido[k]

                # Print product details
                print(f"{producto_nombre:<20} {cantidad:<10} X {total/cantidad:<10} : {total:<20}")

                # Add product total to daily sum
                total_sum += total

                # Print separator
                print("\033[34m" + "-"*60)

        # If no products were found
        if not has_products:
            print("No tiene productos.")
            print("\033[34m" + "-"*60)


    # Print final total income of the day
    print("\n\033[34m" + "-"*60)
    print(f">> Total profit for the day : ${total_sum}")
    print("\033[34m" + "-"*60 + "\033[0m")