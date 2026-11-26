# Expense Tracker Project
from datetime import datetime

expenses = []


def add_expense():
    print("\n========== ADD EXPENSE ==========")

    while True:
        date = input("Enter Date (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(date, "%d-%m-%Y")
            break
        except ValueError:
            print("Please enter a valid date in DD-MM-YYYY format.")

    category = input("Enter Category: ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Enter Category: ").strip()

    description = input("Enter Description: ").strip()
    while not description:
        print("Description cannot be empty.")
        description = input("Enter Description: ").strip()

    while True:
        try:
            amount = float(input("Enter Amount (Rs.): "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid numeric amount.")

    expenses.append({
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount,
    })
    print("Expense Added Successfully!")


def view_expenses():
    print("\n========== EXPENSE RECORDS ==========")
    if not expenses:
        print("No expenses recorded.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print(f"Date: {expense['Date']}")
        print(f"Category: {expense['Category']}")
        print(f"Description: {expense['Description']}")
        print(f"Amount: Rs. {expense['Amount']:.2f}")


def calculate_total():
    total = sum(expense["Amount"] for expense in expenses)
    print("\n========== EXPENSE SUMMARY ==========")
    print("Total Expenses:", len(expenses))
    print(f"Total Amount Spent: Rs. {total:.2f}")


def main():
    print("===== EXPENSE TRACKER =====")

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
