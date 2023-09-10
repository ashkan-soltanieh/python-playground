from abc import ABC, abstractmethod
from typing import Protocol


class TaxCalculator(Protocol):
    def calculate_tax(self) -> int:
        ...


class TaxCalculatorABC(ABC):
    @abstractmethod
    def calculate_tax(self) -> int:
        pass