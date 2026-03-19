import re

# Validates that a field is not empty or blank
def validate_not_empty(field_value, field_name):

    if not str(field_value).strip():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} cannot be empty. Please enter a valid value." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that an ID does not already exist in the database
def validate_duplicate_id(field_value, database):

    if field_value in database:
        return ("\n\033[1;31m" + "-"*60 + "\nError: This ID already exists. Please enter a different ID." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that a specific field value is not duplicated in the database
def validate_duplicate_data(field_value, database, key, field_name):
    
    # Iterate through all records in the database
    for data in database.values():

        # Compare the input value with the specified field
        if field_value == data.get(key):
            return ("\n\033[1;31m" + "-"*60 + f"\nError: This {field_name} is already registered. Please use a different one." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates email format using a regular expression
def validate_email_format(email):

    # Regex pattern for validating email structure
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Check if email matches the pattern
    if not re.match(pattern, email):
        return ("\n\033[1;31m" + "-"*60 + "\nError: Invalid email format. Please enter a valid email (e.g., user@gmail.com)." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that a numeric field contains only digits and is within a length range
def validate_numeric_length(field_value, field_name, min_len, max_len):

    # Check if the value contains only numbers
    if not field_value.isdigit():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must contain only numbers." + "\n" + "-"*60 + "\033[0m")

    # Check if the length is within the allowed range
    if len(field_value) < min_len or len(field_value) > max_len:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must be between 6 and 8 digits." + "\n" + "-"*60 + "\033[0m")

    return None

# Validates that a field contains only alphabetic characters (letters and spaces)
def validate_only_letters(field_value, field_name):

    # Remove spaces and check if remaining characters are letters
    if not field_value.replace(" ", "").isalpha():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must contain only letters (no numbers)." + "\n" + "-"*60 + "\033[0m")

    return None

# Validates that a field contains only numeric characters
def validate_only_numbers(field_value, field_name):

    if not field_value.isdigit():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must contain only numbers." + "\n" + "-"*60 + "\033[0m")

    return None

# Validates that a numeric value is not negative
def validate_cuantiti_negative(field_value):
    if field_value < 1:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: The entered value cannot be negative or zero." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that stock is above a minimum threshold
def validate_stock_above_minimum(field_value, num):
    if field_value <= num:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Stock must be greater than the minimum allowed (3 units). Please enter a value above 3." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that a selected option is within a valid range
def validate_category_option(field_value, min, max):

    if field_value < min or field_value > max:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Value out of allowed range." + "\n" + "-"*60 + "\033[0m")

    return None

# Validates if a sale can be made based on available stock
def validate_sale(stock, min_stock, quantity):
    
    # Calculate available stock after reserving minimum stock
    available_stock = stock - min_stock
    
    # Check if requested quantity exceeds available stock
    if quantity > available_stock:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Only {available_stock} units available for sale." + "\n" + "-"*60 + "\033[0m")
    
    return None