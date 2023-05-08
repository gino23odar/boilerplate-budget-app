class Category:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.ledger = []

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def deposit(self, amount, description=''):
        desc = {'amount': amount, 'description': description}
        self.ledger.append(desc)
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            desc = {'amount': -amount, 'description': description}
            self.ledger.append(desc)
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            withdrawal_desc = "Transfer to " + category.name
            deposit_desc = "Transfer from " + self.name
            self.withdraw(amount, withdrawal_desc)
            category.deposit(amount, deposit_desc)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        total = 0
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amt = '{:.2f}'.format(item['amount']).rjust(7)
            items += desc + amt + '\n'
            total += item['amount']
        output = title + items + 'Total: {:.2f}'.format(total)
        return output
     

def create_spend_chart(categories):
    return 