from .taxcalculator import TaxCalculator


def calculate_tax(calculator: TaxCalculator) -> int:
    # This function is dependant on Protocol
    # and not on any concrete implementation
    return calculator.calculate_tax()
