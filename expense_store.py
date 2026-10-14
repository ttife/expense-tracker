import json 
from expense import Expense

def save_expenses(expenses):
    expense_dicts = []
    for expense in expenses:
        expense_dicts.append(expense.to_dict())

    with open("expenses.json", "w") as f:
        json.dump(expense_dicts, f)

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            expense_dicts = json.load(f)
    except FileNotFoundError as error:
        return []
    expenses = []
    for item in expense_dicts:
        expenses.append(Expense.from_dict(item))
    return expenses