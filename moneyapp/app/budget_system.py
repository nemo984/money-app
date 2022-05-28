from typing import Optional, List
from datetime import datetime
from .helpers import Observable
from .model import Budget, Account
import decimal

class BudgetSystem(Observable):
    def __init__(self, owner: Account, reminder_system, history_system):
        super().__init__()
        self.owner = owner
        self._budgets = []
        self.reminder_system = reminder_system
        self.history_system = history_system

    def add(
        self,
        name: str,
        category: str,
        amount: float,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        note: Optional[str] = None,
    ) -> Budget:
        budget = Budget(owner=self.owner, category=category, name=name,
                        amount=amount, start_date=start_date, end_date=end_date, note=note)
        budget.save()
        self._budgets.append(budget)
        self.notify(self._budgets)
        self.history_system.add(
            action="Budget", action_type="Create", description="You created a budget")
        return budget

    def get(self) -> List[Budget]:
        self._budgets = list(self.owner.budgets_ordered)
        self.notify(self._budgets)
        return self._budgets

    def get_without_notify(self):
        return self._budgets

    def getByCategory(self, category: str) -> List[Budget]:
        categories = Budget.select().where(Budget.category == category)
        return list(categories)

    def getByID(self, budget_id) -> Budget:
        budget = Budget.get_or_none(Budget.id == budget_id)
        return budget

    def add_amount_used(self, budget_id, amount) -> Budget:
        budget = self.getByID(budget_id)
        if budget is None:
            return
        budget.amount_used += decimal.Decimal(amount)
        budget.save()
        self.get()
        if budget.progress_value > self.owner.budget_reminder_threshold1:
            self.reminder_system.add(heading=f"Budget '{budget.name}'", message=f"This budget hits {self.owner.budget_reminder_threshold1}%")
        elif budget.progress_value > self.owner.budget_reminder_threshold2:
            self.reminder_system.add(heading=f"Budget '{budget.name}'", message=f"This budget hits {self.owner.budget_reminder_threshold1}%")
        return budget
    
    def subtract_amount_used(self, budget_id, amount) -> Budget:
        budget = self.getByID(budget_id)
        if budget is None:
            return
        budget.amount_used -= decimal.Decimal(amount)
        budget.save()
        self.get()
        return budget

    def update(
        self,
        budget_id: Budget,
        name: Optional[str] = None,
        category: Optional[str] = None,
        amount: Optional[float] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        note: Optional[str] = None,
    ) -> Budget:
        budget = self.getByID(budget_id)
        if budget is None:
            return
        if name:
            budget.name = name
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
        self.history_system.add(
            action="Budget", action_type="Update", description="You updated a budget")
        return budget

    def delete(self, budget_id: int):
        budget = self.getByID(budget_id)
        if budget is None:
            return
        budget.delete_instance()
        self.history_system.add(
            action="Budget", action_type="Delete", description="You deleted a budget")
        self.get()
