from .taxcalculator import TaxCalculator, TaxCalculatorABC


def calculate_tax_protocol(calculator: TaxCalculator) -> int:
    # This function is dependant on Protocol
    # and not on any concrete implementation
    return calculator.calculate_tax()


def calculate_tax_abc(calculator: TaxCalculatorABC) -> int:
    # This function is dependant on Protocol
    # and not on any concrete implementation
    return calculator.calculate_tax()