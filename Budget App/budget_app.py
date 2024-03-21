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
        return amount < self.get_balance()
             

def create_spend_chart(*categories):
    
    start = "Percentage spent by category:"
    
    for categ in categories:
        pass
    
    print(start)
    


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# food.deposit(2, 'test deposit')
food.get_balance()
food.check_funds(50)
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(300, 'Paycheck came in')
clothing.withdraw(65, 'Nike Sweats')
clothing.transfer(30, food)
print(food)
print(clothing)

create_spend_chart(food, clothing)
