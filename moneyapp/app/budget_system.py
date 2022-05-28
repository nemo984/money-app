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
        self.history_system.add_create("Budget", f"You created a budget '{name}' for {category} category", 
        f"You created a budget name '{name}' for {category} category with an amount of {amount}, start date of {start_date} and end date of {end_date}")
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

        def remind_budget(threshold):
            self.reminder_system.add(heading=f"'{budget.name}'", message=f"This budget hits {threshold}%", budget=budget)
        if budget.progress_value > self.owner.budget_reminder_threshold2:
            remind_budget(self.owner.budget_reminder_threshold2)
        elif budget.progress_value > self.owner.budget_reminder_threshold1:
            remind_budget(self.owner.budget_reminder_threshold1)

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
        change_str = ""
        if budget is None:
            return
        if name:
            change_str += f"You change the name from '{budget.name}' to '{name}'. "
            budget.name = name
        if start_date:
            change_str += f"You change the start date from '{budget.start_date}' to '{start_date}'. "
            budget.start_date = start_date
        if category:
            change_str += f"You change the category from '{budget.category}' to '{category}'. "
            budget.category = category
        if amount:
            change_str += f"You change the amount from '{budget.amount}' to '{amount}'. "
            budget.amount = amount
        if end_date:
            change_str += f"You change the end date from '{budget.end_date}' to '{end_date}'. "
            budget.end_date = end_date
        if note:
            change_str += f"You change the note from '{budget.note}' to '{note}'. "
            budget.note = note
        budget.save()
        self.get()
        self.history_system.add_update("Budget", f"You updated the '{budget.name}' budget", f"You updated the '{budget.name}' budget." + change_str)
        return budget

    def delete(self, budget_id: int):
        budget = self.getByID(budget_id)
        if budget is None:
            return
        self.history_system.add_delete("Budget", f"You deleted the '{budget.name}' budget", f"You deleted the '{budget.name}' budget that have \
        {budget.category} category with an amount of {budget.amount}")
        budget.delete_instance()
        self.get()
