class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Category\tAmount")
            for expense in self.expenses:
                print(f"{expense['category']}\t\t${expense['amount']}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total expenses: ${total}")

    def run(self):
        print("Welcome to Expense Tracker!")
        while True:
            print("\nChoose an option:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Calculate Total Expenses")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: $"))
                self.add_expense(category, amount)
                print("Expense added successfully!")
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.total_expenses()
            elif choice == '4':
                print("Thank you for using Expense Tracker!")
                break
            else:
                print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    expense_tracker = ExpenseTracker()
    expense_tracker.run()
