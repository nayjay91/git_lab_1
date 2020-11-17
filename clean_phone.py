import pandas as pd

def validate_phone(phone_number):
    """
    Tests wheter phone numbers are valid

    Arguements:
    Phone number - A Pandas Series of Phone numbers as a string object

    Returns:
    A boolean Pandas Series
    """
    bool_phone = phone_number.str.contains(r"^\d{3}[-]?\d{3}[-]?\d{4}")
    return bool_phone

numbers = pd.Series(['156-152-1111','456-852-4562','(234)2346323'])
print(validate_phone(numbers))