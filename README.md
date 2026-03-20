# Order Management System — Python

A command-line application for managing customers, products, and orders in a retail environment. Built entirely in Python using in-memory dictionaries, this system covers the full lifecycle of a sales operation: from customer and product registration to order processing and daily report generation.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Data Model](#data-model)
- [Modules](#modules)
- [Validation Rules](#validation-rules)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Output](#output)

---

## Overview

This project simulates a basic point-of-sale (POS) backend through a terminal interface. The user navigates a numbered menu to perform operations such as registering new customers, adding products to a catalog, creating orders, and generating end-of-day financial reports exported as CSV files.

All data is stored in-memory using Python dictionaries and tuples — no external database or framework is required.

---

## Project Structure

```
order-management-system-python/
│
├── main.py            # Entry point — main menu loop
├── database.py        # In-memory data stores (customers, products, orders, categories)
├── customers.py       # Customer registration logic
├── products.py        # Product registration logic
├── orders.py          # Order creation and product-to-order assignment
├── orders_view.py     # View all orders associated with a customer
├── daily_totals.py    # Daily income summary across all orders
├── report.py          # Final report builder and CSV exporter
├── validations.py     # Reusable input validation functions
├── utilities.py       # UI helpers (title display, confirmation prompts, list rendering)
└── final_report.csv   # Sample exported report
```

---

## Features

- **Customer Registration** — Register new customers with ID (CC), full name, email, and phone number. Duplicate detection is enforced for all unique fields.
- **Product Registration** — Add products with name, price, stock, and category. Categories are selected from a predefined list of 12 options.
- **Order Creation** — Create orders by linking a registered customer to one or more products, with real-time stock validation.
- **Order Viewing** — Look up all orders placed by a specific customer, displayed in a structured table.
- **Daily Income Calculation** — Aggregate and display the total revenue across all orders for the current session.
- **Final Report Generation** — Export a full breakdown of customers, their orders, product details, and totals to a `final_report.csv` file.

---

## Data Model

### Customer

| Field     | Type    | Description                         |
|-----------|---------|-------------------------------------|
| `auto_id` | `int`   | Auto-incremented internal identifier |
| `name`    | `str`   | Customer's full name                |
| `email`   | `str`   | Unique email address                |
| `phone`   | `str`   | Contact phone number                |
| `state`   | `bool`  | Account active status               |

**Key:** Colombian national ID number (CC), stored as a string (6–10 digits).

### Product

Products are stored as tuples: `(name, price, stock, category)`

| Index | Type    | Description           |
|-------|---------|-----------------------|
| `[0]` | `str`   | Product name          |
| `[1]` | `float` | Unit price            |
| `[2]` | `int`   | Available stock       |
| `[3]` | `str`   | Category label        |

### Order

Each order is a dictionary containing customer identifiers and dynamically keyed product entries (`producto1`, `producto2`, etc.):

```python
{
    "cc": "123456",
    "name": "Jesus Lucena",
    "producto1": (product_id, product_name, quantity, total_price),
    "producto2": (...)
}
```

### Product Categories

The system supports 12 predefined categories:

`Electronics`, `Appliances`, `Groceries`, `Clothing`, `Footwear`, `Health & Beauty`, `Home & Furniture`, `Stationery`, `Toys`, `Sports`, `Automotive`, `Hardware & Tools`

---

## Modules

### `main.py`
Entry point of the application. Runs a `while` loop that renders the main menu and routes user input to the appropriate module function.

### `database.py`
Defines all in-memory data structures:
- `customer_database` — dictionary of registered customers
- `product_database` — dictionary of registered products
- `order_database` — dictionary of all created orders
- `product_categories` — tuple of available category names

Pre-populated with sample data for testing purposes.

### `customers.py`
Handles the `Customer Registration` flow. Collects and validates CC number, full name, email, and phone. Stores the result in `database.customer_database` and displays a session history table after each batch registration.

### `products.py`
Handles the `Product Registration` flow. Collects and validates product name, price (float), stock (integer, must be > 3), and category (selected by number). Stores results in `database.product_database`.

### `orders.py`
Handles `Order Creation`. Validates that the customer exists, then allows adding multiple products to a single order. Calculates line totals (`quantity × unit price`) and validates stock availability, preserving a minimum buffer of 3 units per product.

### `orders_view.py`
Allows a customer to view all of their orders by entering their CC number. Filters `order_database` and displays a formatted table of products, quantities, unit prices, and totals.

### `daily_totals.py`
Iterates over all orders in `order_database` and accumulates a grand total revenue figure for the session. Prints an order-by-order breakdown followed by the final daily profit.

### `report.py`
Builds a structured report dictionary by joining customers with their respective orders and products. Exports the result to `final_report.csv` using Python's built-in `csv` module. The report includes per-customer subtotals and global session totals.

### `validations.py`
A collection of reusable validation functions used across all modules:

| Function | Description |
|---|---|
| `validate_not_empty` | Ensures a field is not blank |
| `validate_duplicate_id` | Checks for duplicate keys in a database dict |
| `validate_duplicate_data` | Checks for duplicate values in a specific field |
| `validate_email_format` | Validates email using a regex pattern |
| `validate_numeric_length` | Ensures a numeric string is within a length range |
| `validate_only_letters` | Rejects input containing non-alphabetic characters |
| `validate_only_numbers` | Rejects input containing non-numeric characters |
| `validate_cuantiti_negative` | Rejects zero or negative values |
| `validate_stock_above_minimum` | Enforces a minimum stock threshold |
| `validate_category_option` | Validates that a selection falls within a valid index range |
| `validate_sale` | Checks if requested quantity is available considering the stock reserve |

All functions return an error string when validation fails, or `None` on success.

### `utilities.py`
Provides three shared UI helpers:
- `title(text)` — Renders a centered, padded section header in blue
- `confirm_exit(message)` — Prompts the user to confirm whether they want to stop the current operation
- `iterate_list(collection)` — Displays an enumerated list (used for category selection)

---

## Validation Rules

| Field | Rule |
|---|---|
| CC Number | Numeric only, 6–10 digits, unique across all customers |
| Full Name | Letters and spaces only, cannot be empty |
| Email | Must match `user@domain.ext` pattern, must be unique |
| Phone Number | Numeric only, cannot be empty, must be unique |
| Product Price | Numeric (float), must be ≥ 1 |
| Product Stock | Integer, must be > 3 |
| Order Quantity | Integer, must be ≥ 1 and must not exceed `(available stock − 3)` |
| Category Selection | Must be a valid integer within the displayed range |

---

## Getting Started

### Requirements

- Python 3.6 or higher
- No external libraries required

### Running the Application

```bash
# Clone the repository
git clone -b develop https://github.com/nicholas-delarosa/order-management-system-python.git
cd order-management-system-python

# Run the application
python main.py
```

---

## Usage

Upon running the application, the main menu is displayed:

```
------------------ Menu Options ------------------

    1. Customer Registration
    2. Product Registration
    3. Order Creation
    4. View Registered Orders
    5. Daily Income Calculation
    6. Final Report Generation

    7. Exit
```

Enter the number of the desired option and follow the on-screen prompts. Each module validates all input in real time and displays descriptive error messages when invalid data is entered.

> **Recommended flow:** Register customers (1) → Register products (2) → Create orders (3) → View orders (4) → Calculate daily income (5) → Generate report (6)

---

## Output

### Terminal

All tables and summaries are displayed with color-coded output using ANSI escape codes:
- **Blue** — Section headers, separators, and prompts
- **Green** — Successfully created records
- **Red** — Error messages and the exit option

### CSV Report (`final_report.csv`)

The exported report groups data by customer and includes:

```
ID, CUSTOMER NAME, N° IDENTIFICATION
1, Jesus Lucena, 123456
PRODUCT ID, PRODUCT NAME, QUANTITY, UNIT PRICE, TOTAL
1, Pan, 5, 12.0, 60.0
2, Queso, 2, 20.0, 40.0
TOTAL CAT, 100.0

TOTAL DAILY REVENUE, 100.0
TOTAL REGISTERED PRODUCTS, 2
```

---

## Authors

Developed by:
* [Nicholas De la Rosa](https://github.com/nicholas-delarosa)
* [Aura Alean](https://github.com/auraalean56)
* [Jorge Carmona](https://github.com/Envy528)
* [Jesus Lucena](https://github.com/JesusLucena-png)
* [Julian Valenzuela](https://github.com/julianvlz21)
* [Luis Pozzo](https://github.com/LuisPozzo)
* [Alejandro Nova](https://github.com/Nova-Alejandro)
* [Daniel Chacón](https://github.com/Rekiel7)
* [Andres Quintero](https://github.com/TheplexyBoy)
