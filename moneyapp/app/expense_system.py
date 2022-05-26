from typing import Optional, List
from .helpers import Observable
from .model import Expense, Account


class ExpenseSystem(Observable):
    def __init__(self, owner):
        super().__init__()
        self.owner = owner
        self._expenses = []

    def add(
        self,
        category: str,
        amount: float,
        date,
        note: Optional[str] = None,
    ) -> Expense:
        expense = Expense(owner=self.owner, category=category, date=date
                          ,amount=amount, note=note)
        expense.save()
        self._expenses.append(expense)
        self.notify(self._expenses)
        return expense

    def get(self) -> List[Expense]:
        self._expenses = list(self.owner.expenses_ordered)
        self.notify(self._expenses)
        return self._expenses

    def update(
        self,
        expense: Expense,
        date,
        category: Optional[str] = None,
        amount: Optional[float] = None,
        note: Optional[str] = None,
    ) -> Expense:
        if date:
            expense.date = date
        if category:
            expense.category = category
        if amount:
            expense.amount = amount
        if note:
            expense.note = note
        expense.save()
        self.get()
        return expense

    def delete(self, expense: Expense):
        owner = expense.owner
        expense.delete_instance()
        self.get()
