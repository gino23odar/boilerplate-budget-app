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
    values = []  
  # get the value for each category 
    for cat in categories:
        total = 0
        for withdrawal in cat.ledger:
            if withdrawal['amount'] < 0:
                total += withdrawal['amount']
        values.append(total)

    total_neg = sum(values)

  # round the values to get the number of dots in chart
    def o_amount(x):
        portion = x/total_neg * 10
        rounded_down = int(portion) *10
        return rounded_down

    chart_values = list(map(o_amount, values))

  # function to sketch the chart
    def create_chart(vals):
        chart_str = ""
        for i in range(100, -10, -10):
            if i == 100:
                chart_str += "100| "
            elif i == 0:
                chart_str += "  0| "
            else:
                chart_str += str(i).rjust(3) + "| "
    
            for value in vals:
                if value >= i:
                    chart_str += "o  "
                else:
                    chart_str += "   "
    
            chart_str += "\n"
    
        chart_str += "    " + "-" * (len(vals) * 3 + 1) + "\n"
        chart_str += "    "
    
        return chart_str

  # add the names of the categories
    names = []
    for cat in categories:
      names.append(cat.name)
    max_length = max(len(string) for string in names)

    output = ''
    
    # Iterate over each string and each character in each string and add it to the output string
    for i in range(max_length):
        output += ' '
        for string in names:
            if i < len(string):
                output += string[i] + '  '
            else:
                output += '   '
        output += '\n' + ' '*4

    chart = 'Percentage spent by category\n' + create_chart(chart_values) + output.rstrip()

    return chart