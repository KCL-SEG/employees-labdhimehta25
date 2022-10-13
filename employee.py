"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

#class constructor
class Employee:
    def __init__(self, name, description ="", salary=0, commission=0):
        self.name = name
        self.description = description
        self.salary = salary
        self.commission = commission

    #salary is based on fixed monthly pay
    def contractBasedSalary(self, monthlyIncome):
        self.salary = monthlyIncome
        return

    #salary based on the how long they worked for * how much they get paid per hour
    def hourlyBasedSalary(self, hourlyIncome, hoursWorked):
        self.salary = hourlyIncome * hoursWorked
        return

    #commission based on fixed bonus received on top of salary
    def bonusBasedCommission(self, fixedBonusValue):
        self.commission = fixedBonusValue
        return

    #commission based on number of contracts landed * comission per contract
    def contractBasedCommission(self, commissionPerContract, numOfContractsLanded):
        self.commission= commissionPerContract * numOfContractsLanded
        return

    #description = information on how the payement was calaculated
    def outputPayInfo(self, description):
        self.description = description
        return

    def get_pay(self):
        totalpayement = self.salary + self.commission
        return totalpayement

    #outputs informaiton on how the payement was calculated
    def __str__(self):
        return self.description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.outputPayInfo("Billie works on a monthly salary of 4000. Their total pay is 4000.")
billie.contractBasedSalary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.outputPayInfo("Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.")
charlie.hourlyBasedSalary(25,100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.outputPayInfo("Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.")
renee.contractBasedSalary(3000)
renee.contractBasedCommission(200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.outputPayInfo("Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.")
jan.hourlyBasedSalary(25,150)
jan.contractBasedCommission(220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.outputPayInfo("Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.")
robbie.contractBasedSalary(2000)
robbie.bonusBasedCommission(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.outputPayInfo("Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.")
ariel.hourlyBasedSalary(30,120)
ariel.bonusBasedCommission(600)
