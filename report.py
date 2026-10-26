from datetime import datetime


def total_by_category(expenses):
    # adds up all expense amounts, grouped by category
    totals = {}
    for expense in expenses:
        if expense.category not in totals:
            totals[expense.category] = 0
        totals[expense.category] += expense.amount
    return totals


def total_for_month(expenses, year, month):
    # adds up all expenses that fall in a given year/month
    total = 0
    for expense in expenses:
        expense_date = datetime.strptime(expense.date, "%Y-%m-%d")
        if expense_date.year == year and expense_date.month == month:
            total += expense.month
    return total


def compare_to_budget(totals, budgets):
    # for each category, work out how much is left (or over) vs its budget
    comparison = {}
    for category in budgets:
        spent = totals.get(category, 0)
        budget = budgets[category]
        comparison[category] = {
            "spent": spent,
            "budget": budget,
            "remaining": budget - spent,
            "over_budget": spent > budget,
        }
    return comparison