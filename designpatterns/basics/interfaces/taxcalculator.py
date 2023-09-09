from typing import Protocol


class TaxCalculator(Protocol):
    def calculate_tax(self) -> int:
        ...
