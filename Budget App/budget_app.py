class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        display = f"{self.name.center(30, '*')}\n"
        
        for item in self.ledger:
            display = display + f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        
        total = self.get_balance()
        display = display + f"Total: {total:.2f}\n"
        
        return display

    def deposit(self, amount, description=""):
        self.ledger.append({'amount':amount, 'description':description})
        #return self.ledger
        
    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        
        self.ledger.append({'amount':-amount, 'description':description})
        return True
        
    def get_balance(self):
        
        self.first_dep = self.ledger[0]['amount']
        
        for dep_with in self.ledger[1:]:
            self.first_dep = self.first_dep + dep_with['amount']
            
        return self.first_dep    
        
    
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

def create_spend_chart(*categories):
    
    start = "Percentage spent by category"
    
    categ_spent = {}
    #categ_deposit = {}
    
    for  categ in categories:
        spent_money = 0
        #tot_deposit_money = 0
        
        for item in categ.ledger:
            if item['amount'] < 0:
                spent_money += abs(item['amount'])
            continue
            # else:
            #     tot_deposit_money += item['amount']
        
        categ_spent[categ.name] = spent_money
        #categ_deposit[categ.name] = tot_deposit_money
    
    #print(categ_spent)
    # print(categ_spent.values())
    #print(categ_deposit)
    
    # print(list(categ_spent.values()))
    
    total_spent_all = sum(list(categ_spent.values()))
    # print(total_spent_all) 
    
    spent_percent = {key: int((val/total_spent_all) * 100) for key, val in categ_spent.items()}
    rounded_percent = {key: val//10 * 10 for key,val in spent_percent.items()}
    
    for i in range(100, -10, -10):
        start += f"\n{i:>3}|"
        #print(f"{i:>3}|")

        for val in rounded_percent.values():
            if i <= val:
                start += ' o '
            else:
                start += '   '
        
    start += f"\n    {'-' * (len(rounded_percent) * 3 + 1)}"        
    
    #print(max(list(rounded_percent.keys()), key = len))
    
    max_row_len = len(max(list(rounded_percent.keys()), key = len))
    # print(max_row_len)
    
    for row_sec_half in range(max_row_len):
        start += "\n    "
        
        for i in range(len(rounded_percent)):
            if row_sec_half < len(list(rounded_percent.keys())[i]):
                start += f" {list(rounded_percent.keys())[i][row_sec_half]} "
            else:
                start += "   "
        
    start += '\n'   
        
    # print(spent_percent)
    # print(rounded_percent)
    
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
# auto = Category("Auto")
# auto.deposit(100, "deposit")
# clothing.transfer(50, auto)
# auto.withdraw(70, 'car spray')



print(food)
print(clothing)
# print(auto)

print(create_spend_chart(food, clothing)) #, auto
