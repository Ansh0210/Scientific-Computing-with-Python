class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        display = f"{self.name.center(30, '*')}\n"
        
        for item in self.ledger:
            display = display + f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        
        total = self.get_balance()
        display = display + f"Total: {total:.2f}"
        
        return display

    def deposit(self, amount, description=""):
        self.ledger.append({'amount':amount, 'description':description})
        
    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        
        self.ledger.append({'amount':-amount, 'description':description})
        return True
        
    def get_balance(self):
        
        balance = 0
        
        for dep_with in self.ledger:
            balance += dep_with['amount']
            
        return balance    
        
    
    def transfer(self, amount, budg_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {budg_category.name}')
            budg_category.deposit(amount, f'Transfer from {self.name}') 
            return True
        return False
    
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False

def create_spend_chart(categories):
    
    start = "Percentage spent by category"
    
    categ_spent = []
    
    for  categ in categories:
        spent_money = 0
        
        for item in categ.ledger:
            if item['amount'] < 0:
                spent_money += abs(item['amount'])
        
        categ_spent.append(spent_money) 
    
    total_spent_all = sum(categ_spent)
    spent_percent = [(i/total_spent_all) * 100 for i in categ_spent]
    #rounded_percent = [(val//10) * 10 for val in spent_percent]
    
    for i in range(100, -1, -10):
        start += f"\n{i:>3}|"

        for val in spent_percent:
            if val > i:
                start += ' o '
            else:
                start += '   '
        
        start += ' '
        
    start += "\n    ----------" #f"\n    {'-' * (len(rounded_percent) * 3 + 1)}"        
    
    categ_name_length = []
    for categ in categories:
        categ_name_length.append(len(categ.name))
    
    max_row_len = max(categ_name_length)
    
    for row_sec_half in range(max_row_len):
        start += "\n    "
        
        for i in range(len(spent_percent)):
            if row_sec_half < categ_name_length[i]:
                start += f" {categories[i].name[row_sec_half]} "
            else:
                start += "   "
        
        start += ' '
    
    return start
    


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# food.deposit(2, 'test deposit')
# food.get_balance()
# food.check_funds(50)
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(300, 'Paycheck came in')
clothing.withdraw(65, 'Nike Sweats')
clothing.transfer(30, food)
auto = Category("Auto")
auto.deposit(100, "deposit")
clothing.transfer(50, auto)
auto.withdraw(70, 'car spray')



print(food)
print(clothing)
# print(auto)

print(create_spend_chart((food, clothing, auto))) #
