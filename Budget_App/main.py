
import budget as bd
food = bd.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(100, "weekly budget")
print(food.get_balance())

clothing = bd.Category("Clothing")
clothing.transfer(500, clothing)
clothing.withdraw(70.55)
clothing.withdraw(50)
print(clothing.get_balance())

entertainment = bd.Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(150)
print(entertainment.get_balance())

print(food)
print(clothing)
print(entertainment)
