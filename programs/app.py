
from budget import Budget

food_budget = Budget('Food', 400, 50)
print(food_budget)

clothing_budget = Budget('Clothes', 200, 100)
print(clothing_budget)

entertainment_budget = Budget('Entertainment', 100, 20)
print(entertainment_budget)

clothing_budget.addToBudget(30)
print(clothing_budget)

print(clothing_budget.withdrawFromBudget(450))
print(clothing_budget)

print(clothing_budget.withdrawFromBudget(150))
print(clothing_budget)

print(clothing_budget.transferToOther(500, food_budget))
print(food_budget)