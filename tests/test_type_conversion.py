"Testing the type conversion functions"
from decimal import Decimal

from electric_units.utils.type_conversion import to_decimal

def test_to_decimal():
    "Can you create decimal instances from a variety of input dtypes"
    assert Decimal(0.2) == to_decimal("0.2")
    assert Decimal(0.2) == to_decimal(0.2)
    assert Decimal(2) == to_decimal(2)
    assert Decimal(2) == to_decimal("2")
    assert Decimal(2) == to_decimal(Decimal(2))
