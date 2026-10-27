import streamlit as st
from datetime import date

from expense import Expense, ExpenseError, NegativeAmountError
from expense_store import save_expenses, load_expenses
from budget_store import save_budgets, load_budgets
from report import total_by_category, compare_to_budget

st.title("Expense Tracker")

expenses = load_expenses()
budgets = load_budgets()

tab1, tab2, tab3 = st.tabs(["Log Expense", "Budgets", "Report"])

with tab1:
    st.header("Log an expense")
    amount = st.number_input("Amount", min_value=0.0)
    category = st.selectbox("Category", list(budgets.keys()) if budgets else ["No categories yet"])
    expense_date = st.date_input("Date", value=date.today())

    if st.button("Save expense"):
        try:
            new_expense = Expense(amount, category, str(expense_date))
            expenses.append(new_expense)
            save_expenses(expenses)
            st.success("Expense saved!")
        except ExpenseError as error:
            st.error(f"Could not save: {error}")

with tab2:
    st.header("Set your budgets")
    category_name = st.text_input("Category name")
    budget_amount = st.number_input("Budget amount", min_value=0.0)
    if st.button("Save budget"):
        budgets[category_name] = budget_amount
        save_budgets(budgets)
        st.success("Budget saved!")

with tab3:
    st.header("Monthly report")
    totals = total_by_category(expenses)
    comparison = compare_to_budget(totals, budgets)
    for category, data in comparison.items():
        st.write(f"{category}: spent ₦{data['spent']}, budget ₦{data['budget']}, remaining ₦{data['remaining']}")
        if data["over_budget"]:
            st.warning(f"You're over budget on {category}!")

