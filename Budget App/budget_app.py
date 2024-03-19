class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        pass

    def deposit(self, amount, description=""):
        pass
    
    def withdraw(self, amount, description=""):
        pass
    
    def get_balance(self):
        pass
    
    def transfer(self, amount, category):
        pass
    
    def check_funds(self, amount):
        pass

def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)