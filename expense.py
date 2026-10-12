import datetime

class ExpenseError(Exception):
    pass
class NegativeAmountError(ExpenseError):
    pass

class Expense:
    def __init__(self, amount, category, date):
        if date == None:
            raise ExpenseError("Missing Date")
        try:
            number = float(amount)
        except (TypeError, ValueError):
            raise ExpenseError ("Amount is not a number")
        if number < 0:
            raise NegativeAmountError("amount can't be negative")
        self.amount = number
        self.category = category
        self.date = date
    def to_dict(self):
        return{
            'amount': self.amount,
            'category': self.category,
            'date': self.date
        }
    @staticmethod
    def from_dict(data):
        return Expense(
            amount=data.get('amount'),
            category=data.get('category'),
            date=data.get('date')
        )
    def __str__(self):
        return f"You spent #{self.amount} on {self.category} on {self.date}"