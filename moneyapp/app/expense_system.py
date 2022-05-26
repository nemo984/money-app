from typing import Optional, List
from .helpers import Observable
from .model import Expense, Category, Account


class ExpenseSystem(Observable):
    def __init__(self, owner):
        super().__init__()
        self.owner = owner
        self._expenses = []

    def add(
        self,
        category: Category,
        amount: float,
        frequency: Optional[int] = None,
        note: Optional[str] = None,
    ) -> Expense:
        expense = Expense(owner=self.owner, category=category,
                          amount=amount, frequency_day=frequency, note=note)
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
        category: Optional[Category] = None,
        amount: Optional[float] = None,
        frequency: Optional[int] = None,
        note: Optional[str] = None,
    ) -> Expense:
        if category:
            expense.category = category
        if amount:
            expense.amount = amount
        if frequency:
            expense.frequency_day = frequency
        if note:
            expense.note = note
        expense.save()
        self.get()
        return expense

    def delete(self, expense: Expense):
        owner = expense.owner
        expense.delete_instance()
        self.get()
