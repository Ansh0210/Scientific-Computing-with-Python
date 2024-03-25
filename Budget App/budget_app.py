class Category:
    def __init__(self, name):
        # Initialize the category with a name and an empty ledger list for transactions
        self.name = name
        self.ledger = []

    def __str__(self):
        # Provide a string representation of the category, including its ledger
        display = f"{self.name.center(30, '*')}\n"
        
        # Format and add each transaction to the display string
        for item in self.ledger:
            display += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        
        # Calculate and display the total balance
        total = self.get_balance()
        display += f"Total: {total:.2f}\n"
        
        return display

    def deposit(self, amount, description=""):
        # Record a deposit in the ledger as a positive amount
        self.ledger.append({'amount': amount, 'description': description})
        
    def withdraw(self, amount, description=""):
        # Withdraw funds if enough balance is available, and record it as a negative amount
        if not self.check_funds(amount):
            return False
        
        self.ledger.append({'amount': -amount, 'description': description})
        return True
        
    def get_balance(self):
        # Calculate and return the current balance of the category
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
            
        return balance    
    
    def transfer(self, amount, target_category):
        # Transfer funds from this category to another category if funds are sufficient
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {target_category.name}')
            target_category.deposit(amount, f'Transfer from {self.name}') 
            return True
        return False
    
    def check_funds(self, amount):
        # Check if the amount can be withdrawn or transferred without overdrawing
        return amount <= self.get_balance()

def create_spend_chart(categories):
    # Create a chart representing the percentage of expenses in each category
    
    start = "Percentage spent by category"
    categ_spent = []
    
    # Calculate total spent in each category
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        categ_spent.append(spent)
    
    total_spent = sum(categ_spent)
    spent_percent = [(spent / total_spent) * 100 for spent in categ_spent]
    
    # Generate the chart string, starting with percentages
    for percent in range(100, -10, -10):
        start += f"\n{percent:>3}|"
        for val in spent_percent:
            start += ' o ' if val >= percent else '   '
        start += ' '
    
    # Add the bottom border of the chart
    start += f"\n    {'-' * (len(categories) * 3 + 1)}"
    
    # Find the longest category name for vertical label alignment
    max_len = max(len(category.name) for category in categories)
    
    # Add category names vertically to the bottom of the chart
    for i in range(max_len):
        start += "\n    "
        for category in categories:
            char = category.name[i] if i < len(category.name) else ' '
            start += f" {char} "
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
