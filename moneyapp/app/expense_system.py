from typing import Optional, List
from .helpers import Observable
from .model import Expense, Budget, Account
from .budget_system import BudgetSystem
from peewee import fn
from datetime import datetime, timedelta

class ExpenseSystem(Observable):
    def __init__(self, owner, budget_system=None, history_system=None):
        super().__init__()
        self.owner = owner
        self._expenses = []
        self.budget_system = budget_system
        self.history_system = history_system

    def add(
        self,
        category: str,
        amount: float,
        date,
        budget: Optional[Budget] = None,
        note: Optional[str] = None,
    ) -> Expense:
        expense = Expense(owner=self.owner, category=category, date=date, budget=budget
                          ,amount=amount, note=note)
        expense.save()
        self._expenses.append(expense)
        if budget: self.budget_system.add_amount_used(budget.id, expense.amount)
        self.notify(self._expenses)
        
        budget_name = "None" if budget is None else budget.name
        self.history_system.add_create("Expense", f"You created an expense of {amount} amount", 
        f"You created an expense of {amount} amount, category={category}, budget name ={budget_name}")
        return expense

    def get(self) -> List[Expense]:
        self._expenses = list(self.owner.expenses_ordered)
        self.notify(self._expenses)
        return self._expenses

    def getByID(self, expense_id) -> Expense:
        expense = Expense.get_or_none(Expense.id == expense_id)
        return expense

    def filter(self, query: str):
        if query == "":
            return self._expenses

        filtered_expenses = []
        for expense in self._expenses:
            currency = "฿{:,.2f}".format(expense.amount)
            budget_name = expense.budget.name if expense.budget else "" 
            s = f"{expense.date}{expense.category}{currency}{expense.category}{budget_name}"
            if query in s:
                filtered_expenses.append(expense)
        return filtered_expenses

    def update(
        self,
        expense_id: int,
        date,
        category: Optional[str] = None,
        amount: Optional[float] = None,
        note: Optional[str] = None,
    ) -> Expense:
        expense = self.getByID(expense_id)
        change_str = ""
        if expense is None:
            return
        if date:
            change_str += f"You change the start date from '{expense.date}' to '{date}'. "
            expense.date = date
        if category:
            change_str += f"You change the category from '{expense.category}' to '{category}'. "
            expense.category = category
        if amount:
            change_str += f"You change the amount from '{expense.amount}' to '{amount}'. "
            expense.amount = amount
        if note:
            change_str += f"You change the note from '{expense.note}' to '{note}'. "
            expense.note = note
        expense.save()
        self.get()
        self.history_system.add_update("Expense", "You updated an expense", change_str)
        return expense

    def remove_budget(self, budget):
        q = (Expense
                .update({Expense.budget: None})
                .where(Expense.budget == budget))
        q.execute()


    def get_categories_total(self):
        rows = (Expense
                 .select(Expense.category.alias('category'), fn.Sum(Expense.amount).alias('total'))
                 .where(Expense.owner == self.owner)
                 .group_by(Expense.category))
        return {expense.category:expense.total for expense in rows}

    def get_expenses_total(self) -> dict:
        results = {"daily": 0, "weekly": 0, "monthly": 0, "yearly": 0}
        daily = datetime.today() 
        weekly = daily - timedelta(weeks=1)
        monthly = daily - timedelta(weeks=4)
        yearly = daily - timedelta(weeks=52)
        for expense in self._expenses:
            date = datetime.strptime(expense.date, '%d/%m/%Y').date()
            if date >= daily.date():
                results["daily"] += float(expense.amount)
            if date >= weekly.date():
                results["weekly"] += float(expense.amount)
            if date >= monthly.date():
                results["monthly"] += float(expense.amount)
            if date >= yearly.date():
                results["yearly"] += float(expense.amount)
        return results

    def delete(self, expense_id):
        expense = self.getByID(expense_id)
        if expense is None:
            return
        if expense.budget is not None:
            self.budget_system.subtract_amount_used(expense.budget.id, expense.amount)

        budget_name = "None" if expense.budget is None else expense.budget.name
        note = expense.note if expense.note is not None else "" 
        self.history_system.add_delete("Expense", "You deleted an expense", 
        f"You deleted an expense that have an amount of {expense.amount}, category={expense.category}, budget name = {budget_name}, note={note}")
        expense.delete_instance()
        self.get()
