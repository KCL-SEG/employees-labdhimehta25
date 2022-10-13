"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, description ="", salary=0, commission=0):
        self.name = name
        self.description = description
        self.salary = salary
        self.comission = commission

    def outputPayInfo(self, description):
        self.description = description

    def get_pay(self):
        pass

    def __str__(self):
        return self.description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.outputPayInfo("Billie works on a monthly salary of 4000. Their total pay is 4000.")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.outputPayInfo("Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.")

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.outputPayInfo("Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.")

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.outputPayInfo("Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.")

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.outputPayInfo("Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.")

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.outputPayInfo("Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.")
