from .helpers import Observable
from .model import *
from typing import Optional, List

class ExpenseSystem(Observable):
    def __init__(self):
        super().__init__()
        self._expenses = []

    def add(
        self,
        owner: Account,
        category: Category,
        amount: float,
        frequency: Optional[int] = None,
        note: Optional[str] = None,
    ):
        expense = Expense(owner=owner, category=category, 
                        amount=amount, frequency_day=frequency, note=note)
        expense.save()
        self._expenses.append(expense)
        print("Expenses updated: Notifying observers")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
        self.notify(self._expenses)

    def get(self, account: Account) -> List[Expense]:
        self._expenses = account.expenses_ordered
        self.notify(self._expenses)
        return self._expenses

    def update():
        pass

    def delete():
        pass
