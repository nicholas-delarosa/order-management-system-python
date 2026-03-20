import re

# Validates that a field is not empty or blank
def validate_not_empty(field_value, field_name):
    """
    Function: validate_not_empty

    Parameters:

    - field_value:
    Represents the input value provided by the user that needs to be validated.

    - field_name:
    Indicates the name of the field being validated.
    It is used to generate a personalized message in case the field is empty.

    Description:
    This function checks if the given input value is empty.
    If it is empty, it uses the field name to display a customized
    validation message.
    """

    if not str(field_value).strip():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} cannot be empty. Please enter a valid value." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that an ID does not already exist in the database
def validate_duplicate_id(field_value, database):
    """
    Function: validate_duplicate_id

    Parameters:

    - field_value:
    Represents the input value (ID) provided by the user that needs to be validated.

    - database:
    Dictionary where the IDs are stored.
    It is used to check if the given ID already exists.

    Description:
    This function verifies whether the provided ID already exists
    in the database, preventing duplicate entries in the system.
    """

    if field_value in database:
        return ("\n\033[1;31m" + "-"*60 + "\nError: This ID already exists. Please enter a different ID." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that a specific field value is not duplicated in the database
def validate_duplicate_data(field_value, database, key, field_name):
    """
    Function: validate_duplicate_data

    Parameters:

    - field_value:
    Represents the input value that needs to be checked for duplication.

    - database:
    Dictionary where the data is stored and will be validated.

    - key:
    Represents the key of the element inside the dictionary
    that will be used for comparison.

    - field_name:
    Indicates the name of the field being validated.
    It is used to generate a personalized validation message.

    Description:
    This function checks if a specific value already exists within
    a given key in the database, helping to prevent duplicate data
    entries and providing a customized message if duplication is detected.
    """
    
    # Iterate through all records in the database
    for data in database.values():

        # Compare the input value with the specified field
        if field_value == data.get(key):
            return ("\n\033[1;31m" + "-"*60 + f"\nError: This {field_name} is already registered. Please use a different one." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates email format using a regular expression
def validate_email_format(email):
    """
    Function: validate_email_format

    Parameters:

    - email:
    Represents the email input provided by the user.
    It is used to validate whether the format of the email is correct.

    Description:
    This function checks if the given email follows a valid format
    (e.g., contains '@' and a domain), ensuring it is a properly
    structured email address.
    """

    # Regex pattern for validating email structure
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Check if email matches the pattern
    if not re.match(pattern, email):
        return ("\n\033[1;31m" + "-"*60 + "\nError: Invalid email format. Please enter a valid email (e.g., user@gmail.com)." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that a numeric field contains only digits and is within a length range
def validate_numeric_length(field_value, field_name, min_len, max_len):
    """
    Function: validate_numeric_length

    Parameters:

    - field_value:
    Represents the input value to be validated.

    - field_name:
    Indicates the name of the field being validated.
    It is used to generate a personalized validation message.

    - min_len:
    Represents the minimum allowed number of characters.

    - max_len:
    Represents the maximum allowed number of characters.

    Description:
    This function validates that the length of the input (number of characters)
    is within the allowed range, between the minimum and maximum limits.
    """

    # Check if the length is within the allowed range
    if len(field_value) < min_len or len(field_value) > max_len:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must be between 6 and 8 digits." + "\n" + "-"*60 + "\033[0m")

    return None

# Validates that a field contains only alphabetic characters (letters and spaces)
def validate_only_letters(field_value, field_name):
    """
    Function: validate_only_letters

    Parameters:

    - field_value:
    Represents the input value that will be validated.

    - field_name:
    Indicates the name of the field being validated.
    It is used to generate a personalized validation message.

    Description:
    This function checks that the input contains only alphabetic
    characters (letters), preventing numbers or special characters.
    If the validation fails, it uses the field name to display
    a customized message.
    """

    # Remove spaces and check if remaining characters are letters
    if not field_value.replace(" ", "").isalpha():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must contain only letters (no numbers)." + "\n" + "-"*60 + "\033[0m")

    return None

# Validates that a field contains only numeric characters
def validate_only_numbers(field_value, field_name):
    """
    Function: validate_only_numbers

    Parameters:

    - field_value:
    Represents the input value that will be validated.

    - field_name:
    Indicates the name of the field being validated.
    It is used to generate a personalized validation message.

    Description:
    This function checks that the input contains only numeric
    characters (digits), preventing letters or special characters.
    If the validation fails, it uses the field name to display
    a customized message.
    """

    if not field_value.isdigit():
        return ("\n\033[1;31m" + "-"*60 + f"\nError: {field_name} must contain only numbers." + "\n" + "-"*60 + "\033[0m")

    return None

# Validates that a numeric value is not negative
def validate_cuantiti_negative(field_value):
    """
    Function: validate_cuantiti_negative

    Parameters:

    - field_value:
    Represents the numeric value that will be validated.

    Description:
    This function checks that the given value is not negative.
    It ensures that quantities (such as product amounts) are zero
    or positive, preventing invalid negative inputs.
    """

    if field_value < 1:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: The entered value cannot be negative or zero." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that stock is above a minimum threshold
def validate_stock_above_minimum(field_value, num):
    """
    Function: validate_stock_above_minimum

    Parameters:

    - field_value:
    Represents the value to be validated (current stock or quantity).

    - num:
    Represents the minimum allowed stock value.

    Description:
    This function checks that the given value is greater than or equal
    to the minimum allowed stock, ensuring that the quantity does not
    fall below the defined limit.
    """

    if field_value <= num:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Stock must be greater than the minimum allowed (3 units). Please enter a value above 3." + "\n" + "-"*60 + "\033[0m")
    
    return None

# Validates that a selected option is within a valid range
def validate_category_option(field_value, min, max):
    """
    Function: validate_category_option

    Parameters:

    - field_value:
    Represents the input value (usually an option selected by the user).

    - min:
    Represents the minimum allowed value or option.

    - max:
    Represents the maximum allowed value or option.

    Description:
    This function validates that the selected value is within a valid range
    (between min and max). It is commonly used to ensure that a user-selected
    option from a list falls within the allowed limits.
    """

    if field_value < min or field_value > max:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Value out of allowed range." + "\n" + "-"*60 + "\033[0m")

    return None

# Validates if a sale can be made based on available stock
def validate_sale(stock, min_stock, quantity):
    """
    Function: validate_sale

    Parameters:

    - stock:
    Represents the current available stock of the product.

    - min_stock:
    Represents the minimum allowed stock level.

    - quantity:
    Represents the quantity the customer wants to purchase.

    Description:
    This function validates that the requested quantity does not exceed
    the available stock and ensures that the stock will not fall below
    the minimum allowed level after the sale.
    """
    
    # Calculate available stock after reserving minimum stock
    available_stock = stock - min_stock
    
    # Check if requested quantity exceeds available stock
    if quantity > available_stock:
        return ("\n\033[1;31m" + "-"*60 + f"\nError: Only {available_stock} units available for sale." + "\n" + "-"*60 + "\033[0m")
    
    return None