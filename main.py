import os
import utilities
import customers
import products
import orders
import orders_view
import daily_totals
import report

# ==============================
# MAIN OPTIONS MENU
# ==============================

def main():
    # Display the menu title using a utility function
    utilities.title("Menu Options")

    # Print the list of available options for the user
    print("""
\033[34m    1.\033[0m Customer Registration
\033[34m    2.\033[0m Product Registration
\033[34m    3.\033[0m Order Creation
\033[34m    4.\033[0m View Registered Orders
\033[34m    5.\033[0m Daily Income Calculation
\033[34m    6.\033[0m Final Report Generation
            
\033[31m    7.\033[0m Exit
    """)

    # Print a separator line
    print("\033[34m" + "-"*60 + "\033[0m\n")

# Control variable to keep the program running
ws = True 

# Main loop of the program
while ws:

    # Show the main menu
    main()

    # Ask the user to select an option
    option = input("\033[34m >> \033[0mEnter an Option: ")

    # Print a separator line
    print("\n\033[34m" + "-"*60 + "\033[0m")

    # Clear the console screen depending on the operating system
    os.system("cls" if os.name == "nt" else "clear")

    # Option 1: Call customer registration function
    if option == "1":

        customers.Customer_Registration()

    # Option 2: Call product registration function
    elif option == "2":
            
        products.Product_Registration()
        
    # Option 3: Call order creation function
    elif option == "3":

        orders.Order_Creation()

    # Option 4: Display registered orders
    elif option == "4":

        orders_view.View_Registered_Orders()
           
    # Option 5: Calculate daily income
    elif option == "5":
        daily_totals.Daily_Income_Calculation()

    # Option 6: Generate final report
    elif option == "6":
        report.generate_final_report()

    # Option 7: Exit the program
    elif option == "7":
        ws = False

    # Handle invalid input
    else:
        print("\n\033[1;31m" + "-"*60)
        print("Error: Invalid Value Entered. Enter an option between 1 and 7")
        print("-"*60 + "\033[0m")