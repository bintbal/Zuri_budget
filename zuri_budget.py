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
        y = "{:*^30s}".format(f"{self.budget}") + "\n"
        for item in self.ledger:
            y = y + f"{item['description'][:23].ljust(23)}"+ "{:.2f}".format(item['amount']).rjust(7) + "\n"
        total = self.compute_balance()
        y = y + "Total: " + "{:.2f}".format(total)
        return y


food = budget("Food")
food.deposit(1000, "initial deposit")
food.withdraw(100, 'weekly budget')


clothing = budget("Clothing")
food.deposit(500, "initial deposit")
clothing.transfer(500, clothing)
clothing.withdraw(70.55)
clothing.withdraw(50)


entertainment = budget("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(150)
