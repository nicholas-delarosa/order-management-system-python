import validations 
import database
import utilities

def product_registration():

            # Dictionary to store products created during this session
            products_history = {}

            # Control variable to keep the registration active
            pr_act = True

            # Main loop for product registration
            while pr_act:

                # Display title with next product number
                utilities.title(f"Product Registration N{len(database.product_database)+1}")
        
                # ===== INPUT: PRODUCT NAME =====
                while True:
                    # Ask for product name
                    product_name = input("\n\033[34m >> \033[0mEnter the product name: ")

                    # Validate empty field
                    error = validations.validate_not_empty(product_name, "Name")
                    if error:
                        print(error)
                        continue

                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # ===== INPUT: PRODUCT PRICE =====
                while True:

                    # Try to convert input to float
                    try:
                        product_price = float(input("\n\033[34m >> \033[0mEnter the product price: "))
                    except ValueError:
                        print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                        continue

                    # Validate empty field
                    error = validations.validate_not_empty(product_price, "Product Price")
                    if error:
                        print(error)
                        continue

                    # Validate non-negative value
                    error = validations.validate_cuantiti_negative(product_price)
                    if error:
                        print(error)
                        continue

                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # ===== INPUT: PRODUCT STOCK =====
                while True:
                        
                    # Try to convert input to integer
                    try:
                        product_stock = int(input("\n\033[34m >> \033[0mEnter the product stock (must be greater than 3): "))
                    except ValueError:
                        print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                        continue

                    # Validate empty field
                    error = validations.validate_not_empty(product_stock, "Product Stock")
                    if error:
                        print(error)
                        continue

                    # Validate non-negative value
                    error = validations.validate_cuantiti_negative(product_stock)
                    if error:
                        print(error)
                        continue

                    # Validate minimum stock requirement
                    error = validations.validate_stock_above_minimum(product_stock, 3)
                    if error:
                        print(error)
                        continue
                
                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")


                # ===== INPUT: PRODUCT CATEGORY =====
                while True:
                    # Display available categories
                    utilities.iterate_list(database.product_categories)

                    # Ask for category option
                    try: 
                        product_categorie = int(input(f"\n\033[34m >> \033[0mEnter the number of the option for the product category: "))
                    except ValueError:
                        print("\n\033[1;31m" + "-"*60 +"\nError: Only numeric values are allowed. Please enter a valid number." +"\n" + "-"*60 + "\033[0m")
                        continue

                    # Validate empty field
                    error = validations.validate_not_empty(product_categorie, "The option of the product")
                    if error:
                        print(error)
                        continue

                    # Validate valid category range
                    error = validations.validate_category_option(product_categorie, 1, len(database.product_categories))
                    if error:
                        print(error)
                        continue

                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # Register product in database and history
                register_product(product_name, product_price, product_stock, product_categorie,products_history)

                # Ask user if they want to continue
                exit = utilities.confirm_exit()
                if exit == True:
                    pr_act = False
                else:
                    continue

                # ===== PRODUCTS CREATION HISTORY =====

                # Print header
                print("\n\033[34m" + "-"*80)
                print("PRODUCTS CREATION HISTORY")
                print("\033[34m" + "-"*80)
                print(f"{'ID':<5} {'NAME':<22} {'CATEGIRIE':<20} {'STOCK':<10} {'PRICE':<10}")
                print("-"*80 + "\033[0m")

                # Iterate and display created products
                for cc, data in products_history.items():
                    print(
                        f"\033[1;32m{cc:<5} {data[0]:<22} {data[3]:<20} {data[2]:<10} {data[1]:<10}\033[0m"
                    )
                    print("\033[34m" + "-"*80 + "\033[0m")

                # Final separator
                print("\033[34m" + "-"*60 + "\033[0m\n")


def register_product(product_name, product_price, product_stock, product_categorie,products_history):
    """
    Function: register_product

    Parameters:

    - product_name:
    Represents the name of the product to be registered.

    - product_price:
    Indicates the price of the product.

    - product_stock:
    Represents the available quantity (stock) of the product.

    - product_categorie:
    Specifies the category to which the product belongs
    (e.g., food, drinks, etc.).

    - Products_history:
    Dictionary that stores the history of the most recently created products.
    It is used to keep track of all registered products and their information.

    Description:
    This function registers a new product in the system and stores its
    information in the products history dictionary for future reference.
    """

    # Generate new product ID
    id_product = len(database.product_database) + 1

    # Store product in main database (tuple structure)
    database.product_database [id_product] = (product_name,product_price,product_stock,database.product_categories[product_categorie-1])

    # Store product in temporary history
    products_history [id_product] = (product_name,product_price,product_stock,database.product_categories[product_categorie-1])
