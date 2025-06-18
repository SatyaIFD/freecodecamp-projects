# Python Expense Tracker

# Function to add a new expense to the list
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

# Function to print all expenses
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Function to calculate total of all expenses
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

# Function to filter expenses by a specific category
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

# Main function to run the interactive menu
def main():
    expenses = []  # Initialize empty list to hold expense entries

    while True:
        # Display the menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        # Get user input
        choice = input('Enter your choice: ')

        # Option 1: Add new expense
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        # Option 2: Print all expenses
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        # Option 3: Show total expense amount
        elif choice == '3':
            print('\nTotal Expenses:', total_expenses(expenses))

        # Option 4: Filter by category
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = list(filter_expenses_by_category(expenses, category))
            print_expenses(expenses_from_category)

        # Option 5: Exit the loop
        elif choice == '5':
            print('Exiting the program.')
            break

        # Handle invalid input
        else:
            print('Invalid choice. Please enter a number from 1 to 5.')

# Start the program
main()
