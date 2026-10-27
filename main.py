import streamlit as st
import matplotlib.pyplot as plt
from datetime import date

from expense import Expense, ExpenseError, NegativeAmountError
from expense_store import save_expenses, load_expenses
from budget_store import save_budgets, load_budgets
from report import total_by_category, compare_to_budget

st.title("Expense Tracker")
st.set_page_config(page_title="Expense Tracker", layout="wide", page_icon="💰")
st.markdown("""
    <style>
    [data-testid="stMetricValue"] {
        font-size: 1.1rem;
    }
    [data-testid="stMetricLabel"] {
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

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
        col1, col2, col3 = st.columns(3)
        col1.metric("Category", category)
        col2.metric("Spent", f"₦{data['spent']:,.0f}")
        col3.metric("Budget", f"₦{data['budget']:,.0f}")
        if data["over_budget"]:
            st.warning(f"You're over budget on {category}!")

    if totals:
        categories = list(totals.keys())
        spent_values = [totals[c] for c in categories]
        budget_values = [budgets.get(c, 0) for c in categories]

        fig, ax = plt.subplots(figsize=(6, 3))
        plt.rcParams.update({'font.size': 8})
        x = range(len(categories))
        ax.bar(x, spent_values, width=0.4, label="Spent")
        ax.bar([i + 0.4 for i in x], budget_values, width=0.4, label="Budget")
        ax.set_xticks([i + 0.2 for i in x])
        ax.set_xticklabels(categories, rotation=45)
        ax.legend()
        st.pyplot(fig, use_container_width=False)

    st.subheader("Delete an expense")
    if expenses:
        options = [f"{i}: {str(e)}" for i, e in enumerate(expenses)]
        choice = st.selectbox("Pick an expense to delete", options)
        if st.button("Delete expense"):
            index = int(choice.split(":")[0])
            expenses.pop(index)
            save_expenses(expenses)
            st.success("Deleted. Refresh to see updated report.")
