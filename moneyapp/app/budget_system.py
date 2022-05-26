from typing import Optional, List
from datetime import datetime
from .helpers import Observable
from .model import Budget, Account

class BudgetSystem(Observable):
    def __init__(self, owner: Account):
        super().__init__()
        self.owner = owner
        self._budgets = []

    def add(
        self,
        category: str,
        amount: float,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        note: Optional[str] = None,
    ) -> Budget:
        budget = Budget(owner=self.owner, category=category,
                        amount=amount, start_date=start_date, end_date=end_date, note=note)
        budget.save()
        self._budgets.append(budget)
        self.notify(self._budgets)
        return budget

    def get(self) -> List[Budget]:
        self._budgets = list(self.owner.budgets_ordered)
        self.notify(self._budgets)
        return self._budgets

    def update(
        self,
        budget: Budget,
        category: Optional[str] = None,
        amount: Optional[float] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        note: Optional[str] = None,
    ) -> Budget:
        if start_date:
            budget.start_date = start_date
        if category:
            budget.category = category
        if amount:
            budget.amount = amount
        if end_date:
            budget.end_date = end_date
        if note:
            budget.note = note
        budget.save()
        self.get()
        return budget

    def delete(self, budget_id: int):
        budget = Budget.get(Budget.id == budget_id)
        budget.delete_instance()
        self.get()
