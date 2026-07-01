# Project 3: Personal Expense Tracker

# Initialize an empty list 
expense_log = []
monthly_budget = float(input("Set your Monthly Budget (Rs.): "))


# Function to add a new expense
def add_expense():
    print("\nAdd Expense ")
    description = input("Enter Description: ")
    category = input("Enter Category (Food/Travel/Bills/Other): ")
    amount = float(input("Enter Amount (Rs.): "))
    date = input("Enter Date (DD-MM-YYYY): ")

    # Save details into a dictionary and add it to our tracking list
    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date,
    }
    expense_log.append(expense)
    print("Expense added!")


# Function to show all expenses
def view_expenses():
    print("\nAll Expenses ")
    if not expense_log:
        print("No expenses recorded yet.")
        return

    for item in expense_log:
        print(f"Desc: {item['description']} | Cat: {item['category']} | Price: Rs.{item['amount']} | Date: {item['date']}")


# Function to calculate totals and print the final report
def budget_report():
    print("\nBudget Report ")

    # Sum  all 'amount' values from list of dictionaries
    total_spent = 0
    for item in expense_log:
        total_spent += item["amount"]

    remaining = monthly_budget - total_spent

    print(f"Total Budget : Rs. {monthly_budget}")
    print(f"Total Spent  : Rs. {total_spent}")
    print(f"Remaining    : Rs. {remaining}")

    # Simple budget warning check
    if total_spent > monthly_budget:
        print("You have crossed your budget limit!")
    else:
        print("Your spending is under control.")


# Main Menu Loop
while True:
    print("\nEXPENSE TRACKER ")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Budget Report")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        budget_report()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Pick a number from 1 to 4.")