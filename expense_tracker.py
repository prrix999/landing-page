# PROJECT 2 — PERSONAL EXPENSE TRACKER

import json


def get_expense_list():
    try:
        with open("expenses.json", "r") as file:
            expense_list = json.load(file)
            return expense_list
    except FileNotFoundError:
        expense_list = []
        return expense_list
    except json.JSONDecodeError:
        print("Empty file or Corrupted file found!")
        exit()


def get_valid_text(txt):
    while True:
        info = input(f"Enter Your {txt}").strip()
        if not info:
            print("Enter a valid value!")
        else:
            return info


def get_valid_amount():
    while True:
        try:
            amount = float(input(f"Enter Your Expense Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero!")
            else:
                return amount
        except ValueError:
            print("Invalid Value!!")


def add_expense():
    expense_description = get_valid_text("Expense Description: ")
    expense_amount = get_valid_amount()
    expense_category = get_valid_text("Expense Category: ")
    return {"description": expense_description, "amount": expense_amount, "category": expense_category}


def get_spending_by_category(expenses):
    if not expenses:
        return {}
    else:
        category_total = {}
        for x in expenses:
            category_name = x["category"].lower()
            if category_name in category_total:
                category_total[category_name] += x["amount"]
            else:
                category_total[category_name] = x["amount"]
        return category_total


expense_list = get_expense_list()

while True:

    while True:
        try:
            option = int(input("\n\n 1. Add Expense\n 2.View All Expenses\n 3. Show Total Spending\n 4. Spending by Category\n 5. EXIT\n\n Choose An Option From Above:"))
            break
        except ValueError:
            print("Invalid Value!!")

    if option == 1:
        print("===== ADD EXPENSE =====")
        expense = add_expense()
        expense_list.append(expense)
        print("Expense Added!\n")

        with open("expenses.json", "w") as file:
            json.dump(expense_list, file, indent=4)

    elif option == 2:
        print(f"===== ALL EXPENSES =====")
        if not expense_list:
            print("No Expenses Recorded Yet.")
        else:
            for expense_no, expense_dict in enumerate(expense_list, start=1):
                print(f"{expense_no}. {expense_dict['description']} | {expense_dict['amount']} | {expense_dict['category']}")
    elif option == 3:
        print("===== TOTAL SPENDING =====")
        total_amount = sum(n['amount'] for n in expense_list)
        print(f"Your Total Spending: {total_amount}")
    elif option == 4:
        print("===== SPENDING BY CATEGORY =====")
        spending_category = get_spending_by_category(expense_list)
        if not spending_category:
            print("No Expenses Recorded Yet.")
        else:
            for category_index, (category, total) in enumerate(spending_category.items(), start=1):
                print(f"{category_index}. {category.upper()}: {total}")

    elif option == 5:
        break
    else:
        print("Invalid choice!")
