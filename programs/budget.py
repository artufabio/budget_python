

# creates Budget class

class Budget():
    def __init__(self, type_, balance, max_allowance_withdraw):
        self.type_ = type_
        self.balance = balance
        self.max_allowance_withdraw = max_allowance_withdraw
        self.file_ = self.createInfoFile()

    def __repr__(self):
        return f'Budget: {self.type_}.\nBalance: {self.balance}'

    # add money to balance 
    def addToBudget(self, amount):
        self.balance += amount
        return self.balance

    # withdraw from balance
    def withdrawFromBudget(self, amount):
        if self.balance < amount:
            return 'Oooops! Seems like you do not have enough money to withdraw. Please add some to your budget'
        elif amount > self.max_allowance_withdraw:
            return f'Sorry, you are not allow to withdraw this amount of money. Your limit is {self.max_allowance_withdraw}'
        else:
            self.balance -= amount
            return amount 

    # transfer money to another budget
    def transferToOther(self, amount, budget_to_feed):
        amount_to_transfer = self.withdrawFromBudget(amount)
        if type(amount_to_transfer) == "<class 'int'>":
            return budget_to_feed.addToBudget(amount_to_transfer)
        else:
            return amount_to_transfer

    # Create a file in which I can store the type of budget and its balance
    def createInfoFile(self):
        file1 = open(f'{self.type_}_budget.txt', 'w')
        file1.write(f'Budget type: {self.type_}\n')
        file1.write(f'Balance: {self.balance}')
        file1.close()