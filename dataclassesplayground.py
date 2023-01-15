from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
          raise ValueError("Age must be positive")
    
    def __post_init__(self):
        if len(self.name) != 4:
            raise ValueError("Name must only have four letters")
    
    @property
    def birth_year(self):
        return 2023 - self.age

p = Person(name="John", age=100)
print(p.age) # -> 100
print(p.birth_year) # -> 1923