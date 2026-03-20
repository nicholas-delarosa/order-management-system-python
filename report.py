import database
import csv

# Dictionary that will store the final report rows
report_data = {}

# References to databases
customers_db = database.customer_database
orders_db = database.order_database

# Global accumulators
total_daily_revenue = 0
total_registered_products = 0

# Iterate through all customers
for customer_cc, customer_info in customers_db.items():

    # Extract customer information
    customer_id = customer_info.get('auto_id')
    customer_name = customer_info.get('name')

    # Add header row for customer information
    row_id = len(report_data) + 1
    report_data[row_id] = ("ID","CUSTOMER NAME","N° IDENTIFICATION")

    # Add customer data row
    row_id = len(report_data) + 1
    report_data[row_id] = (customer_id, customer_name, customer_cc)

    # Add header for product details
    row_id = len(report_data) + 1
    report_data[row_id] = ("PRODUCT ID", "PRODUCT NAME", "QUANTITY", "UNIT PRICE", "TOTAL")

    # Counters per customer
    product_counter = 1
    customer_total = 0

    # Iterate through all orders
    for order_id, order_data in orders_db.items():
        product_counter = 1

        # Get customer ID associated with the order
        order_customer_cc = order_data['cc']

        # Check if the order belongs to the current customer
        if order_customer_cc == customer_cc:

            # Iterate through order fields
            for field_key, product_data in order_data.items():

                # Validate dynamic product keys (producto1, producto2, etc.)
                if field_key == "producto" + str(product_counter):
                    product_counter += 1

                    # Add product row to report
                    row_id = len(report_data) + 1
                    report_data[row_id] = (
                        product_data[0],
                        product_data[1],
                        product_data[2],
                        product_data[3] / product_data[2],
                        product_data[3]
                    )

                    # Accumulate totals
                    customer_total += product_data[3]
                    total_daily_revenue += product_data[3]
                    total_registered_products += 1

    # Add total per customer
    row_id = len(report_data) + 1
    report_data[row_id] = ("TOTAL CAT", customer_total)

    # Empty row (visual separation)
    row_id = len(report_data) + 1
    report_data[row_id] = (" ")

# Add global totals (repeated per customer)
row_id = len(report_data) + 1
report_data[row_id] = ("TOTAL DAILY REVENUE", total_daily_revenue)

row_id = len(report_data) + 1
report_data[row_id] = ("TOTAL REGISTERED PRODUCTS", total_registered_products)


def generate_final_report(filename="final_report.csv"):

    # Open CSV file in write mode
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write each row from the report dictionary
        for row in report_data.values():
            writer.writerow(row)

    # Success message
    print(f"\n\033[1;32mFinal report generated successfully as '{filename}'.\033[0m")
