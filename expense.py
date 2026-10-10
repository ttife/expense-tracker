import datetime

class ExpenseError(Exception):
    pass
class NegativeAmountError(ExpenseError):
    pass

class Expense:
    def __init__(self, amount, category, date):
        if date == None:
            raise ExpenseError("Missing Date")
        if amount < 0:
            raise NegativeAmountError("amount can't be negative")
        