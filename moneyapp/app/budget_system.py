from .helpers import Observable
from .model import *
from typing import Optional
from datetime import datetime

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
    ):
        budget = Budget(owner=owner, category=category, 
                        amount=amount, end_date=end_date, note=note)
        budget.save()
        self._budgets.append(budget)
        print("Budget updated: Notifying observers")
        print(">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<")
        self.notify(self._budgets)

    def get(self, account: Account) -> List[Budget]:
        self._budgets = account.budgets_ordered
        self.notify(self._budgets)
        return self._budgets

    def update():
        pass

    def delete():
        pass
