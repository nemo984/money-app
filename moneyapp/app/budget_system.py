from typing import Optional, List
from datetime import datetime
from .helpers import Observable
from .model import *


class BudgetSystem(Observable):
    def __init__(self):
        super().__init__()
        self._budgets = []

    def add(
        self,
        owner: Account,
        category: Category,
        amount: float,
        end_date: Optional[datetime] = None,
        note: Optional[str] = None,
    ) -> Budget:
        budget = Budget(owner=owner, category=category,
                        amount=amount, end_date=end_date, note=note)
        budget.save()
        self._budgets.append(budget)
        print("Budget updated: Notifying observers")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
        self.notify(self._budgets)
        return budget

    def get(self, account: Account) -> List[Budget]:
        self._budgets = account.budgets_ordered
        self.notify(self._budgets)
        return self._budgets

    def update(
        self,
        budget: Budget,
        category: Optional[Category] = None,
        amount: Optional[float] = None,
        end_date: Optional[datetime] = None,
        note: Optional[str] = None,
    ) -> Budget:
        if category:
            budget.category = category
        if amount:
            budget.amount = amount
        if end_date:
            budget.end_date = end_date
        if note:
            budget.note = note
        budget.save()
        self.get(budget.owner)
        return budget

    def delete(self, budget: Budget):
        owner = budget.owner
        budget.delete_instance()
        self.get(owner)
