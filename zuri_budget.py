class budget:
    def __init__(self, budget):
        self.name = budget
        self.ledger = list()
        self.total_fund = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": round(float(amount), 2), "description": description})
        self.total_fund = self.total_fund + amount
        return self.total_fund

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -1 * round(float(amount), 2), "description": description})
            self.total_fund = self.total_fund - amount
            return True
        else:
            return False

    def compute_balance(self):
        return self.total_fund

    def transfer(self, amount, category):
        if self.check_funds(amount) is True:
            self.withdraw(amount, "Transfer to" + category.name)
            category.deposit(amount, "Transfer from " + category.name)
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

    # def __str__(self):
    #         y = "{:*^30s}".format(f"{self.budget}") + "\n"
    #         for item in self.ledger:
    #             y = y + f"{item['description'][:23].ljust(23)}"+ "{:.2f}".format(item['amount']).rjust(7) + "\n"
    #         total = self.compute_balance()
    #         y = y + "Total: " + "{:.2f}".format(total)
    #         return y


food = budget("Food")
food.deposit(2000, "initial deposit")
print(food.compute_balance())
food.withdraw(100, 'weekly budget')
print(food.compute_balance())

clothing = budget("Clothing")
clothing.deposit(1500, "initial deposit")
clothing.transfer(500, food)
clothing.withdraw(70.55)
clothing.withdraw(50)

print(clothing.compute_balance())
print(food.get_withdrawals())
print(food.ledger)

entertainment = budget("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(150)
food.transfer(780, entertainment)
print(entertainment.ledger)
print(entertainment.compute_balance())
print(food.compute_balance())
