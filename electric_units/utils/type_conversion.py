"Functions for converting between different data types."
from decimal import Decimal

def to_decimal(value):
    "Converts integers, floats or string representations of either to Decimal"
    if isinstance(value, float):
        decimal_value = Decimal.from_float(value)
    elif isinstance(value, int):
        decimal_value = Decimal(value)
    elif isinstance(value, str):
        try:
            decimal_value = Decimal.from_float(float(value))
        except TypeError:
            raise TypeError("Invalid value, argument must be int or float")
    elif isinstance(value, Decimal):
        decimal_value = value
    else:
        raise TypeError("Invalid value, argument must be int or float")

    return decimal_value
