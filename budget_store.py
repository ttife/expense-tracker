import json

def load_budgets():
    try:
        with open("budgets.json", "r") as f:
            budgets = json.load(f)
    except FileNotFoundError as error:
        return {}
    return budgets

def save_budgets(budgets):
    with open("budgets.json", "w") as f:
        json.dump(budgets, f)