# expense-tracker
A personal expense tracker that logs spending by category, compares it against budgets you set, and gives simple advice on where to cut back or invest more.
## What it does 
- Logs expense as they happen: enter an amount and a category (e.g. feeding, transport, investing) each time you spend
- Set a budget per category: decide once how much you want to spend on each category per month. These budgets are saved and reused every month until you change them
- Weekly and monthly totals: the app adds up what you have spent, by week and by month, automatically.
- Budget comparison and advice: see how close you are to (or how far over) each category's budget, with simple suggestions like "reduce feeding" or "add more to investing."
- Visual report: a chart comparing your budget vs actual spending per category.
### Project Structure
-----main.py #The streamlit app(the screen you see)
-----expense.py #Expense class, holds one logged expense
-----budget_store.py #saves/loads your category budget
-----expense_store.py #saves/loads all logged expenses
-----report.py #adds up totals and compares against budgets
-----advisor.py #turns totals + budgets into plain-English advise
-----data/ #expenses.json and budgets.json live here
-----README.md
## Build with
-python
-streamlit(interface)
-Matplotlib(charts)

# Running it
streamlit run main.py

## python concepts used
-- OOP
-- File handling
-- Exception handling
-- Data visualization
-- GUI
