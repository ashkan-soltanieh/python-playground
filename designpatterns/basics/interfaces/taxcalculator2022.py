from .taxcalculator import TaxCalculatorABC


# Protocols approach -> no need to reference protocol TaxCalculator Class just make sure you implemented it's method
class TaxCalculator2022Protocol:
    def __init__(self, tax_data):
        self.tax_data = tax_data

    def calculate_tax(self) -> int:
        return 2022


# ABC approach -> You need to inherit from TaxCalculatorABC explicitly
class TaxCalculator2022ABC(TaxCalculatorABC):
    def __init__(self, tax_data):
        self.tax_data = tax_data

    def calculate_tax(self) -> int:
        return 2022 