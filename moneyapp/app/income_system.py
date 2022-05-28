from typing import Optional, List
from .helpers import Observable
from .model import Income, Account
from datetime import datetime, timedelta

class IncomeSystem(Observable):
    def __init__(self, owner, history_system):
        super().__init__()
        self.owner = owner
        self._incomes = []
        self.history_system = history_system

    def add(
        self,
        name: str,
        category: str,
        amount: float,
        date,
        note: Optional[str] = None,
        recurrence: Optional[str] = None,
    ) -> Income:
        income = Income(owner=self.owner, name=name, category=category, date=date,
                        amount=amount, note=note,
                        recurrence=recurrence)
        income.save()
        self._incomes.append(income)
        self.notify(self._incomes)
        self.history_system.add(
            action="Income", action_type="Create", description="You created a income")
        return income

    def get(self) -> List[Income]:
        self._incomes = list(self.owner.incomes_ordered)
        self.notify(self._incomes)
        return self._incomes

    def getByID(self, income_id) -> Income:
        income = Income.get_or_none(Income.id == income_id)
        return income

    def filter(self, query: str):
        if query == "":
            return self.get()

        filtered_incomes = []
        for income in self._incomes:
            currency = "฿{:,.2f}".format(income.amount)
            s = f"{income.date}{income.name}{income.category}{currency}{income.recurrence}"
            if query in s:
                filtered_incomes.append(income)
        self.notify(filtered_incomes)
        return filtered_incomes

    def get_incomes_total(self) -> dict:
        results = {"daily": 0, "weekly": 0, "monthly": 0, "yearly": 0}
        for income in self._incomes:
            recurrence = income.recurrence
            if recurrence in results:
                results[recurrence] += income.amount
        return results

    def update(
        self,
        income_id: int,
        name: Optional[str] = None,
        category: Optional[str] = None,
        amount: Optional[float] = None,
        recurrence: Optional[str] = None,
        note: Optional[str] = None,
    ) -> Income:
        income = self.getByID(income_id)
        if income is None:
            return
        if name:
            income.name = name
        if category:
            income.category = category
        if amount:
            income.amount = amount
        if recurrence:
            income.recurrence = recurrence
        if note:
            income.note = note

        income.save()
        self.get()
        self.history_system.add(
            action="Income", action_type="Update", description="You updated a income")
        return income

    def delete(self, income_id):
        income = self.getByID(income_id)
        if income is None:
            return
        income.delete_instance()
        self.get()
        self.history_system.add(
            action="Income", action_type="Delete", description="You deleted a income")
