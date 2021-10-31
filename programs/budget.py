

class Budget():
    def __init__(self, type_, budget, max_allowance_withdraw):
        self.type_ = type_
        self.budget = budget
        self.max_allowance_withdraw = max_allowance_withdraw

    def __repr__(self):
        return f'Budget: {self.type_}.\nAvailability: {self.budget}'

    # add money to balance 
    def addToBudget(self, amount):
        self.budget += amount
        return self.budget

    # withdraw from balance
    def withdrawFromBudget(self, amount):
        if self.budget < amount:
            return 'Oooops! Seems like you do not have enough money to withdraw. Please add some to your budget'
        elif amount > self.max_allowance_withdraw:
            return f'Sorry, you are not allow to withdraw this amount of money. Your limit is {self.max_allowance_withdraw}'
        else:
            self.budget -= amount
            return amount 

    # transfer money to another budget
    def transferToOther(self, amount, budget_to_feed):
        amount_to_transfer = self.withdrawFromBudget(amount)
        if type(amount_to_transfer) == "<class 'int'>":
            return budget_to_feed.addToBudget(amount_to_transfer)
        else:
            return amount_to_transfer