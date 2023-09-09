#################################
### Use basics.classes module ###
#################################
from designpatterns.basics.classes import User

print(User.default_employer)  # output: abc
print(User.get_default_employer())  # output: abc

user1 = User("name1")
print(user1.name)  # output: name1
print(user1.default_employer)  # output: abc
print(user1.say_hello())  # output: Hello name1!

user2 = User("name2")
print(user2.name)  # output: name2
print(user2.default_employer)  # output: abc
print(user2.say_hello())  # output: Hello name2!

User.default_employer = "enb"
print(user1.default_employer)  # output: enb
print(user2.default_employer)  # output: enb
print(user1.get_default_employer())  # output: enb
print(user2.get_default_employer())  # output: enb

# user3 = User()  # Raises TypeError because of missing required argument for constructor

####################################
### Use basics.interfaces module ###
####################################
from designpatterns.basics.interfaces.taxfunctions import calculate_tax
from designpatterns.basics.interfaces.taxcalculator2021 import TaxCalculator2021
from designpatterns.basics.interfaces.taxcalculator2022 import TaxCalculator2022

tax2021 = TaxCalculator2021("tax_data")
tax2022 = TaxCalculator2022("tax_data")

print(calculate_tax(tax2021))
print(calculate_tax(tax2022))
