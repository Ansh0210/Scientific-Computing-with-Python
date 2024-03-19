# Function to add a new expense to the list of expenses.
def add_expense(expenses, amount, category):
    # Appends a new dictionary with amount and category to the expenses list.
    expenses.append({'amount': amount, 'category': category})
    
# Function to print all expenses.
def print_expenses(expenses):
    # Iterates over each expense in the list and prints its amount and category.
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
# Function to calculate the total of all expenses.
def total_expenses(expenses):
    # Uses sum and map functions to calculate the total amount of all expenses.
    return sum(map(lambda expense: expense['amount'], expenses))
    
# Function to filter expenses by a specific category.
def filter_expenses_by_category(expenses, category):
    # Uses filter and lambda to return expenses that match the specified category.
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    # Initializes an empty list to store expenses.
    expenses = []
    # Start a loop to continuously display the menu and prompt the user for actions.
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')  # Prompt the user to enter a choice.

        if choice == '1':
            # Option 1: Add a new expense.
            amount = float(input('Enter amount: '))  # Ask for the expense amount.
            category = input('Enter category: ')  # Ask for the expense category.
            add_expense(expenses, amount, category)  # Add the new expense to the list.

        elif choice == '2':
            # Option 2: List all expenses.
            print('\nAll Expenses:')
            print_expenses(expenses)  # Print all expenses in the list.

        elif choice == '3':
            # Option 3: Show the total of all expenses.
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            # Option 4: Filter expenses by category.
            category = input('Enter category to filter: ')  # Ask for the category to filter by.
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)  # Print expenses that match the category.

        elif choice == '5':
            # Option 5: Exit the program.
            print('Exiting the program.')
            break  # Break the loop to exit the program.
        
# Checks if the script is run as the main program and not imported as a module.
if __name__ == '__main__':
    main()  # Call the main function to run the program.
