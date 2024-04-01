# EXPENSE TRACKER [OWN VERSION]
class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def get_user_choice(self):
        OPTIONS = {
            '1': 'Add an Expense',
            '2': 'Print List of Expenses',
            '3': 'Print Total of Expenses',
            '4': 'Filter an Expense by Category',
            '5': 'Delete an Expense',
            '6': 'Clear All Expenses',
            '7': 'Exit'
        }
        print("OPTIONS:")
        for index, option in OPTIONS.items():
            print(f"{index}. {option}")
        user_choice = input("Type the number: ")
        return user_choice
    
    # Check If List is Empty
    def check_list(self):
        if self.expenses == []:
            print("List is empty")
            return self.run()

    # Check Duplicate Method
    def check_duplicate(self, item):
        if list(item):
            while True:
                choice = input("Item has a duplicate. Continue?[Y/N]: ").lower()
                if choice not in ('y', 'n'):
                    print("Invalid Input")
                    continue
                if choice == 'n':
                    return self.run()
                break

    # Add Expense Method
    def add_expense(self, description, amount):
        self.expenses.append({'description': description, 'amount': amount})

    # Print List of Expenses Method
    def list_of_expenses(self, expenses):
        for expense in expenses:
            print(f"Description: {expense['description']}, Amount: {expense['amount']}")

    # Print Total Expenses Method
    def total_expenses(self):
        print(sum(map(lambda expense: expense['amount'], self.expenses)))

    # Filter Expenses by Category Method
    def filter_expenses(self, description):
        return filter(lambda expense: expense['description'] == description, self.expenses)

    # Delete Expense Method
    def delete_expense(self, description):
        for expense in self.expenses:
            if expense['description'] == description:
                self.expenses.remove(expense)
                print("Updated List:")
                self.check_list()
                for kept_item, amount in self.expenses:
                    print(f"Description: {kept_item}, Amount: {amount}")
                    return self.run()
            print("Item not found")

    # Clear Expenses Method
    def clear_expenses(self):
        self.expenses = []
        print("Expenses Cleared")

    # Run Method    
    def run(self):
        while True:
            user_choice = self.get_user_choice()
            if user_choice == '1':
                description = input("Description: ").lower()
                item = filter(lambda expense: expense['description'] == description, self.expenses)
                self.check_duplicate(item)
                while True:
                    try:
                        amount = int(input("Amount: "))
                        self.add_expense(description, amount)
                        break
                    except:
                        print("Invalid Amount")

            elif user_choice == '2':
                self.check_list()
                self.list_of_expenses(self.expenses)

            elif user_choice == '3':
                self.check_list()
                self.total_expenses()

            elif user_choice == '4':
                self.check_list()
                description = input("Description: ").lower()
                result = self.filter_expenses(description)
                if not list(result):
                    print("Item not found")
                    continue
                self.list_of_expenses(result)

            elif user_choice == '5':
                self.check_list()
                description = input("Enter the description you want to delete: ").lower()
                self.delete_expense(description)

            elif user_choice == '6':
                self.check_list()
                self.clear_expenses()

            elif user_choice == '7':
                break

            else:
                print("Options are 1-7 only.")
                continue

# Main Method
def main():
    run_program = ExpenseTracker()
    run_program.run()

if __name__ == '__main__':
    main()