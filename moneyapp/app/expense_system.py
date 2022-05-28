from typing import Optional, List
from .helpers import Observable
from .model import Expense, Budget, Account
from .budget_system import BudgetSystem
from peewee import fn


class ExpenseSystem(Observable):
    def __init__(self, owner, budget_system, history_system):
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
        self.history_system.add(
            action="Expense", action_type="Create", description="You created a new expense")
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
            return self.get()

        filtered_expenses = []
        for expense in self._expenses:
            currency = "฿{:,.2f}".format(expense.amount)
            budget_name = expense.budget.name if expense.budget else "" 
            s = f"{expense.date}{expense.category}{currency}{expense.category}{budget_name}"
            if query in s:
                filtered_expenses.append(expense)
        self.notify(filtered_expenses)
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
        if expense is None:
            return
        if date:
            expense.date = date
        if category:
            expense.category = category
        if note:
            expense.note = note
        expense.save()
        self.get()
        self.history_system.add(
            action="Expense", action_type="Update", description="You updated your expense")
        return expense

    def get_categories_total(self):
        rows = (Expense
                 .select(Expense.category.alias('category'), fn.Sum(Expense.amount).alias('total'))
                #  .where(Expense.date.between(from_date, to_date))
                 .group_by(Expense.category))
        return {expense.category:expense.total for expense in rows}

    def delete(self, expense_id):
        expense = self.getByID(expense_id)
        if expense is None:
            return
        if expense.budget is not None:
            self.budget_system.subtract_amount_used(expense.budget.id, expense.amount)
        expense.delete_instance()
        self.get()
        self.history_system.add(
            action="Expense", action_type="Delete", description="You deleted your expense")
