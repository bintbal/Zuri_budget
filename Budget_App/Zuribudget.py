class budget:
    def __init__(self, budget):
        self.name = budget
        self.ledger = list()
        self.total_fund = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": round(float(amount), 2), "description": description})
        self.total_fund = self.total_fund + amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -1 * round(float(amount), 2), "description": description})
            self.total_fund = self.total_fund - amount
            return True
        else:
            return False

    def compute_balance(self):
        for item in self.ledger:
            self.total_fund += item["amount"]
        return self.total_fund

    def transfer(self, amount, Category, category=None):
        if self.check_funds(amount) is True:
            self.withdraw(amount, "Transfer to" + Category.name)
            category.deposit(amount, "Transfer from" + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        check_amount = amount
        if self.total_fund >= check_amount:
            return True
        else:
            return False


def get_withdrawals(self):
    for item in self.ledger:
        if item["amount"] < 0:
            self.total_fund += item["amount"]
        return self.total_fund


def __str__(self):
    ledger_print = """"""
    for entry in self.ledger:
        ledger_print += str(entry["description"][:23]).ljust(23) + str(format(entry["amount"], '.2f')).rjust(7) + "\n"

    return str(self.category).center(30, "*") + "\n" + ledger_print + 'Total: ' + str(self.balance)


food = budget("Food")
food.deposit(1000, "initial deposit")
food.withdraw(100, 'weekly budget')
print(food.compute_balance())

clothing = budget("Clothing")
clothing.transfer(500, clothing)
clothing.withdraw(70.55)
clothing.withdraw(50)
print(clothing.compute_balance())

entertainment = budget("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(150)
print(entertainment.compute_balance())

print(food)
print(clothing)
print(entertainment)
