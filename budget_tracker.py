import json
import os
from transaction import Transaction
from budget_utils import calculate_totals, group_by_category

class BudgetTracker:
    def __init__(self):
        self.transactions = self.load_transactions()

    def load_transactions(self):
        if os.path.exists("transactions.json"):
            with open("transactions.json", "r") as file:
                data = json.load(file)
                return [Transaction(transaction["category"], transaction["amount"]) for transaction in data]
        else:
            return []

    def save_transactions(self):
        with open("transactions.json", "w") as file:
            json.dump([{"date": transaction.date, "category": transaction.category, "amount": transaction.amount} for transaction in self.transactions], file)

    def add_transaction(self):
        category = input("Enter transaction category: ")
        while True:
            try:
                amount = float(input("Enter transaction amount: "))
                break
            except ValueError:
                print("Invalid amount input. Please try again.")
        transaction = Transaction(category, amount)
        self.transactions.append(transaction)
        self.save_transactions()
        print("Transaction added successfully.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def calculate_budget(self):
        transactions_by_category = group_by_category(self.transactions)
        totals = calculate_totals(transactions_by_category)
        for category, total in totals.items():
            print(f"{category}: ${total:.2f}")

def main():
    budget_tracker = BudgetTracker()
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Calculate budget")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            budget_tracker.add_transaction()
        elif choice == "2":
            budget_tracker.view_transactions()
        elif choice == "3":
            budget_tracker.calculate_budget()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
