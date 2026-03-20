import validations 
import database
import utilities

def customer_registration():

            # Dictionary to store customers created during this session
            customer_history = {}

            # Control variable to keep the registration active
            cr_act = True

            # Main loop for customer registration
            while cr_act:

                # Show section title with current number of customers + 1
                utilities.title(f"Customer Registration {len(database.customer_database)+1}")
                        
                # ===== INPUT: CUSTOMER ID =====
                while True:

                    # Ask for CC (ID)
                    user_id_document = input("\n\033[34m >> \033[0mEnter your CC number: ")

                    # Validate empty field
                    error = validations.validate_not_empty(user_id_document, "CC Number")
                    if error:
                        print(error)
                        continue

                    # Validate that input contains only numbers
                    error = validations.validate_only_numbers(user_id_document, "CC Number")
                    if error:
                        print(error)
                        continue

                    # Validate duplicate ID in database
                    error = validations.validate_duplicate_id(user_id_document, database.customer_database)
                    if error:
                        print(error)
                        continue  

                    # Validate numeric length (between 6 and 10 digits)
                    error = validations.validate_numeric_length(user_id_document, "CC Number", 6, 10)
                    if error:
                        print(error)
                        continue

                    # Exit loop if all validations pass
                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # ===== INPUT: FULL NAME =====
                while True:

                    # Ask for full name
                    user_full_name = input("\n\033[34m >> \033[0mEnter your full name: ")

                    # Validate empty field
                    error = validations.validate_not_empty(user_full_name, "Full Name")
                    if error:
                        print(error)
                        continue  

                    # Validate that input contains only letters
                    error = validations.validate_only_letters(user_full_name, "Full Name")
                    if error:
                        print(error)
                        continue
                        
                    # Exit loop if valid
                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # ===== INPUT: EMAIL =====
                while True:

                    # Ask for email
                    user_email = input("\n\033[34m >> \033[0mEnter your email: ")
                        
                    # Validate empty field
                    error = validations.validate_not_empty(user_email, "Email")
                    if error:
                        print(error)
                        continue  

                    # Validate email format
                    error = validations.validate_email_format(user_email)
                    if error:
                        print(error)
                        continue

                    # Validate duplicate email in database
                    error = validations.validate_duplicate_data(user_email, database.customer_database, "email", "Email")
                    if error:
                        print(error)
                        continue  
                        
                    # Exit loop if valid
                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # ===== INPUT: PHONE NUMBER =====
                while True:

                    # Ask for phone number
                    user_phone = input("\n\033[34m >> \033[0mEnter your phone number: ")
                        
                    # Validate empty field
                    error = validations.validate_not_empty(user_phone, "Phone Number")
                    if error:
                        print(error)
                        continue  

                    # Validate that input contains only numbers
                    error = validations.validate_only_numbers(user_phone, "Phone Number")
                    if error:
                        print(error)
                        continue

                    # Validate duplicate phone number in database
                    error = validations.validate_duplicate_data(user_phone, database.customer_database, "phone", "Phone Number")
                    if error:
                        print(error)
                        continue
                        
                    # Exit loop if valid
                    break

                # Visual separator
                print("\n\033[34m" + "-"*60 + "\033[0m")

                # ===== CREATE CUSTOMER =====
                # Call function to store customer in database and history
                customer_registration(user_id_document, user_full_name, user_email, user_phone,customer_history)


                # Ask user if they want to exit registration
                exit = utilities.confirm_exit()
                if exit == True:
                    cr_act = False
                else:
                    continue
                
                # ===== CUSTOMER CREATION HISTORY =====

                # Print header for customer creation history
                print("\n\033[34m" + "-"*80)
                print("CUSTOMER CREATION HISTORY")
                print("\033[34m" + "-"*80)
                print(f"{'ID':<5} {'CC':<12} {'NAME':<15} {'EMAIL':<25} {'PHONE':<10}")
                print("-"*80 + "\033[0m")

                # Iterate over created customers and display them
                for cc, data in customer_history.items():
                    print(
                        f"\033[1;32m{data['auto_id']:<5} {cc:<12} {data['name']:<15} {data['email']:<25} {data['phone']:<10}\033[0m"
                    )
                    print("\033[34m" + "-"*80 + "\033[0m")

                # Reset customer history after displaying
                customer_history = {}

                # Final separator
                print("\033[34m" + "-"*60 + "\033[0m\n")


def customer_registration(customer_id, customer_name, customer_email, customer_phone,customer_history):
    """
    Function: customer_registration

    Parameters:

    - customer_id:
    Represents the customer's identification number (ID or "cédula").
    It is used as a unique identifier for each customer in the system.

    - customer_name:
    Stores the full name of the customer.

    - customer_email:
    Contains the customer's email address (e.g., Gmail or any valid email).
    This is used for contact or notification purposes.

    - customer_phone:
    Represents the customer's phone number.
    It can be used for direct communication or verification.

    - customer_history:
    A dictionary structure used to store and manage the history
    of registered customers. This may include past interactions,
    orders, or any relevant data associated with each customer.
    """


    # Generate auto-incremental ID based on database size
    id_customer = len(database.customer_database)+1
                
    # Store customer in main database
    database.customer_database[customer_id] = {
        "auto_id": id_customer,
        "name": customer_name,
        "email": customer_email,
        "phone" : customer_phone,
        "state" : True
    }

    # Store customer in temporary history dictionary
    customer_history[customer_id] = {
        "auto_id": id_customer,
        "name": customer_name,
        "email": customer_email,
        "phone" : customer_phone,
        "state" : True
        }

    # Return confirmation of successful registration
    return True